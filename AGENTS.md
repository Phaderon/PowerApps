# PowerApps Guide Library Agent Instructions

Before creating or editing Power Apps guides in this repo, read:

- `reference/powerapps-bible.md` — entry point and reading order
- `reference/real-build-quirks.md` — live editor confirmed quirks
- `reference/live-build-lessons.md` — lessons from Training Tracker GitHub issues (priority read for new apps)
- `reference/guide-authoring-rules.md`
- `reference/verified-control-reference.md`
- `reference/powerapps-control-defaults.md`
- `reference/known-bad-patterns.md`

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
- Pages: `https://phadedev.github.io/APP-SLUG/`
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
