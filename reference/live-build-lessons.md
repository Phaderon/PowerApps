# Live Build Lessons

Last checked: 2026-06-23

These are lessons learned from the Training Tracker live build — real bugs hit and diagnosed in the Power Apps editor and via GitHub issue threads. They supplement `real-build-quirks.md`. Do not overrule them based on what seems logical; they are ground truth.

---

## Character Escapes Don't Work in Power Apps Strings

Power Apps formula strings do not support `\x` or `\u` escape sequences. Writing `\xB7` outputs the literal characters `\`, `x`, `B`, `7` — not the middle dot `·`.

Use `Char(decimal)` instead:

```powerfx
Char(183)
```

This produces `·` (U+00B7, middle dot / interpunct). This is the correct approach for any Unicode character by decimal code point.

Common ones used in Training Tracker:

| Character | Char() |
|---|---|
| · (interpunct) | `Char(183)` |

Never write `\xB7`, `·`, or any escape sequence in a Power Apps string literal.

---

## Version Stamps Are Mandatory on Every Screen Page and Index

Every `pa-yaml-wrap` call and every `docs/index.html` must carry a version label and a build timestamp. Without them, the user cannot tell whether GitHub Pages has served the latest push — F5 refreshes look identical.

**For screen pages**, always pass `--version`:
```bash
pa-yaml-wrap scrHome.yaml docs/screens/scrHome.html --version v1.2
```
The stamp appears bottom-right in small monospace text: `v1.2  —  Built 23 Jun 2026  10:55 BST`

**For `docs/index.html`**, add the version inline after the `<h1>` title and a build timestamp line below it. Use `date '+%-d %b %Y  %H:%M %Z'` to get the local time string.

**Version convention:** start at `v1.0`, bump minor for each fix/push (`v1.1`, `v1.2`), bump major for structural changes. Every push that modifies screen content increments the version so the stamp visibly changes.

---

## PA1001 — Three Rules for `|-` Block Scalars (All Must Hold)

All three errors share the code `PA1001 YamlInvalidSyntax`. They are distinct causes and must be checked independently.

---

### Rule 1 — Any multi-line formula must use `|-`, never inline

**Error message:** `While parsing a block mapping, did not find expected key.`

YAML cannot span an unquoted scalar value across multiple lines in a block mapping. If a formula opens a parenthesis on the key line without closing it, the next line is parsed as a new key — which fails.

**Wrong:**
```yaml
Fill: =If(
    ThisItem.Complete,
    RGBA(34,139,34,1),
    RGBA(163,100,0,1)
)
```

**Correct:**
```yaml
Fill: |-
  =If(
      ThisItem.Complete,
      RGBA(34,139,34,1),
      RGBA(163,100,0,1)
  )
```

**Pre-output scan:** For every `Key: =` line, count `(` and `)` on that line. If open count > closed count, the formula continues onto the next line — it must use `|-`. Applies to every property: `Fill`, `Color`, `DisabledFill`, `HoverFill`, `Text`, `Visible`, `OnSelect`, and all others.

---

### Rule 2 — Every `|-` block's first content line must start with `=`

**Error message:** `Power Fx expressions must start with '='`

The `=` prefix marks the value as a Power Fx formula. It is required on the **first content line only** — continuation lines do not get it. This applies to every property that uses `|-` without exception: event handlers (`OnSelect`, `OnChange`, `OnVisible`, `OnCheck`, `OnUncheck`) and data properties (`Items`, `Fill`, `Color`, `Visible`, `Text`, etc.).

**Wrong:**
```yaml
OnSelect: |-
  Patch('MyList', varRecord, {Field: Today()});
  Navigate(scrRecord)
```

**Correct:**
```yaml
OnSelect: |-
  =Patch('MyList', varRecord, {Field: Today()});
  Navigate(scrRecord)
```

**Pre-output scan:** For every `|-` in the YAML, check that the immediately following non-empty line starts with `=`.

---

### Rule 3 — Inside a `|-` block, indentation must follow paren depth

**Error message:** `While parsing a block mapping, did not find expected key.` (same as Rule 1, different cause)

When a `|-` block contains a nested formula like `If(condition, If(...))`, each line's indentation must match its logical paren depth. A common mistake when converting inline formulas to `|-` is to carry over original whitespace mechanically — this places the outer closing `)` at the wrong indent level, making the YAML parser see it as a key instead of formula continuation.

**Wrong (outer `)` at wrong indent — both `)` at the same level):**
```yaml
Fill: |-
  =If(
      ThisItem.Complete,
      RGBA(34,139,34,1),
      If(
          condition,
          RGBA(163,100,0,1),
          RGBA(0,78,66,1)
      )
      )
