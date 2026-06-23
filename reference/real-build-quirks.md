# Real Build Quirks

Last checked: 2026-06-20

These are issues found while building the Training Tracker app in the live Power Apps editor. Preserve them even when a generic Microsoft Learn example looks different, unless the live editor is rechecked and the guide is updated deliberately.

## SharePoint List Names With Spaces

Power Fx formulas must wrap SharePoint list names containing spaces in single quotes:

```powerfx
'TT Personnel'
'TT Courses'
'TT TrainingRecords'
```

Do not write unquoted list names in formulas.

## Layer Order

Layer order is a build requirement, not a cosmetic note.

Any classic Button used as a visual background must sit behind the controls it supports:

- card backgrounds
- panel backgrounds
- gallery row backgrounds
- indentation strips
- progress-bar backgrounds

In guide tables, place background controls before the controls that sit on top of them, and add a highlighted layer note when the order matters. If a background covers labels, inputs, icons or buttons in Power Apps, use Send to back or move it to the bottom/back of that screen, group, or gallery template before continuing.

For user-facing build guides, do not rely on table order alone. If a panel background appears first in a properties table, add a "Recommended build order" note that tells the builder to either:

- build the visible controls first, then create/send the panel background to the back, or
- build the panel first, then send it to the back after the visible controls are added.

For progress bars, the background bar must sit behind the fill bar:

```text
recBarBack behind recBarFill
```

## Temporary Formula Errors

Power Apps can show red-line formula errors while the builder is still partway through a phase and referenced controls, variables, or collections do not exist yet.

Future guides must call this out explicitly near the formula. Use this wording pattern:

```text
Temporary red-line note: this formula may complain until [control/collection/variable] exists. Finish this phase first, then recheck.
```

If a formula still red-lines after every control and formula in that phase is complete, treat it as a real issue.

## Grouping Controls

Groups are useful for clear sections such as tab bodies (`grpPeople`, `grpCourses`) and can make the tree tidier.

Use them carefully:

- Group after the controls work and layer order is correct.
- Do not let grouping hide which background control must sit behind visible controls.
- Grouping normally preserves control names, so formulas like `txtEditCourse.Text` still work.
- Avoid unnecessary nested groups during the first build because they can make selection and send-to-back/front operations harder to follow.
- If a group controls visibility, still make sure the guide explains which variable drives it and whether that variable may temporarily red-line.

## Default Values

Do not make the builder waste time hunting for properties that are already correct by default.

Guide rows should focus on properties that must be changed. If a default value is included because it is a useful safety check, label it clearly as default/safety check.

Use Microsoft Learn defaults where documented. If Microsoft Learn does not document a default for a property/control, do not claim one from memory.

Fresh Label controls in the user's live editor do not need `Fill=RGBA(0,0,0,0)` set manually when the goal is a normal transparent label over the screen/card background. The defaults lab did not serialize `Fill` for a fresh standalone Label, and the user confirmed the live editor already shows the intended default state. Future guide rows should omit label `Fill=RGBA(0,0,0,0)` unless transparency is a safety-critical reminder, in which case label it `leave default` or `default/safety check`.

Fresh Label controls in the user's live editor also default to `BorderThickness=0`. The defaults lab did not serialize `BorderThickness` for a fresh standalone Label, and the user confirmed the live editor shows `0`. Do not make `BorderThickness=0` a manual Label step unless it is a labelled safety check.

## Sort Order Enum

Use:

```powerfx
SortOrder.Ascending
SortOrder.Descending
```

Do not use bare `Ascending` or `Descending`.

## DateAdd Day Filters

In the Training Tracker expiring-soon formulas, the live editor accepted the day unit as a quoted string:

```powerfx
DateAdd(Today(), 60, "Days")
```

Do not normalize this to bare `Days`. Do not change it to `TimeUnit.Days` in this guide unless the live editor is rechecked.

## Modern Combo Box

Modern Combo box rows need placeholder fields made explicit:

```powerfx
InputTextPlaceholder="Applies to..."
```

In the user's live editor, modern Combo box `ItemDisplayText=ThisItem.Value` is already the default. Do not make `ItemDisplayText=ThisItem.Value` a manual step for simple value tables unless it is labelled `leave default` or `default/safety check`.

For Office365Users search results:

```powerfx
ItemDisplayText=ThisItem.DisplayName
```

