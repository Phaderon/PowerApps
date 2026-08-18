# PowerApps Guide Library Agent Instructions — "The Power Apps Bible"

This repo is referred to as **the Power Apps Bible** in every project that uses it. If
a user or another session says "consult the Power Apps Bible," this repo is what they
mean.

## Hosting: Cloudflare Pages, NOT GitHub Pages (read this before touching any guide)

**As of 2026-08-15, every guide site in this app family is hosted on Cloudflare Pages,
not GitHub Pages.** GitHub Pages (the legacy Jekyll builder) had repeated build
failures on this repo — user's explicit words: "I am absolutely sick of GitHub... fuck
this GitHub bullshit." GitHub repos are still real (code, version history, issues) —
only static hosting moved. **When the user says "update the guide," it means: edit the
file, `git commit && git push` as usual, THEN deploy to the Cloudflare Pages project
below with `wrangler pages deploy` — both steps, every time, no exceptions.** Never
tell the user to check a `phaderon.github.io` or `phadedev.github.io` URL — those are
dead (Pages disabled on those repos on purpose). If you land in this repo and see a
stale reference to `github.io` anywhere below, that instruction is out of date; trust
this section instead and fix the stale reference while you're there.

| Site | Repo (unchanged) | Live URL (Cloudflare) | Deploy source dir |
|---|---|---|---|
| Guide library hub (this repo) | `Phaderon/PowerApps` | `https://powerapps.pages.dev/` | repo root |
| Policy Tracker fix guide | `Phaderon/PowerApps` (`policy-tracker/`) | `https://powerapps.pages.dev/policy-tracker/` | repo root (mirrored subfolder) |
| Policy Tracker screen YAML | `PhadeDev/policy-tracker` | `https://policy-tracker.pages.dev/` | `docs/` |
| Branch Contact Groups task guide | `Phaderon/PowerApps` (`branch-contact-groups/`) | `https://powerapps.pages.dev/branch-contact-groups/` | repo root (mirrored subfolder) |
| Branch Contact Groups screen YAML | `PhadeDev/branch-contact-groups` | `https://branch-contact-groups.pages.dev/` | `docs/` |
| Training Tracker (guide + all screens, one page) | `Phaderon/PowerApps` (`training-tracker/`) | `https://powerapps.pages.dev/training-tracker/` | repo root |
| Staff Movements (guide + all screens, one page) | `PhadeDev/staff-movements` | `https://staff-movements.pages.dev/` | `docs/` |
| Library & File Plan Manager | `PhadeDev/library-file-plan-manager` | `https://phadedev.github.io/library-file-plan-manager/` | **not yet migrated** — still real GitHub Pages, don't "fix" this one |

Deploy command (credentials already sourced from `~/.config/cloudflare/pages.env` via
`~/.bashrc`, no login needed):
```bash
source ~/.config/cloudflare/pages.env   # usually redundant, harmless
rm -rf <scratchpad>/cf-deploy-X && mkdir -p <scratchpad>/cf-deploy-X
cd <repo> && git archive HEAD -- <docs-subdir-if-any> | tar -x -C <scratchpad>/cf-deploy-X
cd <scratchpad>/cf-deploy-X[/docs]
npx wrangler pages deploy . --project-name=<powerapps|policy-tracker|branch-contact-groups> --branch=main --commit-dirty=true
```
Always deploy from a clean `git archive` export, never the raw working directory —
`.sources/`, `.cache/`, `.backups/`, `.wrangler/` are gitignored scratch content that
must never go live.