```

**Correct (outer `)` at the same indent as `=If(`):**
```yaml
Fill: |-
  =If(
      ThisItem.Complete,
      RGBA(34,139,34,1),
      If(
          condition,
          RGBA(163,100,0,1),
          RGBA(0,78,66,1)
      )
  )
```

**Rule:** The closing `)` of the outermost function must be at the **same indent as `=If(`** — that is, content indent (key indent + 2). Each nested level adds 4 spaces. Use paren depth to derive correct indentation, not the original source whitespace.

**Depth formula:**
- Content base = key indent + 2 spaces
- Each `(` that doesn't close on the same line increases depth by 1 → add 4 spaces per depth level
- Each unmatched `)` decreases depth before placing the line

---

## IsOdd Does Not Exist

`IsOdd()` is not a Power Apps function. It causes a formula error.

Use `Mod()` instead:

```powerfx
Mod(value, 2) = 1
```

Full alternating row colour pattern:

```powerfx
If(Mod(ThisItem.ID, 2) = 0, RGBA(255,255,255,1), RGBA(247,249,252,1))
```

---

## ThisItem.ItemIndex Is Unreliable for Alternating Row Colours

`ItemIndex` reflects the visual position in the gallery at render time. It shifts when the gallery filters or sorts, causing rows to flash between colours or flip incorrectly.

Use a stable identifier instead.

**SharePoint-backed gallery** (items from `'TT Personnel'`, `'TT Courses'`, etc.):
```powerfx
If(Mod(ThisItem.ID, 2) = 0, RGBA(255,255,255,1), RGBA(247,249,252,1))
```

**Collection-backed gallery with a numeric course ID** (e.g. `galMyTraining` bound to `colMyTraining`):
```powerfx
If(Mod(ThisItem.CourseID, 2) = 0, RGBA(255,255,255,1), RGBA(247,249,252,1))
```

**Collection-backed gallery with no numeric ID** (e.g. `galMyChain` keyed by email):
```powerfx
If(Mod(Len(ThisItem.Email), 2) = 0, RGBA(255,255,255,1), RGBA(247,249,252,1))
```

Never use `ThisItem.ItemIndex` in production alternating row formulas.

---

## ModernButton BasePaletteColor — Don't Fight It

`BasePaletteColor` on a `ModernButton` is a Fluent 2 seed colour — the framework derives fill, text, and hover colours from it internally. You do not control the exact output shade; Fluent 2 does.

**The correct approach: pick one dark, saturated seed per button role and leave it alone.** Don't try to match a specific brand hex precisely, don't set it conditionally, don't add a `Color` override to compensate. Work with Fluent 2, not against it.

**Rule: `BasePaletteColor` must be a dark, saturated colour.** If you can imagine reading white text on it, it will probably work. If it's a pastel or near-white, Fluent 2 treats it as a low-contrast accent and overrides it with a dark fill regardless.

Standard roles for new apps (using army dark green as primary):
- Primary action: `RGBA(0,78,66,1)` — app primary colour
- Secondary / cancel: `RGBA(120,120,120,1)` — neutral dark grey
- Destructive: `RGBA(163,45,45,1)` — dark red

Confirmed broken — all render wrong regardless of what you set:
- Any near-white or pastel (`RGBA(244,246,248,1)`, `RGBA(230,241,251,1)`, `RGBA(255,240,240,1)`, etc.)
- Conditional expressions like `If(varTab="X", RGBA(34,139,80,1), RGBA(228,236,248,1))` — the light inactive state will always render dark

**If you need conditional colour states** (active/inactive tab buttons, toggle-style buttons), don't use ModernButton. Use Classic Button with `Fill`, `HoverFill`, and `PressedFill` set directly. See `ui-patterns.md` — Tab Navigation Bar.

---

## Tab Navigation Buttons Must Be Classic Buttons

ModernButton `BasePaletteColor` does not support conditional light/dark fills for active/inactive tab states. Attempting to set `BasePaletteColor` conditionally based on a tab variable will not produce distinct active/inactive visual states when light colours are involved.

Use Classic buttons for tab navigation. Classic buttons expose `Fill`, `HoverFill`, and `PressedFill` directly, giving full colour control.

Standard tab button pattern (two tabs: "People" and "Courses"):

**`btnTabPeople`** — Classic/Button:
```powerfx
Fill         = If(varTab="People", RGBA(34,139,80,1), RGBA(255,255,255,1))
Color        = If(varTab="People", RGBA(255,255,255,1), RGBA(24,95,165,1))
HoverFill    = If(varTab="People", RGBA(28,115,65,1), RGBA(235,241,250,1))
PressedFill  = If(varTab="People", RGBA(22,95,55,1), RGBA(210,225,245,1))
BorderColor  = RGBA(24,95,165,1)
BorderThickness = 1
RadiusTopLeft = RadiusTopRight = RadiusBottomLeft = RadiusBottomRight = 8
OnSelect     = Set(varTab, "People")
```

Same pattern for `btnTabCourses` with `varTab="Courses"`.

---

## SortByColumns Fails on SharePoint Choice Fields

`SortByColumns(source, "FieldName", SortOrder.Ascending)` breaks when the field is a SharePoint Choice type. SharePoint returns Choice fields as records `{Value: "..."}`, not plain strings. `SortByColumns` cannot sort on a record expression.

Use `Sort()` with `.Value` to unwrap the Choice record:

```powerfx
Sort(source, Status.Value, SortOrder.Ascending)
```

For double-sort (status then title):
```powerfx
Sort(
    Sort(source, Title, SortOrder.Ascending),
    Status.Value, SortOrder.Ascending
)
```

Do not use `SortByColumns` on a column that is a SharePoint Choice field.

---

## Multi-Select Choice Field: `in` Operator Fails Silently

The `in` operator checks for a full record match. A SharePoint multi-select Choice field returns a table of records `{Value: "..."}`. Writing `"Army" in ApplicableTo` checks whether the string "Army" matches an entire record — it never will, so it always returns false silently.

Use `CountIf` to check if any value in the table matches:

```powerfx
CountIf(ApplicableTo, Value = drpFilter.Selected.Value) > 0
```

This correctly counts how many rows in the multi-select field have the matching value string.

Example in a Filter:
```powerfx
Filter(colCourses,
    (IsBlank(drpPeopleType.Selected.Value) ||
     drpPeopleType.Selected.Value = "All types" ||
     CountIf(ApplicableTo, Value = drpPeopleType.Selected.Value) > 0)
)
```

---

## Launch() Reuses the Current Browser Tab

`Launch(url)` navigates the current tab away from the Power Apps app. Users lose their place.

Always use `LaunchTarget.New` as the third argument to open in a new tab:

```powerfx
Launch(varCourse.CourseURL, {}, LaunchTarget.New)
```

The second argument `{}` is a required empty record placeholder.

Never write `Launch(url)` alone for any URL that should leave the app running in the background.

---

## Classic Dropdown Always Has a Selection

A Classic Dropdown (not ModernDropdown) always selects the first item on load. Its `.Selected` value is never blank. There is no way to make it empty.

Do not add required-field validation for Classic Dropdown controls — `IsBlank(drpControl.Selected.Value)` will always be false and the validation will never trigger.

If required validation on a dropdown is needed, use ModernDropdown with a placeholder, or add a deliberate "Select..." first item and validate against that string.

---

## Collection IDs Are Text; SharePoint IDs Are Numeric

When a collection is built with `ForAll` and stores SharePoint IDs as `CourseID: C.ID`, the value may be stored as text depending on how the formula evaluated. SharePoint `TT Courses.ID` is a numeric Integer field.

A `LookUp('TT Courses', ID = ThisItem.CourseID)` may silently return blank if the types don't match.

Wrap the collection ID with `Value()` to force numeric comparison:

```powerfx
LookUp('TT Courses', ID = Value(varCourse.CourseID))
```

Use this whenever looking up a SharePoint record by an ID that was previously stored in a collection.

---

## varCourse vs varFullCourse — Two-Variable Pattern for Detail Screens

When a gallery row sets `varCourse` to `ThisItem` (the collection row), and the detail screen needs SharePoint-only fields not included in the collection's `ForAll` projection, those fields will be blank on the detail screen.

**The clean pattern:** keep `varCourse` as the gallery row (for training status, expiry, dates), and look up SP-only fields directly on the detail screen:

```powerfx
LookUp('TT Courses', ID = Value(varCourse.CourseID), CourseHost.Value)
LookUp('TT Courses', ID = Value(varCourse.CourseID), CourseDescription)
LookUp('TT Courses', ID = Value(varCourse.CourseID), CourseURL)
```

For multi-value fields like `ApplicableTo`:
```powerfx
With(
    {courseRow: LookUp('TT Courses', ID = Value(varCourse.CourseID))},
    "Applies to: " & Concat(courseRow.ApplicableTo, Value, ", ")
)
```

**Avoid** putting all fields into `varCourse` by attempting a merged record in `OnSelect` — the schema mismatch between the collection row and the SharePoint record causes `CanEdit` and other collection-only fields to be unrecognized.

**Avoid** keeping a `varFullCourse` variable set in `OnSelect` and then using it with fallbacks on the detail screen — that pattern quickly accumulates fallback formula debt when fields aren't available in both sources.

---

## Collection Projections Must Include Every Field a Downstream Screen Reads

If `scrCourseDetail` reads `varCourse.CourseURL`, `varCourse.CourseHost`, `varCourse.CourseDescription`, and `varCourse.ApplicableTo`, those fields must be either:

1. Included in the `colMyTraining` ForAll projection, or
2. Looked up directly on the detail screen from the SharePoint source.

If you pick option 1, add all of them explicitly. If you add a new field to SharePoint later, you must also add it to the `ForAll` projection or it will be blank on the detail screen.

If you pick option 2, use the `LookUp('TT Courses', ID = Value(varCourse.CourseID), FieldName)` pattern described above.

Never assume a field is in `varCourse` because it exists in SharePoint — it is only there if the `ForAll` included it.

---

## OnStart Collections Go Stale — Reload on Each Screen's OnVisible

`App.OnStart` loads collections once at app launch. If a user adds data in one screen and navigates to another, the collections are still the launch-time snapshot.

Add a `ClearCollect` reload at the top of `OnVisible` for any screen that depends on fresh data:

```powerfx
ClearCollect(colCourses, 'TT Courses');
ClearCollect(colMyRecords,
    Filter('TT TrainingRecords', Lower(PersonEmail) = varMyEmail));
```

This is especially important for `scrMyTraining` — without it, newly added courses won't appear until the app is relaunched.

---

## varViewingForSelf Must Be Initialised on Screen Load

If `scrMyTraining.OnVisible` checks `If(varViewingForSelf, ...)` and `varViewingForSelf` is blank (never set), the entire block is skipped and the gallery is empty.

Always initialise at the top of `OnVisible`:

```powerfx
If(IsBlank(varViewingForSelf), Set(varViewingForSelf, true));
```

This ensures self-view is the default the first time the screen opens, without interfering with team-view navigation from `scrTeamMember`.

Never hard-code `Set(varViewingForSelf, true)` inside `galMyTraining.OnSelect`. That forces self-view every time a course row is tapped, which breaks team-member viewing (the context switches away from the team member before the screen loads).

---

## Form Doesn't Reset Between Visits — OnVisible Must ResetForm

When a screen contains a Form control (`frmCert`), navigating away and back does not automatically reset the form. The previous record's data stays loaded.

Add to the screen's `OnVisible`:

```powerfx
ResetForm(frmCert)
```

Without this, revisiting the screen after viewing one course and tapping a different course can show stale data or cause form submission to patch the wrong record.

---

## Line Manager Relationship Is Directional

To allow Person A to upload training for Person B:
- Person B's `TT Personnel` record must have Person A's email in the `LineManagerEmail` field.
- Setting Person A's record to have Person B as manager only allows Person B to upload for Person A.

The relationship reads: "My manager can upload for me."

This is a common point of confusion. The guide must state it clearly when describing the team management feature.

---

## SharePoint Column Required Field Causes Network Error in Patch

If a SharePoint column is marked Required and the Patch formula sends a blank value for it, Power Apps returns:

```
Network error when using Patch function: Field 'FieldName' is required.
```

This is a SharePoint-level enforcement, not a Power Apps formula error. Two resolution paths:

1. **Unmark Required in SharePoint:** Go to the list → Column settings → Edit → set "Require that this column contains information" to No.
2. **Add app-level validation before Patch:** Use the Set-error-vars-then-If-guard pattern (see `ui-patterns.md`) to validate before the Patch call runs, preventing the network error from ever occurring.

Option 2 is preferred because it gives users a clear UI-level error message rather than a vague network error.

---

## ForAll SelectedItems: Alias vs No Alias for Multi-Select Choice Patch

Two valid ways to patch a multi-select Choice column from a Combo box:

**With alias (can fail in some contexts):**
```powerfx
ApplicableTo: ForAll(cmbNewApplic.SelectedItems As T, {Value: T.Value})
```

**Without alias (more reliable):**
```powerfx
ApplicableTo: ForAll(cmbNewApplic.SelectedItems, {Value: Value})
```

The alias form `As T` can cause a type mismatch in some Power Apps versions. The no-alias form is more reliable. Prefer the no-alias form in new guides.

---

## YAML `Text: =` Is Invalid

A bare `Text: =` with nothing after it is not valid YAML or a valid Power Fx expression. It typically appears when YAML is copied from a partial source or generated incorrectly.

Always use:
```yaml
Text: =""
```

Any property that should be visually empty needs an empty string expression, not a bare `=`.

---

## `%QUALIFIED_DATACARD_FIELD_VALUE.ID%` Is a Broken Placeholder

This string sometimes appears in Form card `Default` properties when YAML is exported incompletely or generated without the correct qualified field value. It is not valid Power Fx.

Replace it with the correct expression. For a DateCompleted data card:
```powerfx
=ThisItem.DateCompleted
```

For any data card, the correct `Default` is the field the card is bound to:
```powerfx
=ThisItem.FieldName
```

If you see this placeholder in YAML, treat it as a required fix before pasting.

---

## ModernButton Does Not Accept FontWeight

`ModernButton@1.0.0` does not expose `FontWeight`. Setting it causes a PA2108 error in the live editor.

Remove `FontWeight` from any `ModernButton` control. The button's font weight is controlled internally by the Fluent 2 system.

Other confirmed missing properties on ModernButton: none yet — but always audit against `verified-control-reference.md` before publishing YAML.

Confirmed missing on Toggle (`Toggle@1.1.5`): `Size` (font size). Toggle does not expose font size.

---

## Badge Control Cannot Repeat From a Collection

The Badge control from the insert menu is designed as a single status indicator. It cannot loop over a table to produce multiple pills.

To render a list of pill badges (e.g. ApplicableTo values), use a **Gallery with Classic Button pill controls** inside it:

```yaml
- galApplicableTo:
    Control: Gallery@2.15.0
    Variant: Vertical
    Properties:
      Height: =36
      Items: =LookUp('TT Courses', ID = Value(varCourse.CourseID)).ApplicableTo
      TemplatePadding: =0
      TemplateSize: =90
      WrapCount: =5
      Width: =500
    Children:
      - btnApplyPill:
          Control: Classic/Button@2.2.0
          Properties:
            DisplayMode: =DisplayMode.View
            Fill: =RGBA(24,95,165,1)
            HoverFill: =Self.Fill
            PressedFill: =Self.Fill
            Color: =RGBA(255,255,255,1)
            HoverColor: =RGBA(255,255,255,1)
            PressedColor: =RGBA(255,255,255,1)
            BorderThickness: =0
            Height: =28
            Width: =84
            RadiusTopLeft: =14
            RadiusTopRight: =14
            RadiusBottomLeft: =14
            RadiusBottomRight: =14
            Size: =10
            Text: =ThisItem.Value
            Y: =4
```

Key settings:
- `WrapCount` controls how many pills appear per row before wrapping.
- `TemplateSize` is the width slot per pill — increase if values like "Civil Service Learning" are clipped.
- `HoverFill = Self.Fill` and `PressedFill = Self.Fill` make the pill non-interactive visually.
- `DisplayMode = DisplayMode.View` prevents click responses.

For coloured pills by value:
```powerfx
Fill = Switch(
    ThisItem.Value,
    "Civil Servant", RGBA(56,152,220,1),
    "Army",          RGBA(59,109,17,1),
    "Contractor",    RGBA(239,159,39,1),
    RGBA(108,117,125,1)
)
```

Strings in the `Switch` must match the SharePoint Choice values exactly, including capitalisation.
