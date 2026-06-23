# UI Patterns

Last checked: 2026-06-23

Reusable UI patterns verified in the Training Tracker live build. Use these as the basis for equivalent constructs in any future app.

---

## Rounded Panel Card (Classic Button)

Use a Classic Button as a rounded white card background. Do not use Rectangle controls — they don't support the same radius properties in this guide family.

```yaml
- recPanel:
    Control: Classic/Button@2.2.0
    Properties:
      Text: =""
      DisplayMode: =DisplayMode.View
      Fill: =RGBA(255,255,255,1)
      HoverFill: =RGBA(255,255,255,1)
      PressedFill: =RGBA(255,255,255,1)
      BorderColor: =RGBA(221,227,234,1)
      BorderThickness: =1
      RadiusTopLeft: =12
      RadiusTopRight: =12
      RadiusBottomLeft: =12
      RadiusBottomRight: =12
      X: =283
      Y: =80
      Width: =800
      Height: =120
```

Layer rule: this control must be listed BEFORE (lower in Children) any controls that sit on top of it. In Power Apps, controls listed later in the Children array appear in front.

---

## Tab Navigation Bar (Two Tabs)

Classic buttons give full conditional Fill control. ModernButton cannot render light-coloured inactive states reliably (see `live-build-lessons.md`).

```yaml
- btnTabPeople:
    Control: Classic/Button@2.2.0
    Properties:
      Text: ="People"
      Fill: =If(varTab="People", RGBA(34,139,80,1), RGBA(255,255,255,1))
      Color: =If(varTab="People", RGBA(255,255,255,1), RGBA(24,95,165,1))
      HoverFill: =If(varTab="People", RGBA(28,115,65,1), RGBA(235,241,250,1))
      PressedFill: =If(varTab="People", RGBA(22,95,55,1), RGBA(210,225,245,1))
      HoverColor: =Self.Color
      PressedColor: =Self.Color
      BorderColor: =RGBA(24,95,165,1)
      BorderThickness: =1
      RadiusTopLeft: =8
      RadiusTopRight: =8
      RadiusBottomLeft: =8
      RadiusBottomRight: =8
      OnSelect: =Set(varTab, "People")
      X: =672
      Y: =48
      Width: =120
      Height: =36

- btnTabCourses:
    Control: Classic/Button@2.2.0
    Properties:
      Text: ="Courses"
      Fill: =If(varTab="Courses", RGBA(34,139,80,1), RGBA(255,255,255,1))
      Color: =If(varTab="Courses", RGBA(255,255,255,1), RGBA(24,95,165,1))
      HoverFill: =If(varTab="Courses", RGBA(28,115,65,1), RGBA(235,241,250,1))
      PressedFill: =If(varTab="Courses", RGBA(22,95,55,1), RGBA(210,225,245,1))
      HoverColor: =Self.Color
      PressedColor: =Self.Color
      BorderColor: =RGBA(24,95,165,1)
      BorderThickness: =1
      RadiusTopLeft: =8
      RadiusTopRight: =8
      RadiusBottomLeft: =8
      RadiusBottomRight: =8
      OnSelect: =Set(varTab, "Courses")
      X: =800
      Y: =48
      Width: =120
      Height: =36
```

Tab body controls use `Visible: =varTab = "People"` or `Visible: =varTab = "Courses"`.

Initialise in `App.OnStart` or screen `OnVisible`:
```powerfx
Set(varTab, "People")
```

---

## Error Border Pattern (Validation Highlight)

A red Classic Button positioned behind an input field simulates a red border. Place it before the input in the Children list so it appears behind.

Template (replace `txtMyField` with the actual control name, `varErrMyField` with the error variable):

```yaml
- recErrMyField:
    Control: Classic/Button@2.2.0
    Properties:
      Text: =""
      DisplayMode: =DisplayMode.View
      Fill: =RGBA(163,45,45,1)
      HoverFill: =Self.Fill
      PressedFill: =Self.Fill
      BorderThickness: =0
      RadiusTopLeft: =8
      RadiusTopRight: =8
      RadiusBottomLeft: =8
      RadiusBottomRight: =8
      Height: =txtMyField.Height + 4
      Width: =txtMyField.Width + 4
      X: =txtMyField.X - 2
      Y: =txtMyField.Y - 2
      Visible: =varErrMyField
```

