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
