// Cloudflare Pages Function - password-gated: mints short-lived presigned PUT
// URLs so the browser can stream a file straight into R2 over the S3 API,
// bypassing the 128MB memory ceiling that /api/upload.js's buffered
// multipart path has (Workers can't hold a 300MB+ file in memory at once).
// See AGENTS.md "Hosting" section for the full design note.

import { AwsClient } from "../../_lib/aws4fetch.js";

const MAX_FILE_BYTES = 2 * 1024 * 1024 * 1024; // 2GB per file (direct-to-R2 path)
const MAX_BUCKET_BYTES = 8 * 1024 * 1024 * 1024; // 8GB soft cap (R2 free tier is 10GB)
const ACCOUNT_ID = "c1cdb682c763bbc327546ccc4e33278c"; // not secret - same account ID already used for wrangler deploys
const BUCKET = "powerapps-uploads";
const URL_TTL_SECONDS = 6 * 60 * 60; // 6 hours - generous headroom for a big file on a slow link

const CORS_HEADERS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET, POST, DELETE, OPTIONS",
  "access-control-allow-headers": "content-type",
};

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: { "content-type": "application/json", "cache-control": "no-store", ...CORS_HEADERS },
  });
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

function sanitizeName(name) {
  return (name || "file").replace(/[^a-zA-Z0-9._-]/g, "_").slice(-150);
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

// Body: { password, files: [{ name, size }] } - returns one presigned PUT URL
// per file. The browser then PUTs the raw file bytes straight to that URL
// (see index.html's upload script) - this Function never sees the file body.
export async function onRequestPost(context) {
  const { env, request } = context;

  const body = await request.json().catch(() => null);
  if (!body || !body.password || body.password !== env.UPLOAD_PASSWORD) {
    return json({ error: "wrong password" }, 401);
  }

  const files = Array.isArray(body.files) ? body.files : [];
  if (files.length === 0) {
    return json({ error: "no files provided" }, 400);
  }

  for (const f of files) {
    if (!f || typeof f.size !== "number" || f.size <= 0) {
      return json({ error: "each file needs a name and size" }, 400);
    }
    if (f.size > MAX_FILE_BYTES) {
      return json({ error: `"${f.name}" is over the 2GB per-file limit` }, 413);
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

  if (!env.R2_ACCESS_KEY_ID || !env.R2_SECRET_ACCESS_KEY) {
    return json({ error: "Direct uploads aren't configured yet - missing R2 API credentials" }, 500);
  }

  const r2 = new AwsClient({
    accessKeyId: env.R2_ACCESS_KEY_ID,
    secretAccessKey: env.R2_SECRET_ACCESS_KEY,
  });

  const presigned = [];
  for (const f of files) {
    const key = `${new Date().toISOString().replace(/[:.]/g, "-")}__${sanitizeName(f.name)}`;
    const signUrl = new URL(`https://${ACCOUNT_ID}.r2.cloudflarestorage.com/${BUCKET}/${encodeURIComponent(key)}`);
    signUrl.searchParams.set("X-Amz-Expires", String(URL_TTL_SECONDS));
    const signed = await r2.sign(new Request(signUrl, { method: "PUT" }), { aws: { signQuery: true } });
    presigned.push({ key, name: f.name, size: f.size, url: signed.url });
  }

  return json({ presigned });
}
