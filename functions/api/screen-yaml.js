// Cloudflare Pages Function - password-gated paste-and-save store for Power Apps
// screen YAML, App.OnStart and the app-wide Formulas dump. One KV key per app
// (?app=<slug>), value is { order: [sectionKey,...], sections: { key: { label,
// content, updated } } }. Every method (including GET) is password-gated because
// pasted YAML can contain real email addresses. CORS is opened the same way as
// functions/api/upload.js so every app's guide site - regardless of which
// Cloudflare Pages project or repo it's hosted from - can call this one central
// API on powerapps.pages.dev instead of needing its own KV namespace.

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

function checkPassword(password, env) {
  return password && password === env.UPLOAD_PASSWORD;
}

async function loadApp(env, app) {
  const raw = await env.SCREEN_YAML.get(`app:${app}`);
  return raw ? JSON.parse(raw) : { order: [], sections: {} };
}

export async function onRequestGet(context) {
  const { env, request } = context;
  const url = new URL(request.url);
  const password = url.searchParams.get("password");
  if (!checkPassword(password, env)) return json({ error: "wrong password" }, 401);

  const app = url.searchParams.get("app");
  if (!app) return json({ error: "app query param required" }, 400);

  return json(await loadApp(env, app));
}

export async function onRequestPost(context) {
  const { env, request } = context;
  let body;
  try {
    body = await request.json();
  } catch (e) {
    return json({ error: "invalid json body" }, 400);
  }
  const { password, app, key, label, content } = body || {};
  if (!checkPassword(password, env)) return json({ error: "wrong password" }, 401);
  if (!app || !key) return json({ error: "app and key are required" }, 400);

  const data = await loadApp(env, app);
  const existing = data.sections[key];
  data.sections[key] = {
    label: label || existing?.label || key,
    content: typeof content === "string" ? content : existing?.content || "",
    updated: new Date().toISOString(),
  };
  if (!data.order.includes(key)) data.order.push(key);

  await env.SCREEN_YAML.put(`app:${app}`, JSON.stringify(data));
  return json(data);
}

export async function onRequestDelete(context) {
  const { env, request } = context;
  let body;
  try {
    body = await request.json();
  } catch (e) {
    return json({ error: "invalid json body" }, 400);
  }
  const { password, app, key } = body || {};
  if (!checkPassword(password, env)) return json({ error: "wrong password" }, 401);
  if (!app || !key) return json({ error: "app and key are required" }, 400);

  const data = await loadApp(env, app);
  delete data.sections[key];
  data.order = data.order.filter((k) => k !== key);

  await env.SCREEN_YAML.put(`app:${app}`, JSON.stringify(data));
  return json(data);
}
