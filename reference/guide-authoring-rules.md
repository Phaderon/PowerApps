# Guide Authoring Rules

Last checked: 2026-06-20

Use this file before creating or changing any future Power Apps guide in this repo.

## Accuracy Standard

No guessed Power Apps properties. No plausible formulas unless verified. Every risky instruction must come from one of:

- Microsoft Learn current documentation.
- This local reference pack.
- Confirmed behavior in the live Power Apps editor, then recorded in this reference pack.

If something is uncertain, mark it as unverified and do not publish it as a build instruction.

## Required Workflow

1. Define the app purpose, users, data sources, roles, and screens.
2. Create or update SharePoint schema notes before writing formulas.
3. Choose controls from `verified-control-reference.md`.
4. For every control table row, include exact control type: modern or classic.
5. For every property in a row, verify that the property belongs to that control family.
6. For formulas, use `powerfx-patterns.md` and source-linked Microsoft Learn pages.
7. Add any new verified fact to this reference pack.
8. Run `python3 tools/audit-guide.py path/to/index.html`.
9. Run `git diff --check`.
10. Preview locally and test responsive layout and copy buttons.

## GitHub Pages Layout

The root `index.html` is a guide library menu. Each guide lives in its own child folder with an `index.html`.

Pattern:

```text
PowerApps/
  index.html
  training-tracker/index.html
  future-app-name/index.html
  reference/index.html
  reference/*.md
  tools/audit-guide.py
```

Every child guide should include a visible link back to `../`.

## Visual Standard

Reuse the Training Tracker guide style unless there is a clear reason not to:

- Standalone HTML.
- No external scripts, fonts, tracking, or build tools.
- Searchable content.
- Code blocks with copy and wrap controls.
- Inline code chips that copy on click.
- Control names in property tables copy on click.
- Responsive split-screen behavior with no page-level horizontal overflow.
- Critical technical notes near the bottom for hard-won build quirks.

## Layer Order Standard

When a control is a visual background, card, panel, row fill, indentation strip, or progress-bar background, the guide must say so before the user builds on top of it.

Rules:

- Put the background control first in the table for that panel/template.
- Add a highlighted layer note before the table when order matters.
- Use "Recommended build order" wording when table order could make the builder leave a background on top of visible controls.
- State what must sit on top of it.
- For progress bars, explicitly say the background bar sits behind the fill bar.
- If a future guide has a tree/grouping section, include the background control in the group list but make clear it must be sent behind the visible controls.

## Temporary Error Standard

If a formula might red-line because a referenced control, collection, variable, flow, or data source is created later in the same phase, add a note directly before that formula.

The note must say:

- what may red-line,
- what missing thing causes it,
- when to recheck it,
- and when to treat it as a real error.

## Grouping Standard

Use groups for meaningful sections, especially tab bodies and repeated screen sections. Do not over-group during initial build instructions.

When recommending a group:

- say why the group exists,
- list exactly which controls go into it,
- state any controls that must not be included,
- keep layer-order warnings visible,
- and mention if grouping should happen after visible controls are working.

## Landing Page Rule

When adding a new guide, add exactly one new card to root `index.html`:

- Card title should be the app/guide name.
- Card description should state app purpose and data sources.
- Pills should include platform, data source, and guide status.
- Link should point to the child folder, e.g. `new-guide/`.
