# Power Apps Reference Pack

Last checked: 2026-06-20

Purpose: reusable, source-linked guidance for building future Power Apps guide pages with the same visual standard as the Training Tracker guide, without guessing control properties or formula patterns.

This is not a copied mirror of Microsoft Learn. It is a practical local reference pack built from:

- Microsoft Learn source pages linked in each reference file.
- Real corrections found while building the Training Tracker guide.
- Local audit rules in `../tools/audit-guide.py`.

## Files

- `powerapps-bible.md` - entry point for the local Microsoft docs mirror, search index, curated quirks, and audit workflow.
- `real-build-quirks.md` - live Power Apps editor fixes discovered while building Training Tracker.
- `verified-control-reference.md` - modern/classic controls currently used by the guide style.
- `powerfx-patterns.md` - formula patterns, source links, and traps.
- `sharepoint-office365users.md` - SharePoint field-shape and Office365Users connector notes.
- `guide-authoring-rules.md` - required workflow for future guide creation.
- `future-guide-template.md` - guide structure and landing-page card pattern.
- `known-bad-patterns.md` - recurring mistakes to block before publishing.

## Rule

If a future guide needs a control, connector, or formula pattern that is not in this pack, verify it from Microsoft Learn or live Power Apps behavior first. Add the result here before using it in the guide.

## Local Microsoft Docs Mirror

Use:

```bash
tools/update-msdocs.sh
python3 tools/index-msdocs.py --rebuild
python3 tools/index-msdocs.py "Combo box ItemDisplayText"
```

The mirror lives in `.sources/` and the SQLite index lives in `.cache/`; both are intentionally gitignored and not published.
