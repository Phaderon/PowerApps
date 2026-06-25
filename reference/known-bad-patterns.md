# Known Bad Patterns

Last checked: 2026-06-25

These are mistakes that must not reappear in this guide family.

## Control Properties

- Modern Combo box with `Placeholder`. Use `InputTextPlaceholder`.
- Modern Combo box with record-shaped `Items` and no explicit `ItemDisplayText`. Use the field that exists in `Items`, for example `ThisItem.DisplayName` for Office365Users search rows.
- Modern Text input with `HintText`. Use `Placeholder`.
- Modern Toggle read as `.Value`. Use `.Checked`.
- Modern Toggle caption set with `Text`. Use `Label`.
- Modern Toggle initial state set with `Default` in this guide family. Use `Checked`.
- Multi-select Combo box preselection with `Default`. Use `DefaultSelectedItems`.
- Modern Dropdown with table-shaped `Items` but no explicit `ItemDisplayText`.
- Modern Dropdown `Default` set as a plain string. Must be a record: `{Value: “...”}`. A plain string causes the dropdown to appear blank on load.
- Any property copied from a similar control without checking that control's Microsoft Learn page.
- `Size` on `Toggle@1.1.5`. Toggle does not expose font-size. Confirmed PA2108 in live editor 2026-06-20.
- `FontWeight` on `ModernButton@1.0.0`. Modern Button does not expose FontWeight. Confirmed by cross-check against user's working Screens.txt (which uses BasePaletteColor, Color, Size but never FontWeight) 2026-06-20.
- Radius properties on `Label@2.5.1` (`RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight`). Label does not expose them; use Classic Button for rounded pills/badges. Confirmed PA2108 in live editor 2026-06-23.
- Light or pastel `BasePaletteColor` on `ModernButton`. Fluent 2 overrides it with a dark fill. Use dark, saturated colours only.
- Conditional `BasePaletteColor` on `ModernButton` (e.g. `If(varTab="X", lightColour, darkColour)`). The light state always renders dark. Use Classic Button for any conditional colour states.
- `Color` override on a `ModernButton` to compensate for a wrong `BasePaletteColor`. Pick a darker seed instead.
- Trying to match an exact brand hex on a `ModernButton`. Work with Fluent 2 — pick the closest dark seed and let the framework derive the final shade.
- `Text: =` (bare, nothing after the equals) in YAML. Must be `Text: =””`.
- `%QUALIFIED_DATACARD_FIELD_VALUE.ID%` in a Form card `Default`. This is a broken placeholder — replace with the actual field expression, e.g. `ThisItem.DateCompleted`.
- YAML properties on a control generated from the guide's *intent* without running an audit against `verified-control-reference.md`. Always audit before publishing.

## Power Fx

- `ScreenTransition.Back`. Use `Back()` or a valid `ScreenTransition` enum.
- Bare `Ascending` or `Descending`. Use `SortOrder.Ascending` or `SortOrder.Descending`.
- Bare `Days`, `Months`, `Years` etc. or `TimeUnit.Days` as the unit argument to `DateAdd`/`DateDiff`. **Always use quoted strings: `”Days”`, `”Months”`, `”Years”`.** Confirmed broken in live builds (Training Tracker + Policy Tracker).
- Schema-less `[]` where Power Apps must infer collection shape.
- Gallery row index formulas. Use `ThisItem.ItemIndex` — it shifts when the gallery filters or sorts.
- `ThisItem.ID` inside collection-backed galleries unless the collection explicitly contains `ID`.
- Nested formulas that rely on ambiguous `ThisItem`; capture the row with `With` or use `As` aliases.
- Bare `DisplayMode=View`. Use `DisplayMode=DisplayMode.View` or set the property value to `DisplayMode.View`.
- `\xB7` or any `\x` escape sequence in Power Apps strings. Use `Char(decimal)` instead. Middle dot is `Char(183)`.
- `IsOdd()` — does not exist in Power Apps. Use `Mod(value, 2) = 1`.
- `SortByColumns` on a SharePoint Choice field. Use `Sort(..., Field.Value, SortOrder.Ascending)` to unwrap the Choice record.
- `”value” in MultiChoiceField` for multi-select Choice filtering. Use `CountIf(MultiChoiceField, Value = “value”) > 0`.
- `Launch(url)` without `LaunchTarget.New` — reuses current tab. Use `Launch(url, {}, LaunchTarget.New)`.
- `ScrollTo(gallery, item)` in screen `OnVisible` or any behavior formula. **`ScrollTo` is not universally supported in canvas apps** — confirmed "unknown or unsupported function" in live build (Policy Tracker). Remove it entirely; restore scroll position via Navigate to the screen instead, or accept the gallery always resets to the top.
- `SortByColumns(AddColumns(table, "SortKey", formula), "SortKey", ...)` pattern inside a **nested gallery's `Items` property** (where `table = ThisItem.GroupedItems`). The dynamically added column is not reliably resolved by `SortByColumns` in this context — confirmed error "column 'SortKey' does not exist" (Policy Tracker). Use `Sort(ThisItem.GroupedItems, formula, SortOrder.Ascending)` instead, referencing fields directly by bare name inside the formula.
- Referencing a SharePoint field in YAML that has not been confirmed to exist in the list. Before using any field name in card/form YAML, verify it is in the live SP list. Confirmed error when `Status.Value` was used but the SP list only had `Published` (boolean) — Policy Tracker.
- `ForAll(cmbControl.SelectedItems As T, {Value: T.Value})` for patching multi-select Choice. Prefer `ForAll(cmbControl.SelectedItems, {Value: Value})` — the alias form can cause type mismatches.
- Notify-first validation pattern (checking fields then calling Notify before running Patch). Use Set-error-vars-then-If-guard pattern instead.

