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
6. Check `powerapps-control-defaults.md` before listing default visual properties.
7. For formulas, use `powerfx-patterns.md` and source-linked Microsoft Learn pages.
8. Add any new verified fact to this reference pack.
9. Run `python3 tools/audit-guide.py path/to/index.html`.
9a. Run `python3 tools/audit-formulas.py path/to/index.html [any local src/formulas/*.md files]` — checks the actual Power Fx content (not just guide prose/YAML) for patterns already confirmed broken live in this Bible: `Base64()`, `AddColumns`/`GroupBy` quoted column names, `Table`-typed UDF parameters, a UDF definition mixed with imperative statements (OnStart/OnSelect vs. the separate `Formulas` property), unescaped `&` inside generated markup strings, and unbalanced brackets. If the project keeps local formula source files separate from the published guide, also run it with `--diff <local.md> <guide.html>` to catch drift between what was actually tested and what's actually published — added 2026-09-11 after exactly that drift was found live (a `Base64()` fix landed in a guide but never made it back into the local source file).
10. Run `git diff --check`.
11. Preview locally and test responsive layout and copy buttons.
12. **Adding a new `<section id="...">` to any guide? Add its matching link to that
    page's sidebar `<nav>` in the same edit, not as an afterthought.** Verify with a
    script, not by eye — `<section id>` values and `<nav><a href="#...">` targets must
    match exactly, same count, same set. Added 2026-09-11 after this was missed twice
    in a row on the same guide (Cadets Org Chart's "Clear All Pictures" and "Phase 4"
    sections were both only reachable by scrolling, with no sidebar link at all) —
    the builder relies on that sidebar to navigate a growing page and a silently
    unlisted section defeats the entire point of having one.

## Defaults Standard

Future guides should separate required changes from defaults.

Rules:

- Put non-default or behavior-critical properties in the main "Key properties" list.
- Do not make the builder hunt for default values unless the property is safety-critical.
- If a default value is listed for reassurance, label it as `leave default` or `default/safety check`.
- Use Microsoft Learn defaults where documented, but do not invent defaults when the docs do not state them.
- Use `powerapps-control-defaults.md` for observed fresh-control defaults from the user's editor. Treat omitted properties as "not serialized on fresh insert", not as proof of a literal value.
- Do not list `Fill=RGBA(0,0,0,0)` for normal Label controls unless it is marked `leave default` or `default/safety check`.
- Do not list `BorderThickness=0` for normal Label controls unless it is marked `leave default` or `default/safety check`.
- Do not list `SelectMultiple=true` for modern Combo box controls unless it is marked `leave default` or `default/safety check`; set `SelectMultiple=false` explicitly for single-select Combo boxes.
- Do not list `ItemDisplayText=ThisItem.Value` for modern Combo box controls using simple value tables unless it is marked `leave default` or `default/safety check`; set `ItemDisplayText` explicitly when the row shape needs another field.
- Classic visual workarounds may still list apparent defaults when they prevent common mistakes, for example keeping `HoverFill` and `PressedFill` locked to `Fill` on classic Button panel backgrounds.
- For future app guides, prefer a two-column wording: `Set these` and `Leave/default check`.

## Inline Formula Standard

When a control row needs an `OnSelect`, `Items`, `OnChange`, or similar formula, place a collapsed copyable formula block directly beside or immediately below that control's properties. A separate formula section may remain for scanning, but the builder should not have to scroll away from the control row to copy the formula.

## Row Tracking Standard

Interactive guide tables should mark the row currently being worked on when the builder clicks a copyable pill or formula copy button. The active row should be clearly highlighted, previously copied rows should be visually muted, and each marked row should include a small clear button for accidental clicks.

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

## Accumulating Properties Standard

Added 2026-09-11, Cadets Org Chart project, after the user explicitly asked to never
have to work out what to add vs. what to keep for a growing `App.OnStart`.

If a guide's build process adds to the same property across multiple stages/phases
(most commonly `App.OnStart`, but this applies to any control property that keeps
growing rather than being replaced each time — e.g. a toggle button's `OnSelect` that
needs to know about more things to refresh as more screens are added) — maintain one
"Current State" section near the top of the guide with the complete, current content
of that property, and republish it in full every time anything changes. Never make the
reader diff a per-stage snippet against what they already pasted.

Present it collapsed by default (native `<details>`/`<summary>`, no JS needed) with a
`code-card`/copy button inside, so it doesn't dominate the page for a reader who
doesn't need it right now — see `cadets-org-chart/index.html`'s `#current-state`
section for a working example, including the accordion CSS.

Per-phase/per-stage sections remain useful as the record of *why* each piece exists;
they are not a substitute for the one always-complete reference.

## Guide Weight Standard

Added 2026-09-11, Cadets Org Chart project, after a still-active phase (not yet
markable "complete", so the existing per-phase collapse/checkbox mechanism doesn't
apply) accumulated three rounds of fix history and one very large unchanged code
block, and the builder asked "where is the new code for this" rather than scroll past
all of it again.

When a phase gets a second (or third...) round of fixes before it's ever marked
complete:

- Add one short, always-visible callout right after that phase's `fix-controls` block
  stating plainly what changed THIS round, where the corrected data/formula actually
  lives (usually the Current State box), and whether any large code block below is
  still unchanged and therefore doesn't need re-copying.
- Wrap the accumulating "why this changed" history callouts in a `cs-accordion`
  `<details>`, collapsed by default — they're a record of why, not something to read
  every visit.
- Wrap any large code block that did NOT change this round in its own collapsed
  `cs-accordion` `<details>` too, with a one-line note above it saying so — don't make
  the builder scroll past hundreds of unchanged lines to find what's new.
- Never hide the actual current instructions/data itself this way — only the
  historical narrative and unchanged bulk content. The one thing that must always stay
  immediately visible (not inside a collapsed accordion) is the "what changed this
  round + where to get it" callout itself.

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
