# Per-Project GitHub Repo Workflow

Last checked: 2026-06-23

When a new app is agreed upon, create a dedicated GitHub repository under the `PhadeDev` organisation. This gives the project its own issues tracker, its own GitHub Pages for screen YAML copy pages, and keeps it cleanly separate from the guide library at `Phaderon/PowerApps`.

---

## Step 1 — Agree on App Name

Confirm the app name with the user before creating the repo. The name should be:
- Descriptive and short: "Staff Tracker", "Coffee Break Tracker", "Asset Register"
- The repo slug is the kebab-case version: `staff-tracker`, `coffee-break-tracker`, `asset-register`

---

## Step 2 — Create the Repo

```bash
gh repo create PhadeDev/APP-SLUG \
  --description "Power Apps canvas app — APP FULL NAME" \
  --private \
  --add-readme
```

Then enable Issues (on by default), and configure GitHub Pages:

```bash
# Create the docs/ folder structure
mkdir -p /var/home/Phaderon/PowerApps-Apps/APP-SLUG/docs/screens

# Create the initial index.html (from the app index template — see below)
# Copy the template and fill in app-specific content

# Initialise git and push
cd /var/home/Phaderon/PowerApps-Apps/APP-SLUG
git init
git remote add origin https://github.com/PhadeDev/APP-SLUG.git
git add .
git commit -m "Initial commit: Power Apps canvas app project"
git push -u origin main
```

Enable GitHub Pages from the repo Settings → Pages → Source: `main` branch, `/docs` folder.

**Pages URL:** `https://phadedev.github.io/APP-SLUG/`

---

## Step 3 — Create Screen HTML Pages

For each screen YAML, write the YAML to a temp file, then wrap it with pa-yaml-wrap. **Always pass `--version`** — this stamps the version and local build time onto every page so the user can tell at a glance whether GitHub Pages has served the latest push.

```bash
pa-yaml-wrap /tmp/scrHome.yaml /var/home/Phaderon/PowerApps-Apps/APP-SLUG/docs/screens/scrHome.html --version v1.0
```

The tool adds CRLF enforcement, produces a standalone copy-button HTML page, and stamps the bottom-right corner with e.g. `v1.0  —  Built 23 Jun 2026  11:02 BST` using the system local time.

**Version convention:**
- Start every app at `v1.0`
- Bump the minor number (`v1.1`, `v1.2`) for bug fixes and field-level changes
- Bump the major number (`v2.0`) for structural redesigns or added screens
- Every push that changes screen content must re-wrap with the new version so the stamp changes

**Also stamp `docs/index.html`** with the same version. Add directly below the `<h1>`:
```html
<h1>APP_FULL_NAME <span style="font-size:0.65em;font-weight:400;color:#666;vertical-align:middle;margin-left:8px;">vX.Y</span></h1>
<p style="font-size:0.75rem;color:#3a3a55;font-family:'Cascadia Code','Consolas',monospace;margin-bottom:4px;">Built DD Mon YYYY  HH:MM TZ</p>
```

Use `date '+%-d %b %Y  %H:%M %Z'` in the terminal to get the correct local timestamp string to paste in.

---

## Step 4 — Create the Project Index Page

The `docs/index.html` is the main GitHub Pages page for the app. It shows:
- App name and description
- SharePoint setup checklist
- App.OnStart copy block
- Ordered screen cards (with links to the copy pages)

Use the app index template below to generate it. The user navigates to this page first, reads the setup steps, then clicks each screen card to copy the YAML.

---

## App Index HTML Template