**MANDATORY, every code-card/code-block on any guide page, no exceptions, not even a
one-liner — added 2026-08-15, explicit standing rule for every agent (Claude, Codex,
whoever):** every code-card must carry a `data-updated="<ISO-8601 UTC timestamp>"`
attribute on its stamp element, a real `HH:MM <TZ>` in the human-readable display text
(not just a date), and the shared "auto-fading Updated pill" script must be present on
that page. User's own words: "every single time there's a code block made on this
site... that entire updated thing with the date and the time appears, every time. I
don't have to keep asking for it." Root cause this was raised over: three code-cards
got added without a time component, so when their content was silently fixed later
that same day there was no visible signal anything had changed — after GitHub Pages'
long history of "did this actually update," the user has zero tolerance left for that
ambiguity. **How to apply, every time you touch a code-card:**
1. Get the real current time: `date -u +%Y-%m-%dT%H:%M:%SZ` (UTC) and `date '+%Y-%m-%d %H:%M %Z'` (local display) — never guess or reuse an old timestamp.
2. New code-card: `<span class="code-stamp" data-updated="<ISO>">v1 &middot; <local date HH:MM TZ></span>`.
3. Editing an EXISTING code-card's content: bump the version number AND replace both the `data-updated` value and the display text with the real current time — never leave a stale stamp on changed content, that's the exact bug that triggered this rule.
4. The CSS (`.update-pill` + `.code-stamp` styling) and the pill-computing `<script>` block (scans `[data-updated]`, shows "Updated Xh ago" for 48h then auto-hides) must exist somewhere on the page — copy it from `policy-tracker/index.html` (Fix Guide template) or `PhadeDev/policy-tracker`'s `docs/screens/NewsletterPack.html` (Screen YAML / clipboard-copy template) if the page doesn't have it yet, don't reinvent it.
5. Applies to every guide family — Policy Tracker, Branch Contact Groups, Training Tracker, and any future app — both the Fix Guide code-card template and the Screen YAML clipboard-copy template. As of 2026-08-15 only Policy Tracker's two pages have been retrofitted with this on their EXISTING stamps; Branch Contact Groups and Training Tracker still need their old stamps converted — do that opportunistically the next time either is touched, don't wait to be asked.

**Policy Tracker fix guide has a live completion-tracking system** (added 2026-08-15,
`functions/api/fix-status.js` + a Cloudflare KV namespace bound to the `powerapps`
Pages project as `FIX_STATUS`). Each Fix section has a "Mark complete" checkbox;
checking it POSTs `{app, id, done}` to `/api/fix-status` and collapses that section.
**You can and should read this state directly instead of asking the user what's
already fixed:** `curl "https://powerapps.pages.dev/api/fix-status?app=policy-tracker"`
returns JSON of every completed fix's section `id`. **Retention rule (user's explicit
call, 2026-08-15): a fix marked complete for 30+ days should be deleted outright** —
remove its whole `<section>`, its sidebar `<nav>` link, and its KV entry — not just
left collapsed forever. The KV value is currently just `true`/absent; **before this
rule can actually fire, the Pages Function needs to store a completion timestamp
instead of a bare boolean** (check `functions/api/fix-status.js` — if it's still
storing `true`, update it to store an ISO date string, migrate any existing `true`
values to "today" once, and only then start actually deleting on future visits). Do
this check every time you're asked to touch the Policy Tracker guide, not just when
explicitly asked to clean up.

**Homepage has a password-gated multi-file upload box into R2** (added 2026-08-17,
`functions/api/upload.js` + `functions/api/upload/[key].js`, R2 bucket
`powerapps-uploads` bound to the `powerapps` Pages project as `UPLOADS`, password
stored as the Pages secret `UPLOAD_PASSWORD`, not in this repo). The user uses this to
hand files (screenshots, exports, zips) to whichever agent is working, from any device.
**Read what's there instead of asking the user to re-send:**
`curl "https://powerapps.pages.dev/api/upload?password=<UPLOAD_PASSWORD>"` lists
objects; fetch one with
`curl "https://powerapps.pages.dev/api/upload/<key>?password=<UPLOAD_PASSWORD>" -o <file>`.
Get the password value from the user directly if you don't already have it in this
session — never print it into a file, guide page, or committed code. **Storage
safeguards, all already in place, don't remove them:** an R2 bucket lifecycle rule
auto-deletes every object after 14 days (set via the Cloudflare API directly on the
bucket, not enforced in code); the upload Function also rejects any single file over
25MB and refuses new uploads once the bucket's total size is within ~2GB of the R2 free
tier's 10GB/month cap. If asked to raise these limits, remember the point of the caps is
to make this feature unable to blow through the free tier unattended — don't just delete
them, ask first if a genuinely bigger file needs to go through.

