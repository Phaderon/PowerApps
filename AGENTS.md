# PowerApps Guide Library Agent Instructions

Before creating or editing Power Apps guides in this repo, read:

- `reference/powerapps-bible.md`
- `reference/README.md`
- `reference/real-build-quirks.md`
- `reference/guide-authoring-rules.md`
- `reference/verified-control-reference.md`
- `reference/powerapps-control-defaults.md`
- `reference/known-bad-patterns.md`

Load these when relevant:

- Power Fx formulas: `reference/powerfx-patterns.md`
- SharePoint or Office365Users: `reference/sharepoint-office365users.md`
- New guide structure: `reference/future-guide-template.md`

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