Do not use `Placeholder` for modern Combo box.

Still set `ItemDisplayText` explicitly when the `Items` row shape does not display from a `Value` field, for example Office365Users search rows.

In the user's live editor, modern Combo box `SelectMultiple=true` is already the default. Do not make `SelectMultiple=true` a manual step unless it is labelled `leave default` or `default/safety check`. For single-select Combo boxes, set `SelectMultiple=false` explicitly.

## Modern Dropdown With Table Items

When a modern Dropdown uses a table of records, state the display formula explicitly:

```powerfx
ItemDisplayText=ThisItem.Label
```

For Training Tracker recurrence dropdowns, keep reading the numeric recurrence from:

```powerfx
drpNewRecur.Selected.Months
drpEditRecur.Selected.Months
```

## Modern Toggle

Use `Checked` for state and `Label` for caption text in this guide family. Do not use `.Value` to read modern Toggle state.

## Office365Users Casing

Preserve operation-specific casing:

- `Office365Users.SearchUserV2(...).value`: `.DisplayName`, `.Mail`
- `Office365Users.UserProfileV2(...)`: `.displayName`, `.jobTitle`, `.mail`

## ModernButton BasePaletteColor — Light Colours Always Render Dark

`BasePaletteColor` is a Fluent 2 seed, not a fill. The framework derives fill, text, and hover colours from it. Light and pastel seeds are treated as low-contrast accents and overrides them with dark fills.

Use only dark, saturated colours:
- Navy: `RGBA(24,95,165,1)`
- Dark green: `RGBA(34,139,80,1)` or `RGBA(34,139,80,1)`
- Dark grey: `RGBA(120,120,120,1)`
- Dark red: `RGBA(163,45,45,1)`

For any button that needs a light or white fill (tab nav active/inactive, etc.), switch to Classic Button and use `Fill`, `HoverFill`, `PressedFill` directly.

## Tab Buttons Must Be Classic Buttons

Modern Button cannot conditionally switch between light and dark fills for active/inactive tab states. Replace any ModernButton used as a tab navigation button with a Classic/Button and set `Fill` conditionally.

## IsOdd Does Not Exist

`IsOdd()` is not a Power Apps function. Use `Mod(value, 2) = 1`.

## \xB7 Prints as Literal Text

Power Apps strings do not support `\x` or `\u` escape sequences. `\xB7` outputs the four characters `\xB7` literally. Use `Char(183)` for the middle dot `·`.

## SortByColumns Fails on Choice Fields

`SortByColumns` cannot sort on a Choice column because the column returns a record. Use `Sort(source, ChoiceField.Value, SortOrder.Ascending)` to unwrap the Choice record to a string first.

## Multi-Select Choice: `in` Operator Silently Returns Nothing

`"Army" in ApplicableTo` checks for a full record match against a string — it always returns false. Use `CountIf(ApplicableTo, Value = "Army") > 0`.

## Launch Opens in Current Tab

`Launch(url)` reuses the current tab. Use `Launch(url, {}, LaunchTarget.New)` to open in a new tab.

## Collection Projections Must Include All Downstream Fields

If a detail screen reads `varCourse.CourseHost`, `varCourse.CourseURL`, etc., those fields must either be in the `ForAll` projection that built `colMyTraining`, or the detail screen must look them up directly from SharePoint. They do not flow through automatically.

## varViewingForSelf Must Be Initialised

Add `If(IsBlank(varViewingForSelf), Set(varViewingForSelf, true))` to the top of any screen `OnVisible` that branches on this variable. If it is never set, the screen body is skipped entirely.

## Form Does Not Reset Between Visits

Add `ResetForm(frmCert)` to a form screen's `OnVisible`. Without it, the form shows the previous record's data when the user navigates back and taps a different item.

## SharePoint Required Column Causes Network Error

A Patch against a SharePoint column marked Required with a blank value returns "Network error: Field 'X' is required." Unmark the column as Required in SharePoint, or add app-level validation to prevent Patch from running when the field is blank.

## Notify-First Validation Pattern Breaks Error Borders

If validation calls `Notify(...)` before setting error variables, the Notify message appears but the error borders (Visible driven by error variables) never show because the success path immediately clears everything. Set all error variables first, then check them in an If guard. See `ui-patterns.md` for the correct pattern.
