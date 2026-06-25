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

## DateAdd / DateDiff Unit Argument — Always a Quoted String

**Hard rule (confirmed broken in live builds — Training Tracker and Policy Tracker):**

The time-unit argument to `DateAdd` and `DateDiff` must be a **quoted string**, not a bare identifier or enum:

```powerfx
// CORRECT
DateAdd(Today(), 7, "Days")
DateAdd(Today(), Mod(5 - Weekday(Today()) + 7, 7), "Days")
DateDiff(Today(), ExpiryDate, "Days")

// WRONG — causes runtime error in canvas apps
DateAdd(Today(), 7, Days)
DateAdd(Today(), 7, TimeUnit.Days)
```

Microsoft Learn sometimes documents `TimeUnit.Days` but this does not work in the canvas app formula bar. Always use quoted string literals: `"Days"`, `"Months"`, `"Years"`, `"Hours"`, `"Minutes"`, `"Seconds"`.

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

## Launch (Open URL in New Tab)

`Launch(url)` alone reuses the current browser tab, navigating away from the app.

Always use `LaunchTarget.New` to open in a new tab:

```powerfx
Launch(urlValue, {}, LaunchTarget.New)
```

The second argument must be `{}` (empty record placeholder).

## Alternating Row Colours

Do not use `ThisItem.ItemIndex` — it shifts when the gallery filters or sorts.

For SharePoint-backed galleries (items have `ThisItem.ID`):
```powerfx
If(Mod(ThisItem.ID, 2) = 0, RGBA(255,255,255,1), RGBA(247,249,252,1))
```

For collection-backed galleries with a numeric course or record ID:
```powerfx
If(Mod(ThisItem.CourseID, 2) = 0, RGBA(255,255,255,1), RGBA(247,249,252,1))
```

## Multi-Select Choice Field Filter

The `in` operator checks full record equality. A multi-select Choice column holds a table of `{Value: "..."}` records — `"Army" in ApplicableTo` always returns false.

Use `CountIf`:

```powerfx
CountIf(ApplicableTo, Value = drpFilter.Selected.Value) > 0
```

Inside a Filter:
```powerfx
Filter(source,
    IsBlank(drpFilter.Selected.Value) ||
    drpFilter.Selected.Value = "All" ||
    CountIf(ApplicableTo, Value = drpFilter.Selected.Value) > 0
)
```

## Sort Choice Field

`SortByColumns` on a SharePoint Choice field fails because the field returns a record.

Use `Sort()` with `.Value` to unwrap:

```powerfx
Sort(source, Status.Value, SortOrder.Ascending)
```

Double-sort (e.g. active before archived, then alphabetical):
```powerfx
Sort(
    Sort(source, Title, SortOrder.Ascending),
    Status.Value, SortOrder.Ascending
)
```

## Special Characters in Strings

Power Apps does not support `\x` or `\u` escape sequences. Use `Char(decimal)`:

```powerfx
Char(183)   // · middle dot / interpunct
```

## Training Status Calculation

Standard pattern used across the Training Tracker:

```powerfx
If(IsBlank(rec.DateCompleted), "Not Started",
   C.RecurrenceMonths = 0, "Complete",
   DateAdd(rec.DateCompleted, C.RecurrenceMonths, TimeUnit.Months) < Today(), "Expired",
   DateAdd(rec.DateCompleted, C.RecurrenceMonths, TimeUnit.Months) <= DateAdd(Today(), 60, "Days"), "Expiring Soon",
   "In Date")
```

## Sort Gallery by Status Priority

Add a numeric sort key then sort twice:

```powerfx
Sort(
    Sort(source, CourseName, SortOrder.Ascending),
    Switch(TrainingStatus,
        "Expired",       1,
        "Not Started",   2,
        "Expiring Soon", 3,
        "In Date",       4,
        "Complete",      5,
        99),
    SortOrder.Ascending
)
```

Or use `AddColumns`:

```powerfx
SortByColumns(
    AddColumns(
        source,
        SortKey, Switch(TrainingStatus,
            "Expired",       1,
            "Not Started",   2,
            "Expiring Soon", 3,
            "In Date",       4,
            "Complete",      5)
    ),
    "SortKey", SortOrder.Ascending,
    "CourseName", SortOrder.Ascending
)
```

## Concat Multi-Select Choice for Display

```powerfx
Concat(record.ApplicableTo, Value, ", ")
```

## ForAll Multi-Select Choice Patch

Prefer the no-alias form — the `As T` alias can cause type mismatches in some versions:

```powerfx
ApplicableTo: ForAll(cmbApplic.SelectedItems, {Value: Value})
```

## Collection ID vs SharePoint ID Type Mismatch

When a collection stores an ID that was originally from SharePoint (numeric), use `Value()` to force numeric comparison in LookUp:

```powerfx
LookUp('TT Courses', ID = Value(varCourse.CourseID))
```

## Days Remaining / Overdue

```powerfx
If(
    ExpiresOn >= Today(),
    Text(DateDiff(Today(), ExpiresOn, TimeUnit.Days)) & " days remaining",
    "Overdue by " & Text(DateDiff(ExpiresOn, Today(), TimeUnit.Days)) & " days"
)
```

## Visible Guard for Optional Date Fields

Any label or pill that only makes sense when an expiry date exists:

```powerfx
Visible = !IsBlank(ThisItem.ExpiresOn)
```

## If Chain Validation Before Patch

Do not use Notify-first. Set all error variables first, then gate the Patch:

```powerfx
Set(varErrTitle, IsBlank(Trim(txtTitle.Text)));
Set(varErrURL,   IsBlank(txtURL.Text));

If(
    varErrTitle || varErrURL,
    false,
    Patch(...);
    Set(varErrTitle, false);
    Set(varErrURL, false);
    Notify("Saved.", NotificationType.Success)
)
