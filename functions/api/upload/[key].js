// Cloudflare Pages Function - fetch or delete a single uploaded object by key.
// Password-gated the same way as functions/api/upload.js.

export async function onRequestGet(context) {
  const { env, request, params } = context;
  const password = new URL(request.url).searchParams.get("password");
  if (!password || password !== env.UPLOAD_PASSWORD) {
    return new Response(JSON.stringify({ error: "wrong password" }), {
      status: 401,
      headers: { "content-type": "application/json" },
    });
  }
  const obj = await env.UPLOADS.get(params.key);
  if (!obj) {
    return new Response(JSON.stringify({ error: "not found" }), {
      status: 404,
      headers: { "content-type": "application/json" },
    });
  }
  return new Response(obj.body, {
    headers: {
      "content-type": obj.httpMetadata?.contentType || "application/octet-stream",
      "content-disposition": `attachment; filename="${params.key}"`,
      "cache-control": "no-store",
    },
  });
}

export async function onRequestDelete(context) {
  const { env, request, params } = context;
  const password = new URL(request.url).searchParams.get("password");
  if (!password || password !== env.UPLOAD_PASSWORD) {
    return new Response(JSON.stringify({ error: "wrong password" }), {
      status: 401,
      headers: { "content-type": "application/json" },
    });
  }
  await env.UPLOADS.delete(params.key);
  return new Response(JSON.stringify({ deleted: params.key }), {
    headers: { "content-type": "application/json" },
  });
}
