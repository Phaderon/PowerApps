# YAML Pre-Output Validation Checklist

Last checked: 2026-06-23

Run through this checklist mentally before generating or outputting ANY screen YAML. Do not skip items based on "this section won't apply here" — check every item every time. A single missed property causes a PA2108 error that breaks the entire paste.

---

## 1. YAML Structure

- [ ] Every formula value starts with `=` prefix — no bare values on formula properties
- [ ] **[PA1001] `|-` is only allowed on event handlers and Items** — `OnSelect`, `OnChange`, `OnVisible`, `OnCheck`, `OnUncheck`, `Items`. All other properties (`Fill`, `Color`, `Visible`, `Text`, `DisabledFill`, `HoverFill`, `BorderColor`, etc.) must use a single-line formula. `|-` on style/visual properties causes PA1001 even with structurally valid YAML.
- [ ] **[PA1001] No inline multi-line formulas** — for every `Key: =Something(` line, count `(` vs `)`. If open > closed, it must use `|-`. But since `|-` is restricted to handlers/Items, the formula itself must be collapsed to a single line for any other property type.
- [ ] **[PA1001] Every `|-` block's first content line starts with `=`** — event handlers and Items only. Missing `=` causes PA1001 "Power Fx expressions must start with '='".
- [ ] **[PA1001] Inside `|-` blocks, closing parens follow paren depth** — outer `)` sits at the same indent as `=If(`. A double-`)` at the same indent level is wrong.
- [ ] Indent is exactly 2 spaces — no tabs anywhere
- [ ] Control names follow the naming convention (`btn`, `lbl`, `txt`, `cmb`, `drp`, `gal`, `rec`, `ico`, `tgl`, `frm`)
- [ ] No trailing spaces on any line
- [ ] **[PA1006] Screen-copy YAML starts with `Screens:`** — do not start with `- scrName:`. A bare top-level list item can cause PA1006 "Empty or invalid value for Control" at line 1, column 3 even when `Control: Screen` exists.
- [ ] **[PA1001] Screen nodes under `Screens:` do not have `Control:`** — `Screens:` → `scrName:` → `Properties:` is the valid shape. `Control: Screen` at this level causes "Property 'Control' not found on type ... ScreenInstance" at line 3, column 5.
- [ ] **[YAML parser] Quote single-line formulas containing `: `** — examples: `Default: '={Value: "New to MoD/Branch"}'` and `Text: '=If(IsBlank(varRole), "Role not set", "Role: " & varRole)'`. This keeps `yaml.safe_load` valid while preserving the parsed Power Fx formula.
- [ ] `Control:` and `Variant:` values use exact version strings (see version list below)
- [ ] **[PA2109] Gallery variants are exact and case-sensitive** — for `Gallery@2.15.0`, use `Variant: Vertical`, `Variant: Horizontal`, or `Variant: VariableHeight`; never `verticalGallery`.
- [ ] **[PA2108] Labels do not support radius properties** — never put `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, or `RadiusBottomRight` on `Label@2.5.1`. Use Classic Button for rounded pills/badges.
- [ ] Screen copy pages show a visible first-lines payload preview and refuse to copy stale `Control: Screen` screen payloads
- [ ] Index links to generated screen pages include the current version query string, for example `screens/scrDashboard.html?v=1.9`

### Known valid version strings

```
Label@2.5.1
  Do not use radius properties on Label@2.5.1
Classic/Button@2.2.0
Classic/Icon@2.5.0
Gallery@2.15.0
  Valid classic variants: Vertical, Horizontal, VariableHeight