Save as `docs/index.html` and replace all `APP_*` placeholders:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APP_FULL_NAME — PowerApps</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #0f0f1a;
      color: #e8e8f0;
      max-width: 900px;
      margin: 0 auto;
      padding: 40px 24px 80px;
    }
    h1 { font-size: 1.8rem; font-weight: 600; color: #c8b8ff; margin-bottom: 8px; }
    .subtitle { color: #888; font-size: 0.95rem; margin-bottom: 40px; }
    h2 { font-size: 1.2rem; color: #a0c0e0; margin: 40px 0 16px; border-bottom: 1px solid #2a2a3a; padding-bottom: 8px; }
    h3 { font-size: 1rem; color: #e8e8f0; margin: 24px 0 8px; }
    p { color: #aaa; line-height: 1.6; margin-bottom: 12px; }
    table { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin-bottom: 24px; }
    th { background: #1a1a2e; color: #c8b8ff; text-align: left; padding: 8px 12px; border: 1px solid #2a2a3a; }
    td { padding: 8px 12px; border: 1px solid #2a2a3a; color: #d0d0e0; vertical-align: top; }
    tr:nth-child(even) td { background: #131320; }
    .code-block { position: relative; margin: 12px 0 24px; }
    pre {
      background: #1a1a2e;
      color: #c8d8f0;
      padding: 16px;
      border-radius: 8px;
      font-family: 'Cascadia Code', 'Consolas', monospace;
      font-size: 0.82rem;
      line-height: 1.55;
      overflow-x: auto;
      white-space: pre;
    }
    .copy-btn {
      position: absolute;
      top: 8px;
      right: 8px;
      padding: 4px 12px;
      background: #7c4dff;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.78rem;
      transition: background 0.15s;
    }
    .copy-btn:hover { background: #6a3de8; }
    .copy-btn.ok { background: #2a7d4e; }
    .screen-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; margin-top: 16px; }
    .screen-card {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #1a1a2e;
      border: 1px solid #2a2a3a;
      border-radius: 12px;
      padding: 20px;
      text-decoration: none;
      color: inherit;
      transition: border-color 0.15s, background 0.15s;
    }
    .screen-card:hover { border-color: #7c4dff; background: #1e1e35; }
    .screen-number { font-size: 0.75rem; color: #666; margin-bottom: 8px; }
    .screen-name { font-size: 1rem; font-weight: 600; color: #c8b8ff; margin-bottom: 6px; }
    .screen-desc { font-size: 0.82rem; color: #888; line-height: 1.4; }
    .screen-cta { margin-top: 16px; font-size: 0.82rem; color: #7c4dff; }
    .note { background: #1a2a1a; border-left: 3px solid #2a7d4e; padding: 12px 16px; border-radius: 4px; font-size: 0.85rem; color: #aaa; margin: 16px 0; }
    .warning { background: #2a1a1a; border-left: 3px solid #7d2a2a; padding: 12px 16px; border-radius: 4px; font-size: 0.85rem; color: #aaa; margin: 16px 0; }
    ol { padding-left: 24px; color: #aaa; font-size: 0.9rem; line-height: 2; }
    a.back { font-size: 0.82rem; color: #666; text-decoration: none; display: inline-block; margin-bottom: 32px; }
    a.back:hover { color: #999; }
  </style>
</head>
<body>

<a class="back" href="https://phaderon.github.io/PowerApps/">← Guide Library</a>
<h1>APP_FULL_NAME</h1>
<p class="subtitle">APP_DESCRIPTION</p>

<h2>Before You Start</h2>
<ol>
  <li>Create the SharePoint lists below (all columns, exact names).</li>
  <li>Open Power Apps Studio → New blank canvas app.</li>
  <li>Add all data sources listed below (Data panel → Add data).</li>
  <li>Set App → OnStart using the code block below.</li>
  <li>Create one blank screen per screen in the list, then paste each YAML.</li>
</ol>

<h2>Data Connections</h2>
<p>Add these in the Data panel before pasting any YAML:</p>
APP_DATA_CONNECTIONS

<h2>SharePoint Lists</h2>
APP_SHAREPOINT_TABLES

<div class="warning">Mark every column <strong>Not Required</strong> in SharePoint. Required fields cause network errors — validation is handled in the app.</div>

<h2>App.OnStart</h2>
<p>Paste into <strong>App → OnStart</strong> in Power Apps Studio.</p>
<div class="code-block">
  <button class="copy-btn" onclick="copyBlock(this, 'on-start')">Copy</button>
  <pre id="on-start">APP_ON_START_FORMULA</pre>
</div>

<h2>Screens</h2>
<p>Paste each screen in order. Create a new blank screen first, then paste.</p>
<div class="screen-grid">
APP_SCREEN_CARDS
</div>

<h2>Issues</h2>
<p>Found a problem? <a href="https://github.com/PhadeDev/APP-SLUG/issues" style="color:#7c4dff">Report it here</a>.</p>

<script>
async function copyBlock(btn, id) {
  const text = document.getElementById(id).textContent;
  try {
    await navigator.clipboard.writeText(text);
    btn.textContent = '✓ Copied!';
    btn.className = 'copy-btn ok';
    setTimeout(() => { btn.textContent = 'Copy'; btn.className = 'copy-btn'; }, 3000);
  } catch (e) {
    btn.textContent = 'Failed';
  }
}
</script>
</body>
</html>
```

### Screen card HTML snippet (repeat per screen):

```html
<a class="screen-card" href="screens/scrXxx.html">
  <div>
    <div class="screen-number">Screen N</div>
    <div class="screen-name">scrXxx</div>
    <div class="screen-desc">What this screen does in one sentence.</div>
  </div>
  <div class="screen-cta">Open and copy →</div>
</a>
```

### SharePoint table HTML snippet (repeat per list):

```html
<h3>List: <code>XX ListName</code></h3>
<table>
  <thead><tr><th>Column name</th><th>Type</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>Title</td><td>Single line of text</td><td>Built-in — rename to meaningful label</td></tr>
    <tr><td>Status</td><td>Choice</td><td>Options: Active, Archived</td></tr>
  </tbody>
</table>
```

---

## Step 5 — Add Library Card

Add a card to the main PowerApps guide library at `/var/home/Phaderon/PowerApps/index.html`. Confirm with the user before doing this if the app is still in progress.

```html
<a class="guide-card" href="https://phadedev.github.io/APP-SLUG/">
  <div class="guide-top">
    <span class="guide-kicker">Canvas app</span>
    <h2>APP FULL NAME</h2>
    <p>SHORT_APP_DESCRIPTION</p>
  </div>
  <div>
    <div class="guide-meta">
      <span class="pill">N screens</span>
      <span class="pill">SharePoint</span>
      <span class="pill">YYYY-MM-DD</span>
    </div>
    <span class="open-row">Open app guide <span aria-hidden="true">→</span></span>
  </div>
</a>
```

---

## Step 6 — Commit and Push

```bash
cd /var/home/Phaderon/PowerApps-Apps/APP-SLUG
git add docs/
git commit -m "Add all screens and index page"
git push origin main
```

Wait ~60 seconds for GitHub Pages to build. Then verify the live URL.

---

## App Directory

All per-project repos are cloned or initialised at:

```
/var/home/Phaderon/PowerApps-Apps/
  APP-SLUG/
    docs/
      index.html
      screens/
        scrHome.html
        scrDetail.html
        ...
```

The `PowerApps-Apps/` directory is a sibling of `PowerApps/` (the guide library repo).

---

## Quick Reference

| What | Where |
|---|---|
| Guide library repo | `Phaderon/PowerApps` at `/var/home/Phaderon/PowerApps/` |
| Guide library Pages | `https://phaderon.github.io/PowerApps/` |
| New app repos | `PhadeDev/APP-SLUG` at `/var/home/Phaderon/PowerApps-Apps/APP-SLUG/` |
| New app Pages | `https://phadedev.github.io/APP-SLUG/` |
| Issues | `https://github.com/PhadeDev/APP-SLUG/issues` |
