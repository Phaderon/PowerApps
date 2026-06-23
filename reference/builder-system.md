# App Builder System

Last checked: 2026-06-23

This document defines the conventions, naming rules, and workflow for generating a complete new Power Apps canvas app from scratch. When asked to build a new app, follow this document before writing a single line of YAML.

---

## Phase 0 — Requirements Gathering (Ask First)

Before building anything, ask the user only about the business purpose and workflow. Do NOT ask about list names, column names, column types, or screen names — those are design decisions that belong to Phase 1 and are the builder's responsibility to define.

### Questions to ask the user

**What the app does:**
- What does this app need to do in one or two sentences?
- What problem is it solving?

**Who uses it:**
- Who are the users — what roles exist? (e.g. regular staff, managers, admins)
- How many people roughly?
- Do different roles see different things or have different permissions?

**Workflow:**
- Walk me through what a typical user does step by step when they open the app.
- Walk me through what an admin does.
- Are there any approval flows, manager relationships, or delegated actions?

**Business rules:**
- Are there any date-based rules? (expiry dates, recurrence intervals, deadlines)
- What makes a record complete vs incomplete?
- Are there any status states a record can be in?
- What happens when something expires or is overdue?

**Outputs:**
- Does anyone need to export or report on the data?
- Are there any notifications or alerts needed?

**Branding:**
- Primary colour? (default: army dark green `RGBA(0,78,66,1)` / `#004e42`)
- Any specific name for the app?

### What NOT to ask the user
- List names, column names, column types — design these yourself in Phase 1.
- How many lists are needed — derive this from the workflow.
- What Choice options to use — propose sensible defaults and confirm only if the domain is specialised.
- Screen names or navigation structure — design these yourself in Phase 2.

---

## Phase 1 — SharePoint List Design (Builder's Responsibility)

Based on the workflow the user described, design all SharePoint lists completely. Present the full design to the user as a setup checklist — column by column — so they can create it in SharePoint without needing to make any decisions.

### Output format to the user

For each list, produce a table like this:

**List name: `AB ListName`**

| Column name | Type | Options / Notes |
|---|---|---|
| Title | Single line of text | Built-in — rename to meaningful label if needed |
| Status | Choice | Active, Archived |
| Email | Single line of text | Store email in lowercase |
| ... | ... | ... |

Tell the user: exact column names (they must match in Power Fx), exact type to select in SharePoint, exact Choice option strings with their capitalisation, which columns to mark as Not Required (all of them — enforce required in the app).

### List name rules
- Prefix all related lists with the app abbreviation: `TT Personnel`, `TT Courses`, etc.
- List names with spaces must be wrapped in single quotes in Power Fx: `'TT Personnel'`
- Never reference a list without the prefix in formulas.
- Use 2–3 character abbreviation that won't clash with existing lists.

### Column type rules

| Intended use | SharePoint column type | Power Fx access |
|---|---|---|
| Short text | Single line of text | `record.ColumnName` |
| Long text | Multiple lines of text (plain) | `record.ColumnName` |
| Number | Number | `record.ColumnName` |
| Date | Date and Time (Date Only) | `record.ColumnName`, use `Text(date, "dd mmm yyyy")` |
| Single choice | Choice | `record.ColumnName.Value` |
| Multi-select choice | Choice (Allow multiple selections) | table of `{Value: "..."}` records |
| Yes/No | Yes/No | `record.ColumnName` (boolean) |
| Person/Group | Person or Group | returns a record; use specific sub-fields |
| URL | Single line of text | `record.ColumnName` — NOT SharePoint Hyperlink type |
| Attachment | Built-in (on SharePoint list) | accessed via Edit Form Attachments card only |

### Required field rule
Mark ALL columns as Not Required in SharePoint. Enforce required fields in the app using the Set-error-vars-then-If-guard pattern (see `ui-patterns.md`). This gives users a clear red-border error instead of a vague network error from SharePoint.

---

## Phase 2 — Variable and Collection Naming

### Global variables (Set)

| Prefix | Purpose | Example |
|---|---|---|
| `var` | Any global variable | `varMyEmail`, `varTab`, `varEditCourse` |
| `varMe` | Current user's record from the people list | `varMe` |
| `varErr` | Validation error flag (boolean) | `varErrTitle`, `varErrURL` |
| `varViewing` | Context for viewing another user's data | `varViewingPerson`, `varViewingForSelf` |
| `varSelected` | Currently selected record for a detail screen | `varSelectedCourse`, `varRecord` |
| `varEdit` | Record being edited in an edit panel | `varEditCourse`, `varEditPerson` |

### Collections (ClearCollect)

