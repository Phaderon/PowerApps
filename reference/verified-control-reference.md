# Verified Control Reference

Last checked: 2026-06-20

Sources:

- Modern control updates: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-updates
- Modern controls reference: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-reference
- Modern Text input: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input
- Modern Combo box: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox
- Modern Dropdown: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown
- Modern Toggle: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle
- Modern Button: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button
- Classic Button: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button
- Gallery: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-gallery
- Icon/shape controls: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-shapes-icons
- Edit form: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-form-detail
- Core properties: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-core

## Baseline Warning

Microsoft's modern controls are in active change. Microsoft Learn notes that modern controls received updated versions from February 2026 with new property names, enum values, and behavior changes. Recheck Microsoft Learn before using a control not listed here or before changing a property convention.

## Modern Text Input

Use for single-line, multi-line, password, and search text entry.

Verified key properties:

- `Default` - initial text value.
- `Text` - current entered text, used in formulas.
- `Placeholder` - hint text when empty.
- `Type` - use enum values such as `TextInputType.SingleLine`, `TextInputType.Multiline`, `TextInputType.Password`, `TextInputType.Search`.
- `TriggerOutput` - use enum values such as `TriggerOutput.Keypress`, `TriggerOutput.FocusOut`, `TriggerOutput.Delayed`.
- `Required`, `ValidationState`, `DisplayMode`, `Visible`.
- Layout/style: `X`, `Y`, `Width`, `Height`, `Align`, `PaddingTop`, `PaddingBottom`, `PaddingLeft`, `PaddingRight`, `Font`, `Size`, `Color`, `FontWeight`, `Italic`, `Underline`, `Strikethrough`, `Fill`, `BorderColor`, `BorderStyle`, `BorderThickness`, `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight`.

Do not use:

- `HintText` for modern Text input. Use `Placeholder`.
- `FontSize` if the current updated modern Text input control exposes `Size`; older guide rows may still use `FontSize` and should be checked in the live editor before final publishing.

## Modern Combo Box

Use for searchable selection, especially multi-select.

Verified key properties:

- `Items`
- `ItemDisplayText` - formula that determines the visible text for each item. Use `ThisItem` to reference the current row.
- `DefaultSelectedItems`
- `SelectMultiple`
- `InputTextPlaceholder` - hint text in the input field.
- `AccessibleLabel`, `IsSearchable`, `Visible`, `DisplayMode`
- Layout/style properties including `X`, `Y`, `Width`, `Height`, padding, color, font, fill, border, and radius properties as exposed by the current modern control.

Do not use:

- `Placeholder` for modern Combo box. Use `InputTextPlaceholder`.
- Missing `ItemDisplayText`. Simple value tables usually use `ThisItem.Value`; Office365Users search rows in this guide use `ThisItem.DisplayName`.
- `Default` for multi-select preselection. Use `DefaultSelectedItems`.
- `.Selected` when `SelectMultiple=true` and the formula needs all values. Use `.SelectedItems`.

Known build note:

- In the user's current Power Apps editor, `SelectMultiple=true` is the default for modern Combo box. Set `SelectMultiple=false` explicitly for single-selection Combo boxes.
- `ItemDisplayText` must match the shape of `Items`. `ThisItem.Value` only works when `Items` is a simple value table or SharePoint choice-style table with a `Value` field.

## Modern Dropdown

Use for a single fixed selection. Microsoft recommends Combo box for multi-select.

Verified key properties:

- `Items`
- `ItemDisplayText` - formula that determines the visible text for each item. For a table like `{Label: "...", Months: 12}`, use `ThisItem.Label`.
- `Default`
- `OnChange`
- `ValidationState`
- `Required`
- `AccessibleLabel`
- `Visible`, `DisplayMode`
- Style/layout properties including `Appearance`, `BasePaletteColor`, `Font`, `Size`, `Color`, `FontWeight`, `Italic`, `Underline`, `Strikethrough`, `Fill`, `BorderColor`, `BorderStyle`, `BorderThickness`, radius and padding properties.

Do not use:

- `DefaultSelectedItems`; that belongs to Combo box style selection, not modern Dropdown.
- Multi-select patterns; use Combo box instead.
- Old "display/value field" wording for table-shaped items. State `ItemDisplayText` explicitly.

## Modern Toggle

Use for true/false state.

Verified key properties:

- `Checked` - initial/current boolean state used by this guide pattern.
- `Label` - caption text beside the toggle.
- `OnCheck`, `OnUncheck`, `OnSelect`.
- `AccessibleLabel`, `Visible`, `DisplayMode`.

Do not use:

- `.Value` to read a modern Toggle in this guide. Use `.Checked`.
- `Text` for the visible caption. Use `Label`.
- `Default` for the initial state in this guide. Use `Checked`.

## Modern Button

Use for real clickable commands.

Common verified properties:

- `Text`
- `OnSelect`
- `DisplayMode`
- `Visible`
- `BasePaletteColor`
- `X`, `Y`, `Width`, `Height`
- Font and style properties exposed by the current modern Button control.

Do not use modern Button as a rounded static card unless the live editor supports all needed view/hover styling. The Training Tracker guide uses classic Button for static rounded panels.

## Classic Button As Rounded Panel

Use this established Training Tracker pattern for cards and rounded panels.

Required properties:

- `Text=""`
- `DisplayMode=DisplayMode.View`
- `Fill=<panel color>`
- `HoverFill=<same panel color>`
- `PressedFill=<same panel color>`
- `BorderColor`, `BorderThickness`
- `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight`

Do not use:

- Rectangle control for rounded panels. In this guide family, rounded panels are classic Buttons.

## Classic Gallery

Use for lists of records and repeated row layouts.

Verified core properties:

- `Items`
- Template sizing and child controls.
- Formula context supports `ThisItem`.
- For nested formulas, use `As` aliases or capture `ThisItem` first with `With`.

Do not assume:

- A row index property exists.
- `ThisItem.ID` exists in a collection unless the collection explicitly contains `ID`.

## Classic Icon

Use for action icons where Power Apps provides built-in icon shapes.

Verified core properties:

- Appearance, size, position, and `OnSelect`.

Do not use:

- Icons as a substitute for accessible labelled buttons unless the guide includes a clear accessible label or nearby text.

## Classic Edit Form And Attachments

Use classic Edit form when SharePoint attachments are required. The Training Tracker certificate upload depends on the classic Attachments card pattern.

Verified core properties:

- `DataSource`
- `Item`
- form mode actions such as `NewForm`, `EditForm`, `SubmitForm`, `ResetForm`.

Do not replace with:

- A modern-only control pattern unless attachments have been reverified in the target tenant/editor.
