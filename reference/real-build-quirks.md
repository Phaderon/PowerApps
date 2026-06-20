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

Modern Combo box rows need all of these made explicit:

```powerfx
SelectMultiple=true
InputTextPlaceholder="Applies to..."
ItemDisplayText=ThisItem.Value
```

For Office365Users search results:

```powerfx
ItemDisplayText=ThisItem.DisplayName
```

Do not use `Placeholder` for modern Combo box.

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