**Always start here:** `reference/database.html` — every reference document in this
repo consolidated onto one page, in reading order (known-bad-patterns first, since
that's the highest-signal "here's exactly what broke and how to fix it" content).
Live at `https://powerapps.pages.dev/reference/database.html`. Fetch that one
URL/file first for any Power Apps question — it replaces needing to guess which of the
individual files below to check.

The individual files remain the editable sources (edit these, then re-run
`python3 tools/build-database.py` to republish `reference/database.html`):

- `reference/known-bad-patterns.md` — confirmed-wrong properties/formulas/patterns, the single highest-value file
- `reference/powerapps-bible.md` — entry point and reading order
- `reference/verified-control-reference.md` — exact property lists per control, verified
- `reference/powerapps-control-defaults.md` — lab-derived fresh-control defaults
- `reference/real-build-quirks.md` — live editor confirmed quirks
- `reference/live-build-lessons.md` — lessons from Training Tracker GitHub issues (priority read for new apps)
- `reference/guide-authoring-rules.md`
- `reference/external/` — separately-produced (ChatGPT) research: broader property-name coverage, NOT independently runtime-verified. See `reference/external-research-notes.md` for the precedence rule — this project's own `known-bad-patterns.md`/`live-build-lessons.md` always win on conflict.
- `docs/CONTROL_VERIFICATION_CHECKLIST.md` in the relevant per-project repo (e.g. `PhadeDev/policy-tracker`) — the ground-truth "look at it, poke it" verification checklist, scoped to controls that project actually uses or might use, as opposed to Microsoft's entire catalogue

Load these when relevant:

- Building a new app from scratch: `reference/builder-system.md` — requirements gathering, naming conventions, YAML rules, Patch templates, publishing
- Delivering output to the user: `reference/output-format.md` — exact delivery order, App.OnStart separation rule, GitHub Pages format
- Validating YAML before output: `reference/yaml-validation-checklist.md` — complete checklist, run before every YAML delivery
- Creating a new per-project repo: `reference/project-repo-workflow.md` — GitHub repo setup, Pages template, library card
- Reusable UI patterns: `reference/ui-patterns.md` — panels, tab nav, error borders, pill galleries, status colours
- Power Fx formulas: `reference/powerfx-patterns.md`
- SharePoint or Office365Users: `reference/sharepoint-office365users.md`
- New guide structure: `reference/future-guide-template.md`

## Building a New App — Mandatory Process

When asked to build a new Power Apps app:

1. **Phase 0:** Ask only business/workflow questions. Never ask about list/column names.
2. **Phase 1:** Design all SharePoint lists. Output a complete setup checklist.
3. **Phase 2–4:** Name all variables, collections, and screens. Write App.OnStart.
4. **Run the YAML validation checklist** (`reference/yaml-validation-checklist.md`) against the plan before writing a single line of YAML.
5. **Create the per-project GitHub repo** (`reference/project-repo-workflow.md`).
6. **Generate screen YAML** — audit every control against `reference/verified-control-reference.md`. PA2108 traps: `Size` on `Toggle@1.1.5`, `FontWeight` on `ModernButton@1.0.0`.
7. **Deliver output** in the format specified in `reference/output-format.md`:
   - SharePoint setup (tables)
   - Data connections list
   - App.OnStart as a **separate code block** — NEVER inside screen YAML
   - GitHub Pages URL for screen copy pages
   - Issues tracker URL

## Screen YAML Generation Rules

- 2-space indent, CRLF line endings (pa-yaml-wrap enforces CRLF), all formula values prefixed with `=`
- Multi-line formulas (colons in values, multi-statement) use `|-` block scalar
- Z-order: controls listed LATER in Children appear IN FRONT
- Background panels listed FIRST; error borders listed IMMEDIATELY BEFORE the field they highlight; overlays listed LAST
- Never embed App.OnStart formulas in screen YAML
- Run full validation checklist before wrapping and pushing

## Wrapping Screen YAML

```bash
pa-yaml-wrap /tmp/ScreenName.yaml /var/home/Phaderon/PowerApps-Apps/app-slug/docs/screens/ScreenName.html
```

Per-project repos live at: `/var/home/Phaderon/PowerApps-Apps/APP-SLUG/`
Guide library repo: `/var/home/Phaderon/PowerApps/`

## Per-Project Repo URLs

- Repo: `https://github.com/PhadeDev/APP-SLUG`
- Pages (Cloudflare, NOT GitHub Pages — see Hosting section above): `https://APP-SLUG.pages.dev/`
- Issues: `https://github.com/PhadeDev/APP-SLUG/issues`

---

Accuracy rule: do not invent Power Apps properties, connector fields, formula behavior, or default values. Use the local reference pack, current Microsoft Learn pages, lab-derived fresh-control defaults, or confirmed live-editor behavior supplied by the user. If a fact is newly verified, add it to the reference pack before using it as a final guide instruction.

When accuracy matters, search the local Microsoft docs mirror first:

```bash
tools/update-msdocs.sh
python3 tools/index-msdocs.py --rebuild
python3 tools/index-msdocs.py "Combo box ItemDisplayText"
```

The mirror is stored in `.sources/` and is not published to GitHub Pages.

Before publishing guide edits, run:

```bash
python3 tools/audit-guide.py training-tracker/index.html
git diff --check
```

For a future guide, replace `training-tracker/index.html` with that guide's path.
