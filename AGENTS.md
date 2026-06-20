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

## Screen YAML Generation

When asked to generate a complete PowerApps screen as importable YAML:

1. **Read the guide first.** Load the relevant Phase section from `training-tracker/index.html` for every control's properties and formulas. Never invent values.
2. **Read `reference/verified-control-reference.md`** for the exact property list of every modern control (`ModernButton@1.0.0`, `ModernTextInput@1.1.0`, `ModernDropdown@1.0.1`, `ModernCombobox@1.1.0`, `Toggle@1.1.5`).
3. **Write the YAML file** to `~/Downloads/ScreenName.yaml`:
   - 2-space indent, CRLF line endings, all formula values prefixed with `=`
   - Multi-line formulas (colons in values, multi-statement) use `|-` block scalar
   - Flat control list (no GroupContainer) unless explicitly requested
   - Tab visibility via `Visible: =varTab = "TabName"` on individual controls
   - Controls appearing ON TOP of others must appear LATER in `Children:` (z-order = list order)
4. **Audit before wrapping** — verify every property on every modern control against `reference/verified-control-reference.md`. Known PA2108 traps: `Size` on `Toggle@1.1.5`, `FontWeight` on `ModernButton@1.0.0`.
5. **Wrap and push:**
   ```bash
   pa-yaml-wrap ~/Downloads/ScreenName.yaml /var/home/Phaderon/PowerApps/screens/ScreenName.html
   cd /var/home/Phaderon/PowerApps
   git add screens/ScreenName.html
   git commit -m "Add ScreenName YAML"
   git push origin main
   ```
6. **Add a card** to `index.html` (copy the scrAdminManage card pattern).
7. Report the live URL: `https://phaderon.github.io/PowerApps/screens/ScreenName.html`

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
