# Power Fx Patterns

Last checked: 2026-06-20

Sources:

- Formula reference: https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-canvas-apps
- Sort and SortByColumns: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-sort
- Patch: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-patch
- Filter, Search, LookUp: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-filter-lookup
- Distinct: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-distinct
- GroupBy/Ungroup/AddColumns examples: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-groupby
- UpdateContext: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-updatecontext

## Sorting

Use full enum values:

```powerfx
SortByColumns(Source, "Title", SortOrder.Ascending)
SortByColumns(Source, "Created", SortOrder.Descending)
```

Do not use bare `Ascending` or `Descending`.

## DateAdd Day Filters

Microsoft Learn documents `TimeUnit.Days`, but the Training Tracker live build required the day-unit argument as a quoted string in expiring-soon filters:

```powerfx
DateAdd(Today(), 60, "Days")
```

Do not change those Training Tracker formulas to bare `Days` or `TimeUnit.Days` unless the live editor is rechecked.

## Filtering And Lookup

Use `Filter` for many records and `LookUp` for the first matching record.

```powerfx
Filter('TT Personnel', Active = true)
LookUp('TT Personnel', Lower(Email) = varMyEmail)
```

Use `As` aliases in nested formulas:

```powerfx
Filter(colPeople As P, Lower(P.ManagerEmail) = varMyEmail)
```

## Patch

Use `Patch(DataSource, BaseRecord, ChangeRecord)` to update records. Use `Defaults(DataSource)` to create records.

```powerfx
Patch('TT Courses', Defaults('TT Courses'), {Title: txtCourse.Text})
Patch('TT Courses', varEditCourse, {Title: txtEditCourse.Text})
```

For SharePoint Choice columns, patch records with a `Value` field:

```powerfx
{Status: {Value: "Active"}}
```

For multi-choice columns, patch a table of `{Value: ...}` records:

```powerfx
{ApplicableTo: ForAll(cmbApplic.SelectedItems As T, {Value: T.Value})}
```

## Collections

Prefer explicit shape when initializing collections that will be patched or reused later. Avoid schema-less empty table literals in guide formulas.

Good:

```powerfx
ClearCollect(colCourses, 'TT Courses')
```

Avoid:

```powerfx
ClearCollect(colCourses, [])
```

## Record Scope

When a formula is inside a gallery and also uses nested `ForAll`, `Filter`, `AddColumns`, or `With`, capture the selected gallery row first:

```powerfx
With(
    {selectedPerson: ThisItem},
    Filter(colRecords, Lower(PersonEmail) = Lower(selectedPerson.Email))
)
```

## Navigation

Do not use `ScreenTransition.Back`. For browser-like back behavior, use:

```powerfx
Back()
```

For navigation transitions, use valid enum values such as:

```powerfx
Navigate(scrHome, ScreenTransition.Fade)
Navigate(scrHome, ScreenTransition.None)
```
