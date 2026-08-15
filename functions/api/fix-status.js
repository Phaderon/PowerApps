// Cloudflare Pages Function - GET/POST fix-completion state, backed by KV.
// One KV key per "app" (?app=policy-tracker), value is a JSON object of
// {fixId: "<ISO completion timestamp>"} - the timestamp (not a bare boolean)
// is what lets a future session apply the 30-day retention rule: a fix
// completed 30+ days ago should have its whole section deleted from the
// guide, not just left collapsed. See AGENTS.md "Hosting" section.

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: {
      "content-type": "application/json",
      "cache-control": "no-store",
    },
  });
}

export async function onRequestGet(context) {
  const app = new URL(context.request.url).searchParams.get("app");
  if (!app) return json({ error: "app query param required" }, 400);
  const raw = await context.env.FIX_STATUS.get(app);
  return json(raw ? JSON.parse(raw) : {});
}

export async function onRequestPost(context) {
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ error: "invalid json body" }, 400);
  }
  const { app, id, done } = body || {};
  if (!app || !id || typeof done !== "boolean") {
    return json({ error: "app, id (string) and done (boolean) are required" }, 400);
  }
  const raw = await context.env.FIX_STATUS.get(app);
  const data = raw ? JSON.parse(raw) : {};
  if (done) {
    data[id] = new Date().toISOString();
  } else {
    delete data[id];
  }
  await context.env.FIX_STATUS.put(app, JSON.stringify(data));
  return json(data);
}