| Prefix | Purpose | Example |
|---|---|---|
| `col` | Any collection | `colCourses`, `colMyRecords` |
| `colMy` | Current user's records | `colMyTraining`, `colMyRecords` |
| `colView` | Records for the person being viewed | `colViewTraining`, `colViewRecords` |
| `colAll` | All records (admin context) | `colAllRecords`, `colAllPersonnel` |
| `colCompliance` | Computed compliance summary | `colCompliance` |

### Control naming

| Prefix | Control type |
|---|---|
| `btn` | Button (Classic or Modern) |
| `lbl` | Label |
| `txt` | Text input (Modern) |
| `cmb` | Combo box (Modern) |
| `drp` | Dropdown (Modern or Classic) |
| `gal` | Gallery |
| `rec` | Classic Button used as a panel/background |
| `ico` | Icon |
| `tgl` | Toggle (Modern) |
| `frm` | Form |
| `img` | Image |
| `tim` | Timer |

---

## Phase 3 — App.OnStart Template

Every app starts with these:

```powerfx
Set(varMyEmail, Lower(User().Email));
Set(varMe, LookUp('AppName Personnel', Lower(Email) = varMyEmail));
Set(varTab, "DefaultTab");
ClearCollect(colMainList, 'AppName MainList');
```

Add `ClearCollect` calls for every list the app needs at startup. Always use `Lower()` when comparing email addresses.

---

## Phase 4 — Screen Architecture

### Standard screens

Every app should have at minimum:

| Screen | Purpose |
|---|---|
| `scrStart` | Loading / login check / route to correct home |
| `scrHome` | Main user-facing screen |
| `scrDetail` | Detail / record view for a selected item |
| `scrAdmin` | Admin management screen (if admin role exists) |

Add screens for team management, profile pages, archive views, etc. as needed.

### Screen naming convention
- Use `scr` prefix: `scrMyTraining`, `scrCourseDetail`, `scrAdminManage`
- Name by function, not visual layout

### Screen OnVisible template
Every screen that shows data from a collection should reload that collection at the top of `OnVisible`:

```powerfx
ClearCollect(colCourses, 'TT Courses');
ClearCollect(colMyRecords,
    Filter('TT TrainingRecords', Lower(PersonEmail) = varMyEmail));
```

For screens that can show self-view or team-member view, add the initialisation guard:
```powerfx
If(IsBlank(varViewingForSelf), Set(varViewingForSelf, true));
```

---

## Phase 5 — Control Patterns

### Use Classic Button for
- Panel backgrounds / card backgrounds
- Gallery row backgrounds (alternating colour, status stripe)
- Tab navigation (active/inactive colour states)
- Visual dividers
- Error border highlights

### Use Modern Button for
- Actual clickable actions (Save, Add, Archive, Go to course)
- Use dark `BasePaletteColor` only (see `live-build-lessons.md`)

### Use Modern Text Input for
- Single-line text entry
- Multi-line text entry (set `Type = TextInputType.Multiline`)
- Search inputs (set `Type = TextInputType.Search`)

### Use Modern Combo Box for
- Multi-select (default — `SelectMultiple=true`)
- Single-select searchable (set `SelectMultiple=false`)
- People picker (bind to `Office365Users.SearchUserV2`)

### Use Modern Dropdown for
- Fixed single-select lists
- Always set `Default = {Value: "..."}` — never a plain string

### Use Modern Toggle for
- Boolean flags
- Filter toggles (e.g. "Non-compliant only")
- Read state with `.Checked`, not `.Value`

### Use Classic Gallery for
- All lists of records
- Pill badge rows (via WrapCount)

### Use Classic Edit Form for
- Any screen that needs SharePoint Attachments
- Date pickers bound to SharePoint date fields

---

## Phase 6 — YAML Generation Rules

### Format requirements
- 2-space indent
- CRLF line endings (the `pa-yaml-wrap` tool handles this)
- All formula values prefixed with `=`
- Multi-line formulas use `|-` block scalar
- Control version strings must match known versions from this reference pack

### Z-order rule
Controls listed LATER in the `Children` array appear IN FRONT. Background panels must be listed BEFORE the controls they sit behind.

### Children order
1. Background panels and cards (recPanel, recHeader)
2. Gallery controls
3. Input controls and labels
4. Overlay panels (edit panels, add panels — placed after the controls they cover)
5. Error border controls (immediately before the field they highlight — lower z-order)

Wait — error borders must appear BEHIND their field. Since later = in front, error borders must be listed BEFORE the field they highlight.

Correct order for a field with an error border:
```yaml
Children:
  - recErrTitle:       # error border — listed first = behind
      ...
  - txtTitle:          # field — listed after = in front
      ...
```