The +4 height/width and -2 X/Y creates a 2px overhang on each side — it reads as a red border, not a red fill.

If the field moves, the error border moves with it because it references the field's X/Y/Width/Height.

---

## Validation Pattern (Set Error Vars Then If Guard)

Do not use the Notify-first pattern for form validation. Notify fires before the error variables are set, so red borders don't appear.

Use this pattern for every save button that validates required fields:

```powerfx
Set(varErrTitle,  IsBlank(Trim(txtTitle.Text)));
Set(varErrApplic, CountRows(cmbApplic.SelectedItems) = 0);
Set(varErrHost,   IsBlank(drpHost.Selected.Value) || drpHost.Selected.Value = "Select...");
Set(varErrURL,    IsBlank(txtURL.Text));

If(
    varErrTitle || varErrApplic || varErrHost || varErrURL,
    false,
    Patch(DataSource, BaseRecord,
        {
            Title:      Trim(txtTitle.Text),
            ApplicableTo: ForAll(cmbApplic.SelectedItems, {Value: Value}),
            Host:       {Value: drpHost.Selected.Value},
            URL:        txtURL.Text
        }
    );
    Set(varErrTitle, false);
    Set(varErrApplic, false);
    Set(varErrHost, false);
    Set(varErrURL, false);
    Notify("Saved.", NotificationType.Success);
    ClearCollect(colData, DataSource)
)
```

Key rules:
- All `Set(varErrX, ...)` calls run unconditionally at the top, before the `If`.
- The `If` guard checks all error variables together.
- On success, all error variables are reset to `false` inside the success block.
- The Patch only runs if no errors are set.

---

## Clearing Error Borders When User Starts Correcting

Add `OnChange` to each validated input to clear the error variable as soon as the user types or changes the field:

```powerfx
txtTitle.OnChange:   Set(varErrTitle, false)
cmbApplic.OnChange:  Set(varErrApplic, false)
drpHost.OnChange:    Set(varErrHost, false)
txtURL.OnChange:     Set(varErrURL, false)
```

---

## Resetting Error Borders When Opening Edit Panel

Error variables linger from the previous save attempt. When the user opens an edit panel (e.g. clicking a pencil icon), reset all error variables:

Add to the pencil/edit button's `OnSelect`:
```powerfx
Set(varErrTitle, false);
Set(varErrURL, false);
Set(varErrApplic, false);
Set(varErrHost, false)
```

Without this, red borders from a previous failed save remain visible when the edit panel opens.

---

## Pill Badge Gallery (Repeating Coloured Pills)

Use a Gallery + Classic Button. The Badge control cannot loop over a collection.

```yaml
- galPills:
    Control: Gallery@2.15.0
    Variant: Vertical
    Properties:
      Items: =sourceTable
      TemplatePadding: =0
      TemplateSize: =90
      WrapCount: =5
      Height: =36
      Width: =500
      Visible: =CountRows(sourceTable) > 0
    Children:
      - btnPill:
          Control: Classic/Button@2.2.0
          Properties:
            Text: =ThisItem.Value
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
            Y: =4
```

Replace `sourceTable` with the actual table expression. For a SharePoint multi-select Choice field via LookUp:
```powerfx
Items: =LookUp('TT Courses', ID = Value(varCourse.CourseID)).ApplicableTo
```

For colour-coded pills by value (e.g. staff type):
```powerfx
Fill: =Switch(
    ThisItem.Value,
    "Civil Servant", RGBA(56,152,220,1),
    "Army",          RGBA(59,109,17,1),
    "Contractor",    RGBA(239,159,39,1),
    RGBA(108,117,125,1)
)
```

Increase `TemplateSize` and `btnPill.Width` together if long values like "Civil Service Learning" are clipped.

---

## Screen Header Bar

Full-width blue header with a back icon and title:

