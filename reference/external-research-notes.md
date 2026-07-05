# External Research: ChatGPT Control Property Matrix (2026-07-05)

Three files landed in `reference/external/` from a separate ChatGPT research pass:
`powerapps_canvas_control_bible_v0_1.md` (curated summary, ~870 lines),
`powerapps_canvas_control_property_matrix_v0_1.csv` (raw property matrix, 412 rows),
and `powerapps_canvas_control_bible_schema_v0_1.json` (the CSV's column schema).

## What this is good for

Much broader **property-name coverage** than this Bible had compiled by hand — 412
property rows across every Modern and Classic control Microsoft documents, including
controls this project hasn't touched yet (e.g. it flagged a **`Rating`** modern control
that was missing from `CONTROL_VERIFICATION_CHECKLIST.md` in the Policy Tracker repo —
added there now). Use it as a **property-name dictionary**: if you're not sure whether
a property exists on a control, check here first before guessing.

## What this is NOT

It is honest about its own limits (its own intro says exactly this): it's derived from
Microsoft's documentation pages, the same source class that has been **wrong or
incomplete multiple times** in this project's actual live builds — `ModernDatePicker.
SelectedDate` not being settable, `ModernCombobox.Reset()` clearing the selection
instead of restoring it, `Required` not suppressing the clear-X on `ModernDropdown`,
`GroupContainer.DropShadow` defaulting on. None of those specific facts would have
been caught by more thorough documentation scraping, because the documentation itself
doesn't mention them — they were only found by touching the real, running control.

Its own confidence levels reflect this: of the 412 rows, ~171 are "High" (from an
individual control's docs page), ~180 are "Medium" (inferred/shared, not verified per
control), and the rest are "Gap flagged" (property list not even fully harvested yet).
None are independently runtime-verified.

## Precedence rule

**When this external research conflicts with `known-bad-patterns.md` or
`live-build-lessons.md`, this project's own empirically-confirmed entries win, every
time.** This matrix is a starting point for coverage on controls we haven't verified
yet, not a correction to anything we've already confirmed the hard way.

## Two genuinely useful pointers surfaced by this research (not yet followed up)

- [`microsoft/power-platform-skills` issue 101](https://github.com/microsoft/power-platform-skills/issues/101) —
  hidden/generated properties (e.g. `SearchItems` on searchable controls) that don't
  show up via `describe_control`/standard tooling. Worth checking if a control ever
  seems to have an internal property we can't find documented anywhere.
- [`microsoft/power-platform-skills` issue 146](https://github.com/microsoft/power-platform-skills/issues/146) —
  `PowerBIIntegration`, a runtime-injected host object, not a normal insertable
  control — can surprise an offline schema/compiler if ever encountered.

Full raw files: [`bible.md`](external/powerapps_canvas_control_bible_v0_1.md) ·
[`property matrix (CSV)`](external/powerapps_canvas_control_property_matrix_v0_1.csv) ·
[`schema (JSON)`](external/powerapps_canvas_control_bible_schema_v0_1.json)