## Architecture

- Loading collections only in `App.OnStart` and not reloading in screen `OnVisible`. Collections go stale when data is added in a different screen or session.
- Not initialising `varViewingForSelf` at the top of `OnVisible`. If it is blank, a self-view/team-view screen will show nothing.
- Hard-coding `Set(varViewingForSelf, true)` in a gallery row `OnSelect`. This breaks team-member viewing.
- Not calling `ResetForm(frmCert)` in a form screen's `OnVisible`. The form shows stale data on revisit.
- Not resetting error border variables (`Set(varErrX, false)`) when opening an edit panel. Red borders from a previous failed save linger.
- Assuming a field exists in `varCourse` because it exists in SharePoint. The field only exists in `varCourse` if the `ForAll` projection that built `colMyTraining` included it.
- Using Badge control to render repeating pills. Badge cannot loop over a collection — use Gallery + Classic Button.

## YAML File Structure

- Any screen YAML that does not start with `Screens:\n  ScreenName:`. The pa-yaml-wrap tool and PowerApps Studio paste both require this exact top-level format. **Never use `- ScreenName:` (list item).** Always use the dict form: `Screens:` at col 0, screen name at col 2, `Properties:` and `Children:` at col 4.
- `GroupContainer@1.5.0` without a `Variant:` keyword. **Every GroupContainer requires `Variant: ManualLayout` (or `Variant: AutoLayout`) between `Control:` and `Properties:`.** Omitting it causes PA1011 on paste. Confirmed broken in Overview build.
- `LayoutMode: =LayoutMode.ManualLayout` inside a GroupContainer's Properties block. **Do not set LayoutMode as a property — `Variant: ManualLayout` already implies it.** Including it causes PA2108. Remove the property entirely.
- `Gallery@2.15.0` without a `Variant:` keyword. **Every Gallery requires `Variant:` between `Control:` and `Properties:`.** Use `Variant: Vertical` for vertical galleries, `Variant: Horizontal` for horizontal galleries, `Variant: VariableHeight` for variable-height galleries. Confirmed PA1011 in Overview build.
- `Image@2.2.0` — stale. **Always use `Image@2.2.3`.** PA2105 warns it may produce errors.

## Guide-Writing

- “Same as above.”
- “Duplicate the previous screen.”
- “Use the same technique.”
- Long inline control paragraphs that hide exact properties.
- Background/card/panel/gallery-row controls without a layer-order note when they can cover other controls.
- Formulas that may temporarily red-line without a reassurance note explaining what later control/collection/variable resolves it.
- Grouping instructions that hide layer-order requirements or fail to list exactly which controls are included/excluded.
- Long property lists that mix actual changes with default values without marking which are defaults.
- Repeating fresh-control defaults from `powerapps-control-defaults.md` as if the user must manually change them.
- Repeating `Fill=RGBA(0,0,0,0)` on normal Label controls as if it must be manually changed.
- Repeating `BorderThickness=0` on normal Label controls as if it must be manually changed.
- Repeating `SelectMultiple=true` on modern Combo box controls as if it must be manually changed.
- Repeating `ItemDisplayText=ThisItem.Value` on modern Combo box simple value tables as if it must be manually changed.
- Treating a property omitted from the fresh-control export as a guaranteed literal default value.
- Control rows that say only “see formula below” when the formula can be placed in a collapsed copyable block beside the control.
- Any instruction that depends on visual guessing rather than exact control names and properties.
- Re-pasting full screen YAML to fix a single property. Targeted property changes are always safer and preserve existing customisations.