```yaml
- recHeader:
    Control: Classic/Button@2.2.0
    Properties:
      Text: =""
      DisplayMode: =DisplayMode.View
      Fill: =RGBA(24,95,165,1)
      HoverFill: =RGBA(24,95,165,1)
      PressedFill: =RGBA(24,95,165,1)
      BorderThickness: =0
      RadiusTopLeft: =0
      RadiusTopRight: =0
      RadiusBottomLeft: =0
      RadiusBottomRight: =0
      X: =0
      Y: =0
      Width: =1366
      Height: =72

- icoBack:
    Control: Classic/Icon@2.5.0
    Properties:
      Icon: =Icon.ChevronLeft
      Color: =RGBA(230,241,251,1)
      BorderColor: =RGBA(0,18,107,1)
      OnSelect: =Back()
      X: =16
      Y: =24
      Width: =24
      Height: =24

- lblScreenTitle:
    Control: Label@2.5.1
    Properties:
      Text: ="Screen Title"
      Color: =RGBA(255,255,255,1)
      FontWeight: =FontWeight.Bold
      Size: =16
      Font: =Font.'Open Sans'
      X: =52
      Y: =4
      Width: =900
      Height: =44

- lblScreenSub:
    Control: Label@2.5.1
    Properties:
      Text: ="Subtitle or context"
      Color: =RGBA(181,212,244,1)
      Size: =11
      Font: =Font.'Open Sans'
      X: =52
      Y: =44
      Width: =900
      Height: =24
```

---

## Training Status Colour Coding

Consistent colour values for status labels and fills across the app:

| Status | Fill | Text |
|---|---|---|
| Expired | `RGBA(163,45,45,1)` | `RGBA(255,255,255,1)` |
| Not Started | `RGBA(108,117,125,1)` | `RGBA(255,255,255,1)` |
| Expiring Soon | `RGBA(180,100,0,1)` | `RGBA(255,255,255,1)` |
| In Date | `RGBA(59,109,17,1)` | `RGBA(255,255,255,1)` |
| Complete | `RGBA(59,109,17,1)` | `RGBA(255,255,255,1)` |

Switch formula for Fill:
```powerfx
Switch(ThisItem.TrainingStatus,
    "Expired",       RGBA(163,45,45,1),
    "Not Started",   RGBA(108,117,125,1),
    "Expiring Soon", RGBA(180,100,0,1),
    "In Date",       RGBA(59,109,17,1),
    "Complete",      RGBA(59,109,17,1),
    RGBA(108,117,125,1)
)
```

---

## Days Remaining / Overdue Label

Show urgency text below a date label. Separate label, colour-coded.

```powerfx
Text = If(
    IsBlank(ThisItem.ExpiresOn),
    "",
    If(
        ThisItem.ExpiresOn >= Today(),
        Text(DateDiff(Today(), ThisItem.ExpiresOn, TimeUnit.Days)) & " days remaining",
        "Overdue by " & Text(DateDiff(ThisItem.ExpiresOn, Today(), TimeUnit.Days)) & " days"
    )
)

Color = If(
    IsBlank(ThisItem.ExpiresOn),
    RGBA(136,135,128,1),
    ThisItem.ExpiresOn < Today(), RGBA(163,45,45,1),
    DateDiff(Today(), ThisItem.ExpiresOn, TimeUnit.Days) <= 60, RGBA(180,100,0,1),
    RGBA(59,109,17,1)
)

Visible = !IsBlank(ThisItem.ExpiresOn)
```

`Visible = !IsBlank(ThisItem.ExpiresOn)` is critical — without it the label appears for courses with no expiry date.

---

## Date + Middle Dot Separator Label

A date label with `·` as a separator between date and expiry:

```powerfx
If(
    IsBlank(ThisItem.DateDone),
    "Not yet completed",
    "Completed " & Text(ThisItem.DateDone, "dd mmm yyyy") &
    If(
        IsBlank(ThisItem.ExpiresOn),
        "",
        " " & Char(183) & " expires " & Text(ThisItem.ExpiresOn, "dd mmm yyyy")
    )
)
```

`Char(183)` is the only correct way to produce `·` in a Power Apps string. Never use `\xB7`.

---

## Context-Aware Search and Filter (Shared Controls, Multiple Tabs)

When a search input and a dropdown filter are shared between two gallery tabs, wire each gallery's `Items` to the same controls and make the search placeholder context-aware.

