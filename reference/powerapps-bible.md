# PowerApps Bible

Last checked: 2026-06-20

This is the entry point for the local Power Apps knowledge base.

## Layers

1. Microsoft source mirror under `.sources/`
   - `powerapps-docs`
   - `power-platform`
   - Not published to GitHub Pages.
   - Updated with `tools/update-msdocs.sh`.

2. Search index under `.cache/powerapps-bible.sqlite`
   - Built with `python3 tools/index-msdocs.py --rebuild`.
   - Queried with `python3 tools/index-msdocs.py "Combo box ItemDisplayText"`.

3. Curated local reference pack under `reference/`
   - Human-friendly rules.
   - Real build quirks from the Training Tracker app.
   - Corrections discovered while building future guides.

4. Audit tooling under `tools/`
   - Blocks known bad guide patterns before publishing.

## Non-Negotiable Accuracy Rule

Do not write guide instructions from memory when the property, connector field, or formula behavior is risky. Search the local Microsoft docs mirror and the curated reference pack first. If the answer is not present, verify with current Microsoft Learn or live Power Apps behavior, then add the result to the curated reference pack.

## Real Build Quirks To Preserve

- SharePoint list names with spaces must be wrapped in single quotes, for example `'TT Personnel'`.
- Sort order must use full enum names, for example `SortOrder.Ascending`, not bare `Ascending`.
- Modern Combo box hint text uses `InputTextPlaceholder`, not `Placeholder`.
- Modern Combo box display text must be explicit with `ItemDisplayText`.
- In the Training Tracker day-filtering formulas, preserve the exact working day-unit spelling from the live editor. If the app accepted `"Days"` and rejected bare `Days`, do not normalize it away.
- Modern Toggle state is handled with `Checked` in this guide family.
- Office365Users connector casing differs by operation. Preserve the exact field casing used by the verified operation.

## Common Searches

```bash
python3 tools/index-msdocs.py "Combo box ItemDisplayText"
python3 tools/index-msdocs.py "Text input Placeholder"
python3 tools/index-msdocs.py "SortOrder.Ascending"
python3 tools/index-msdocs.py "Office365Users SearchUserV2"
python3 tools/index-msdocs.py "DateDiff TimeUnit Days"
python3 tools/index-msdocs.py "Patch SharePoint choice Value"
```

## Start Here For Quirks

Read `real-build-quirks.md` before changing formulas or control rows in Training Tracker.
