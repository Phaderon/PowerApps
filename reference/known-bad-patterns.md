# Known Bad Patterns

Last checked: 2026-06-20

These are mistakes that must not reappear in this guide family.

## Control Properties

- Modern Combo box with `Placeholder`. Use `InputTextPlaceholder`.
- Modern Combo box without `ItemDisplayText`. Use the field that exists in `Items`, for example `ThisItem.Value` for simple value tables or `ThisItem.DisplayName` for Office365Users search rows.
- Modern Text input with `HintText`. Use `Placeholder`.
- Modern Toggle read as `.Value`. Use `.Checked`.
- Modern Toggle caption set with `Text`. Use `Label`.
- Modern Toggle initial state set with `Default` in this guide family. Use `Checked`.
- Multi-select Combo box preselection with `Default`. Use `DefaultSelectedItems`.
- Modern Dropdown with table-shaped `Items` but no explicit `ItemDisplayText`.
- Any property copied from a similar control without checking that control's Microsoft Learn page.

## Power Fx

- `ScreenTransition.Back`. Use `Back()` or a valid `ScreenTransition` enum.
- Bare `Ascending` or `Descending`. Use `SortOrder.Ascending` or `SortOrder.Descending`.
- Training Tracker day filters using bare `Days` or unverified `TimeUnit.Days`. Preserve the verified quoted string `"Days"` unless the live editor is rechecked.
- Schema-less `[]` where Power Apps must infer collection shape.
- Gallery row index formulas.
- `ThisItem.ID` inside collection-backed galleries unless the collection explicitly contains `ID`.
- Nested formulas that rely on ambiguous `ThisItem`; capture the row with `With` or use `As` aliases.
- Bare `DisplayMode=View`. Use `DisplayMode=DisplayMode.View` or set the property value to `DisplayMode.View`.

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
- Treating a property omitted from the fresh-control export as a guaranteed literal default value.
- Control rows that say only "see formula below" when the formula can be placed in a collapsed copyable block beside the control.
- Any instruction that depends on visual guessing rather than exact control names and properties.