### Known invalid properties (do not generate)
- `FontWeight` on `ModernButton@1.0.0` — causes PA2108
- `Size` on `Toggle@1.1.5` — causes PA2108
- `Placeholder` on `ModernCombobox` — use `InputTextPlaceholder`
- `HintText` on any modern control — use `Placeholder` (ModernTextInput) or `InputTextPlaceholder` (ModernCombobox)
- `Text: =` (bare) — must be `Text: =""`
- `Default` for multi-select preselection on ModernCombobox — use `DefaultSelectedItems`
- `ScreenTransition.Back` — use `Back()`

### Audit before pushing
Run:
```bash
python3 tools/audit-guide.py path/to/guide.html
rg -n "FontWeight" screens/ScreenName.yaml
rg -n "Toggle.*Size|Size.*Toggle" screens/ScreenName.yaml
```

---

## Phase 7 — Patch Formula Template

For an Add form (creates new record):
```powerfx
Set(varErrField1, IsBlank(Trim(txtField1.Text)));
Set(varErrField2, CountRows(cmbField2.SelectedItems) = 0);

If(
    varErrField1 || varErrField2,
    false,
    Patch('List Name', Defaults('List Name'),
        {
            Title:   Trim(txtField1.Text),
            Field2:  ForAll(cmbField2.SelectedItems, {Value: Value}),
            Status:  {Value: "Active"}
        }
    );
    Set(varErrField1, false);
    Set(varErrField2, false);
    Notify("Added.", NotificationType.Success);
    Reset(txtField1);
    Reset(cmbField2);
    ClearCollect(colData, 'List Name')
)
```

For an Edit form (updates existing record):
```powerfx
Set(varErrField1, IsBlank(Trim(txtField1.Text)));
Set(varErrField2, CountRows(cmbField2.SelectedItems) = 0);

If(
    varErrField1 || varErrField2,
    false,
    Patch('List Name', varEditRecord,
        {
            Title:  Trim(txtField1.Text),
            Field2: ForAll(cmbField2.SelectedItems, {Value: Value})
        }
    );
    Set(varErrField1, false);
    Set(varErrField2, false);
    Notify("Saved.", NotificationType.Success);
    ClearCollect(colData, 'List Name');
    Set(varEditRecord, Blank())
)
```

---

## Phase 8 — Publishing Workflow

1. Write YAML to scratchpad or `/var/home/Phaderon/PowerApps/screens/`.
2. Run `pa-yaml-wrap` to wrap in copy-button HTML with CRLF:
   ```bash
   pa-yaml-wrap ~/Downloads/ScreenName.yaml /var/home/Phaderon/PowerApps/screens/ScreenName.html
   ```
3. Add a card to the root `index.html` (copy the scrAdminManage card pattern).
4. Commit and push:
   ```bash
   cd /var/home/Phaderon/PowerApps
   git add screens/ScreenName.html index.html
   git commit -m "Add ScreenName"
   git push origin main
   ```
5. Report the live URL: `https://phaderon.github.io/PowerApps/screens/ScreenName.html`
6. Add the new screen to the `AGENTS.md` list of known screen files.

---

## Quick Reference: Common Formula Patterns

### Get current user
```powerfx
Set(varMyEmail, Lower(User().Email));
Set(varMe, LookUp('AppName Personnel', Lower(Email) = varMyEmail));
```

### Filter gallery with search + type dropdown
```powerfx
SortByColumns(
    Filter(
        'DataSource',
        (IsBlank(txtSearch.Text) || txtSearch.Text in Title) &&
        (IsBlank(drpType.Selected.Value) ||
         drpType.Selected.Value = "All" ||
         StaffType.Value = drpType.Selected.Value)
    ),
    "Title", SortOrder.Ascending
)
```

### Navigate with context variable
```powerfx
Set(varSelectedRecord, ThisItem);
Navigate(scrDetail, ScreenTransition.Cover)
```

### TrainingStatus calculation
```powerfx
If(IsBlank(rec.DateCompleted), "Not Started",
   C.RecurrenceMonths = 0, "Complete",
   DateAdd(rec.DateCompleted, C.RecurrenceMonths, TimeUnit.Months) < Today(), "Expired",
   DateAdd(rec.DateCompleted, C.RecurrenceMonths, TimeUnit.Months) <= DateAdd(Today(), 60, "Days"), "Expiring Soon",
   "In Date")
```

### Sort gallery by status priority
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

### Open URL in new tab
```powerfx
Launch(urlValue, {}, LaunchTarget.New)
```

### Concat multi-select Choice for display
```powerfx
Concat(record.ApplicableTo, Value, ", ")
```

### Filter by multi-select Choice
```powerfx
CountIf(ApplicableTo, Value = drpFilter.Selected.Value) > 0
```