Classic/TextInput@2.3.2
Classic/DropDown@2.3.1
Classic/ComboBox@2.4.0
Classic/DatePicker@2.6.0
Classic/CheckBox@2.1.0
Classic/Toggle@2.1.0
Form@2.4.4
ModernButton@1.0.0
ModernTextInput@1.1.0
ModernDropdown@1.0.1
ModernCombobox@1.1.0
Toggle@1.1.5
ModernDatePicker@1.0.0
GroupContainer@1.5.0
Rectangle@2.3.0
Image@2.2.3
Timer@2.1.0
HtmlViewer@2.1.0
```

---

## 2. Z-Order

Controls appear in the order listed — later = on top. Verify:

- [ ] Background panels (`recPanel`, `recHeader`, `recCard`) are listed FIRST
- [ ] Error border controls are listed IMMEDIATELY BEFORE the field they highlight (so they appear behind it)
- [ ] Overlay panels (edit/add panels) are listed LAST — they cover everything below
- [ ] Gallery row backgrounds are listed FIRST inside gallery Children

---

## 3. Property Blocklist — Check Every Control

**ModernButton@1.0.0 — do not generate these:**
- [ ] `FontWeight` — not exposed; causes PA2108
- [ ] `Color` as a workaround for BasePaletteColor — remove and fix the seed colour instead
- [ ] Conditional `BasePaletteColor` with light/pastel branches — use Classic Button instead
- [ ] Light or pastel `BasePaletteColor` (anything that reads like a pastel) — pick a darker seed

**Toggle@1.1.5 — do not generate:**
- [ ] `Size` (font size) — not exposed; causes PA2108
- [ ] `Default` for initial state — use `Checked`
- [ ] `.Value` to read state — use `.Checked`
- [ ] `Text` for label — use `Label`

**ModernCombobox@1.1.0 — do not generate:**
- [ ] `Placeholder` — use `InputTextPlaceholder`
- [ ] `HintText` — use `InputTextPlaceholder`
- [ ] `Default` for multi-select preselection — use `DefaultSelectedItems`

**ModernTextInput@1.1.0 — do not generate:**
- [ ] `HintText` — use `Placeholder`

**ModernDropdown@1.0.1 — verify:**
- [ ] `Default` is a record `{Value: "..."}` not a plain string — a plain string causes blank display on load
- [ ] If `Items` is table-shaped, `ItemDisplayText` is set explicitly

---

## 4. Power Fx Formula Checks

For every formula in the YAML, check:

- [ ] No `\xB7` or `\uXXXX` escape sequences → use `Char(183)` for middle dot
- [ ] No `IsOdd()` function → use `Mod(value, 2) = 1`
- [ ] No `SortByColumns` on a SharePoint Choice field → use `Sort(..., Field.Value, SortOrder.Ascending)`
- [ ] No `"value" in MultiChoiceField` → use `CountIf(field, Value = "value") > 0`
- [ ] No `Launch(url)` without `LaunchTarget.New` → use `Launch(url, {}, LaunchTarget.New)`
- [ ] No `ForAll(items As T, {Value: T.Value})` for patching → use `ForAll(items, {Value: Value})`
- [ ] No `Text: =` bare → any empty text must be `Text: =""`
- [ ] No `%QUALIFIED_DATACARD_FIELD_VALUE%` placeholder anywhere — replace with actual expression
- [ ] No `ScreenTransition.Back` → use `Back()` or a valid ScreenTransition enum
- [ ] No bare `Ascending`/`Descending` → use `SortOrder.Ascending` / `SortOrder.Descending`
- [ ] No `ThisItem.ItemIndex` in alternating row colours → use `Mod(ThisItem.ID, 2)` or stable field
- [ ] No Notify-first validation pattern → use Set-error-vars-then-If-guard (see `builder-system.md` Phase 7)
- [ ] `LookUp` by SharePoint ID through a collection: wrap with `Value()` → `LookUp('List', ID = Value(varRow.StoredID))`
- [ ] **[PA2108] No `.Value1` on SharePoint Choice fields** → always use `.Value`. `.Value1` is an internal artifact, not the choice string, and will error.
- [ ] **[Expected Boolean / Incompatible types] Toggle bound to a SharePoint Choice field** → use `field.Value = "Yes"` for `Checked`, `Visible`, `If()`, and `Label`; patch with `{Value: "Yes"}`/`{Value: "No"}`. If `field = true` causes "Incompatible types: Record, Boolean", the column is a Choice, not a Yes/No — switch to `.Value = "Yes"` throughout.

---

## 5. Architecture Checks

- [ ] Screen OnVisible reloads all collections this screen reads
- [ ] If `varViewingForSelf` is used: `If(IsBlank(varViewingForSelf), Set(varViewingForSelf, true))` is at the top of OnVisible
- [ ] If a Form control exists on this screen: `ResetForm(frmXxx)` is in OnVisible
- [ ] Error border vars are reset when opening any edit/add panel
- [ ] Every field read from `varSelected` or `varCourse` was included in the `ForAll` projection that built the collection, OR is looked up directly from SharePoint in the formula

---

## 6. SharePoint Integration

- [ ] All list names with spaces wrapped in single quotes in every formula: `'TT Personnel'`
- [ ] Choice fields accessed as `.Value`: `record.Status.Value` not `record.Status`
- [ ] Multi-select Choice patched with no-alias ForAll: `ForAll(cmbControl.SelectedItems, {Value: Value})`
- [ ] URL fields are Single line of text (not SharePoint Hyperlink type) — accessed as plain string
- [ ] Person/Group fields accessed via the correct sub-field (check `sharepoint-office365users.md`)

---

## 7. ModernButton Colour Check

For every ModernButton in the YAML:

- [ ] `BasePaletteColor` is dark and saturated — if you can read white text on it, it will work
- [ ] `BasePaletteColor` is a static value — not a conditional expression
- [ ] If the button needs active/inactive states → it must be a Classic Button, not ModernButton

Standard approved seeds:
- Primary action: `=RGBA(0,78,66,1)` (army dark green)
- Secondary / cancel: `=RGBA(120,120,120,1)`
- Destructive: `=RGBA(163,45,45,1)`

---

## 8. App.OnStart Separation

- [ ] App.OnStart formulas are NOT embedded in any screen YAML
- [ ] Every variable that screen formulas read is initialised in App.OnStart
- [ ] `varMyEmail` is set as the first line of App.OnStart

---

## 9. Delivery Readiness

- [ ] All screens are complete — no screen ends with TODO, placeholder, or missing formula
- [ ] Screen count matches what was agreed with the user
- [ ] GitHub Pages site has a page for every screen
- [ ] Index page shows screens in correct paste order
- [ ] Issues tracker URL is known and ready to report
- [ ] **Every screen HTML page carries a version and build timestamp** — pass `--version vX.Y` to `pa-yaml-wrap` on every output. Re-wrap every screen on every push, even if only one screen changed, so timestamps update uniformly.
- [ ] **`docs/index.html` carries the same version and local build timestamp** — inline after the `<h1>` title. Without this, the user cannot tell whether GitHub Pages has served the latest push when refreshing.
