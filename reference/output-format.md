# App Delivery Output Format

Last checked: 2026-06-23

This document defines the exact format for delivering a complete Power Apps app build. Follow this order every time. Never mix App.OnStart into screen YAML.

---

## Delivery Order

When delivering a completed app, present output in this exact sequence:

### 1. SharePoint Setup Checklist

A table per list showing every column the user needs to create. They copy this directly to SharePoint. See `builder-system.md` Phase 1 for the table format.

Present this first so the user can create all lists before opening Power Apps Studio.

### 2. Data Connections

List the data connections the user must add in Power Apps Studio before pasting any YAML:

```
Add these data sources in Power Apps Studio (Data panel → Add data):
- 'XX ListName'   (SharePoint → your site → XX ListName)
- 'XX OtherList'  (SharePoint → your site → XX OtherList)
```

If Office365Users is needed:
```
- Office365Users  (Office 365 Users connector)
```

### 3. App.OnStart — Separate Code Block

**Never embed App.OnStart formulas inside screen YAML.** Always deliver it as a standalone Power Fx code block.

Example format:

```
## App.OnStart

Paste this into App → OnStart in the Power Apps Studio:
```powerfx
Set(varMyEmail, Lower(User().Email));
Set(varMe, LookUp('XX Personnel', Lower(Email) = varMyEmail));
Set(varTab, "Home");
ClearCollect(colPersonnel, 'XX Personnel')
```
```

The user pastes this into the App object's OnStart property, not into any screen.

### 4. GitHub Pages — Screen YAML

After creating the GitHub Pages site for the project (see `project-repo-workflow.md`), report:

```
Your app screens are ready at: https://phadedev.github.io/APP-NAME/

Paste order:
1. Open Power Apps Studio → New screen (blank) for each screen below
2. Open each link, click "Copy YAML", then paste into the new screen

Screen 1 — scrHome:    https://phadedev.github.io/APP-NAME/screens/scrHome.html
Screen 2 — scrDetail:  https://phadedev.github.io/APP-NAME/screens/scrDetail.html
Screen 3 — scrAdmin:   https://phadedev.github.io/APP-NAME/screens/scrAdmin.html
```

Screens are pasted one at a time. Each screen replaces the blank screen content.

### 5. Issues Tracker

Report the issues URL:

```
Report any problems here: https://github.com/PhadeDev/APP-NAME/issues
```

---

## App.OnStart Rules

- App.OnStart is ALWAYS a separate code block — never part of a screen's YAML
- App.OnStart must initialise every variable every screen may read
- App.OnStart loads initial collections that all screens share
- Screen OnVisible reloads screen-specific collections (see `builder-system.md` Phase 4)
- Screens must never depend on a variable that App.OnStart does not set

### Variables that must always be in App.OnStart

```powerfx
Set(varMyEmail, Lower(User().Email));
```

This is the identity anchor used by every filter, every permission check, every context load. It must come first.

### Collections that go in App.OnStart (load once)

- Reference lists that never change mid-session: `colCourses`, `colPersonnel`, `colCategories`
- These are static reference tables — not the user's live data

### Collections that go in screen OnVisible (reload each visit)

- Anything the user can edit: `colMyRecords`, `colAllRecords`, filtered lists
- Rule: if the user can Patch into it, reload it in OnVisible

---

## Non-Screen Code Blocks

Some formulas belong to specific controls rather than the screen or app, but are too long to embed clearly in YAML. If a formula is over 8 lines, consider delivering it as a separate labelled code block alongside the YAML:

```
### Formula: galHome → Items
Paste into the gallery's Items property:
```powerfx
SortByColumns(
  Filter( ...
```
```

Always make clear: control name, property name, and that this replaces the entire property value.

---

## What Never Goes in Screen YAML

- `App.OnStart` formulas
- Connection references or connector calls that belong at app level
- Variable initialisation that applies to all screens
- `%QUALIFIED_DATACARD_FIELD_VALUE%` or any template placeholder — these are bugs, not YAML

---

## Final Delivery Checklist

Before reporting "done" to the user, verify:

- [ ] SharePoint checklist is complete (all lists, all columns, all types, all Choice options)
- [ ] Data connections listed (every SharePoint list, any connectors)
- [ ] App.OnStart is a separate code block, not in any screen YAML
- [ ] Each screen YAML has a copy-button page on the project GitHub Pages
- [ ] GitHub Pages index shows all screens in paste order
- [ ] Issues tracker URL reported
- [ ] Library card added to `Phaderon/PowerApps` index.html (or confirm with user first)
