// Cloudflare Pages Function - password-gated multi-file upload into R2.
// Storage safeguards (so this can never silently run away past the R2 free
// tier): a bucket lifecycle rule auto-deletes every object after 14 days
// (set via the R2 API, not enforced here), plus this Function enforces a
// per-file size cap and a total-bucket-size cap before accepting a write.
// See AGENTS.md "Hosting" section for the full design note.

const MAX_FILE_BYTES = 25 * 1024 * 1024; // 25MB per file
const MAX_BUCKET_BYTES = 8 * 1024 * 1024 * 1024; // 8GB soft cap (R2 free tier is 10GB)

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });
}

function sanitizeName(name) {
  return (name || "file")
    .replace(/[^a-zA-Z0-9._-]/g, "_")
    .slice(-150);
}

async function currentBucketBytes(bucket) {
  let total = 0;
  let cursor;
  do {
    const page = await bucket.list({ cursor });
    for (const obj of page.objects) total += obj.size;
    cursor = page.truncated ? page.cursor : undefined;
  } while (cursor);
  return total;
}

export async function onRequestPost(context) {
  const { env, request } = context;

  const form = await request.formData();
  const password = form.get("password");
  if (!password || password !== env.UPLOAD_PASSWORD) {
    return json({ error: "wrong password" }, 401);
  }

  const files = form.getAll("files").filter((f) => f && typeof f.arrayBuffer === "function");
  if (files.length === 0) {
    return json({ error: "no files provided" }, 400);
  }

  for (const file of files) {
    if (file.size > MAX_FILE_BYTES) {
      return json({ error: `"${file.name}" is over the 25MB per-file limit` }, 413);
    }
  }

  const usedBytes = await currentBucketBytes(env.UPLOADS);
  const incomingBytes = files.reduce((sum, f) => sum + f.size, 0);
  if (usedBytes + incomingBytes > MAX_BUCKET_BYTES) {
    return json(
      { error: "Upload storage is near its safety cap (8GB). Ask for old files to be cleared, or wait for the 14-day auto-expiry." },
      507
    );
  }

  const uploaded = [];
  for (const file of files) {
    const key = `${new Date().toISOString().replace(/[:.]/g, "-")}__${sanitizeName(file.name)}`;
    await env.UPLOADS.put(key, file.stream(), {
      httpMetadata: { contentType: file.type || "application/octet-stream" },
    });
    uploaded.push({ key, name: file.name, size: file.size });
  }

  return json({ uploaded });
}

// Lists current objects - password-gated the same way, used by the upload
// box to show what's already there and by me to check what's been sent.
export async function onRequestGet(context) {
  const { env, request } = context;
  const password = new URL(request.url).searchParams.get("password");
  if (!password || password !== env.UPLOAD_PASSWORD) {
    return json({ error: "wrong password" }, 401);
  }
  const page = await env.UPLOADS.list();
  const objects = page.objects
    .sort((a, b) => new Date(b.uploaded) - new Date(a.uploaded))
    .map((o) => ({ key: o.key, size: o.size, uploaded: o.uploaded }));
  return json({ objects });
}