Search placeholder:
```powerfx
txtSearch.Placeholder = If(varTab = "People", "Search name or email...", "Search course name...")
```

People gallery filter:
```powerfx
SortByColumns(
    Filter(
        'TT Personnel',
        Active = true &&
        (IsBlank(txtSearch.Text) ||
         txtSearch.Text in Title ||
         txtSearch.Text in Email) &&
        (IsBlank(drpTypeFilter.Selected.Value) ||
         drpTypeFilter.Selected.Value = "All types" ||
         StaffType.Value = drpTypeFilter.Selected.Value)
    ),
    "Title", SortOrder.Ascending
)
```

Courses gallery filter (multi-select Choice on ApplicableTo):
```powerfx
Sort(
    Sort(
        Filter(
            colCourses,
            (IsBlank(txtSearch.Text) ||
             txtSearch.Text in Title) &&
            (IsBlank(drpTypeFilter.Selected.Value) ||
             drpTypeFilter.Selected.Value = "All types" ||
             CountIf(ApplicableTo, Value = drpTypeFilter.Selected.Value) > 0)
        ),
        Title, SortOrder.Ascending
    ),
    Status.Value, SortOrder.Ascending
)
```

---

## ModernDropdown Default — Record Format

A ModernDropdown `Default` must be a record matching the Items row shape, not a plain string.

For Items bound to a simple string array:
```powerfx
Default = {Value: "All types"}
```

For Items bound to a table with a `Label` column:
```powerfx
Default = {Label: "Every year", Months: 12}
```

A plain string like `Default = "All types"` will cause the dropdown to show blank on load, and Filter formulas that check `.Selected.Value` will return no results.

---

## Non-Compliant Filter Toggle

Add a modern Toggle to let admins quickly filter to only staff with outstanding training:

```powerfx
tglNonCompliantOnly.Label = "Non-compliant only"
```

In the gallery `Items` filter, add as the last condition:
```powerfx
(!tglNonCompliantOnly.Checked || Outstanding > 0)
```

When the toggle is off (unchecked), `!false = true`, so the condition passes for all rows. When on, only rows with `Outstanding > 0` pass.

---

## TeamMember Drill-Down: Setting Context for Viewing Another Person's Training

When navigating from a team gallery to view someone else's training:

```powerfx
Set(varViewingPerson, LookUp('TT Personnel', Lower(Email) = Lower(ThisItem.Email)));
Set(varViewingForSelf, false);
ClearCollect(colViewRecords, Filter(colAllRecords, Lower(PersonEmail) = Lower(ThisItem.Email)));
```

Then build `colViewTraining` the same way as `colMyTraining` but using the selected person's email and staff type.

On `scrMyTraining`, switch the gallery source:
```powerfx
galMyTraining.Items = If(varViewingForSelf, colMyTraining, colViewTraining)
```

And update the greeting label:
```powerfx
If(varViewingForSelf,
    "Hello, " & First(Split(varMe.Title," ")).Value,
    "Viewing: " & varViewingPerson.Title)
```

---

## External Link Button (Opens New Tab)

```yaml
- btnGoToCourse:
    Control: ModernButton@1.0.0
    Properties:
      Text: ="Go to course →"
      BasePaletteColor: =RGBA(24,95,165,1)
      OnSelect: =Launch(LookUp('TT Courses', ID = Value(varCourse.CourseID), CourseURL), {}, LaunchTarget.New)
      Visible: =!IsBlank(LookUp('TT Courses', ID = Value(varCourse.CourseID), CourseURL))
      Width: =200
      Height: =30
```

Always use `LaunchTarget.New` as the third argument. The second argument must be `{}` (empty record).

---

## My Team Button (Auto-Hides When No Direct Reports)

```yaml
- btnMyTeam:
    Control: ModernButton@1.0.0
    Properties:
      Text: ="My team"
      BasePaletteColor: =RGBA(46,110,145,1)
      Visible: =CountRows(Filter('TT Personnel', Lower(LineManagerEmail) = varMyEmail && Active = true)) > 0
      OnSelect: =Navigate(scrTeamMember, ScreenTransition.Cover)
      X: =1086
      Y: =16
      Width: =124
      Height: =40
```

The button is invisible when the current user has no active direct reports. No additional logic needed.
