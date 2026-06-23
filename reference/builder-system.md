# App Builder System

Last checked: 2026-06-23

This document defines the conventions, naming rules, and workflow for generating a complete new Power Apps canvas app from scratch. When asked to build a new app, follow this document before writing a single line of YAML.

---

## Phase 0 — Consultation Q&A (Do This First, Always)

When the user requests a new app, do NOT start building immediately. Run a proper consultation phase first.

### Step 0a — First Response

When the user describes an app they want:
1. Acknowledge what they've told you.
2. Think through the use case and identify every gap, edge case, and design decision that needs clarifying.
3. Ask all your questions in a single message — grouped by topic, clearly numbered. Do not drip-feed questions one by one.
4. Be thorough. It is better to ask 10 questions now than to build something wrong and need to redesign it later.

The consultation is a proper design session — treat it like a requirements meeting. The user knows the business domain; you know the technical implications. Ask enough questions to design the data model, access rules, workflow, and screens with confidence before touching any code.

### Question Topics to Cover (derive specific questions from these)

**Purpose and scope:**
- What does this app need to do, exactly? What is the core task a user performs?
- Who uses it and what are their different roles?
- Are there any roles that can do things other roles cannot?
- How many users roughly?

**Workflow — standard user:**
- Walk me through what a standard user does when they open the app.
- What are the key actions they take? (add, edit, view, search, filter, submit)
- Is there any concept of "my records" vs "all records"?

**Workflow — manager/admin:**
- What can a manager or admin do that a standard user cannot?
- Can managers see or edit other people's records?
- Is there any kind of approval or sign-off flow?

**Business rules:**
- Are there any date-driven rules? (expiry, deadlines, renewal intervals, overdue logic)
- What does a record look like when it is "complete" vs "incomplete" vs "overdue"?
- Are there any status values a record can have? What triggers a status change?
- Are there any mandatory fields? (These become the validation rules in the app)

**Data relationships:**
- Are there different categories or types of thing being tracked? (e.g. different course types, asset categories)
- Does a person have a line manager relationship? Can managers update on behalf of others?
- Are there any lists of reference data that don't change often? (e.g. list of departments, list of roles)

**Edge cases:**
- What happens when someone leaves / is deactivated?
- What happens if a record needs to be deleted vs archived?
- Are there any records that should be read-only to most users?

**Notifications and reporting:**
- Does anyone need to be notified when something changes, expires, or is submitted?
- Does anyone need to export or report on the data?

**Branding:**
- Is the primary colour the default army dark green (`#004e42`), or a different colour?
- Any specific app name?

**Technical:**
- Are all users on the same M365 tenant?
- Is there an existing SharePoint site to use, or a new one?

### What NOT to ask the user
- List names, column names, column types — design these yourself in Phase 1.
- How many lists are needed — derive this from the workflow answers.
- What Choice option strings to use — propose sensible defaults and confirm only if the domain is specialised.
- Screen names or navigation structure — design these yourself in Phase 2.

### Step 0b — Follow-Up Questions

After the user answers, review their responses critically. If any answer raises new questions or reveals a gap, ask those as a short follow-up — still in one message.

It is acceptable to do up to 3 rounds of questions if the app is complex. Never build until you are confident you understand every part of the workflow.

### Step 0c — Confirm Before Building

When you have enough information to design the complete app, present a brief summary:
- App name
- Roles and what each can do
- Core screens (just names and one-line purpose)
- Key business rules

Then end with:

> **Ready to build?** Any final changes before I go ahead?

Wait for the user to say "build" or ask more questions. Do not start Phase 1 until the user explicitly confirms.

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
- Set `BasePaletteColor` to one dark seed and leave it alone — do not fight Fluent 2
  - Primary action: app primary colour (default `RGBA(0,78,66,1)`)
  - Secondary / cancel: `RGBA(120,120,120,1)`
  - Destructive: `RGBA(163,45,45,1)`
- Never set `BasePaletteColor` conditionally on a ModernButton — the light state will always render dark
- Never add a `Color` override to try to fix a bad `BasePaletteColor` — find a darker seed instead
- For anything needing conditional colour states (tab nav, active/inactive), use Classic Button instead

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

For a new app, always use the per-project repo system — do NOT push screen YAML into the `Phaderon/PowerApps` guide library repo.

See `output-format.md` for the exact delivery sequence and `project-repo-workflow.md` for the full GitHub repo setup procedure.

**Summary for a new app:**

1. Run the YAML validation checklist in `yaml-validation-checklist.md` before generating any YAML.
2. Deliver output in this order:
   - SharePoint setup checklist (tables)
   - Data connections list
   - **App.OnStart as a separate code block** — NEVER in screen YAML
   - GitHub Pages link for screen YAMLs
3. Create the per-project repo under `PhadeDev`:
   ```bash
   gh repo create PhadeDev/app-slug --description "Power Apps canvas app — App Name" --private --add-readme
   ```
4. Create the `docs/` structure and push screens via `pa-yaml-wrap`:
   ```bash
   pa-yaml-wrap /tmp/scrHome.yaml /var/home/Phaderon/PowerApps-Apps/app-slug/docs/screens/scrHome.html
   ```
5. Build the `docs/index.html` from the template in `project-repo-workflow.md`.
6. Commit and push to the project repo, enable GitHub Pages from `/docs`.
7. Report: live URL, screen paste order, issues tracker URL.
8. Ask user's permission to add a library card to `Phaderon/PowerApps/index.html`.

**App.OnStart separation rule — non-negotiable:**
App.OnStart is ALWAYS delivered as a separate code block. If a formula belongs in `App.OnStart`, it does NOT appear anywhere in the screen YAML. No exceptions.

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
