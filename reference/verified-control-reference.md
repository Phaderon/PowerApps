# Verified Control Reference

Last checked: 2026-07-05

Sources:

- Modern control updates: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-updates
- Modern controls reference (full index of all modern controls): https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-reference
- Modern Text input: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input
- Modern Combo box: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox
- Modern Dropdown: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown
- Modern Toggle: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle
- Modern Button: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button
- Modern Progress bar: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-progress-bar
- Modern Avatar: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-avatar
- Modern Badge: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-badge
- Modern Checkbox: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-checkbox
- Modern Date picker: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-date-picker
- Modern Number input: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input
- Modern Radio group: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group
- Modern Slider: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider
- Modern Spinner: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-spinner
- Modern Tab List: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-tabs-or-tabs-list
- Modern Header: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-header
- Modern Link: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-link
- Modern Info button: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-info-button
- Modern Text: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text
- Modern Card (preview): https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-card
- Classic Button: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button
- Gallery: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-gallery
- Icon/shape controls: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-shapes-icons
- Edit form: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-form-detail
- Core properties: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-core

## Full Modern Control Catalogue (2026-07-05)

Microsoft's index page lists 23 modern controls total. Not all are documented in depth below yet — only the ones verified/used or likely to matter for this app family. Full list for reference: Avatar, Badge, Button, Card (preview), Checkbox, Combobox, Copilot answer (preview), Data Grid (preview), Date picker, Dropdown (preview), Header, Info button, Link, Number input, Progress bar, Radio group, Spinner, Slider, Stream (preview), Table (preview), Tabs/tab list, Text, Text input, Toggle. Copilot answer, Data Grid, Table, and Stream skipped below as niche/preview and not yet needed by any app in this family — fetch their pages the same way if a future build needs them.

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
- Missing `ItemDisplayText` when `Items` is record-shaped and the display field is not `Value`. Office365Users search rows in this guide use `ThisItem.DisplayName`.
- `Default` for multi-select preselection. Use `DefaultSelectedItems`.
- `.Selected` when `SelectMultiple=true` and the formula needs all values. Use `.SelectedItems`.

Known build note:

- In the user's current Power Apps editor, `SelectMultiple=true` is the default for modern Combo box. Set `SelectMultiple=false` explicitly for single-selection Combo boxes.
- In the user's current Power Apps editor, `ItemDisplayText=ThisItem.Value` is the default for modern Combo box simple value tables. Do not list it as a manual step unless it is a labelled default/safety check.
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

## Modern Progress Bar (`Progress@1.1.34`)

Displays determinate (`Value`/`Max`) or indeterminate (loading) progress. No native `ProgressBar` control name exists — the real control type is `Progress`.

Verified key properties:

- `Value` – number, 0 to `Max`. Only applies when `Indeterminate = false`.
- `Max` – the number that represents 100%. Not required to be 100 — set it to a real count (e.g. `CountRows(...)`) and skip doing percentage math yourself.
- `Indeterminate` – `true`/`false`. When `true`, `Value`/`Max` are ignored (animated loading state).
- `ProgressColor` – **plain string literal**, not a typed enum: `="Brand"`, `="Success"`, `="Error"`, or `="Warning"`. Confirmed live via a real control paste 2026-07-05 (`="Square"` shown in the formula bar) — do not assume this follows the same `'XCanvas.Y'.Z` enum pattern as Badge below; it doesn't.
- `Shape` – plain string literal: `="Square"` or `="Rounded"`.
- `Thickness` – plain string literal: `="Medium"` or `="Large"`.
- `BasePaletteColor` – only matters if you want a colour outside the four `ProgressColor` presets.
- No `Min` property. No `Fill`/`BorderColor` — colour is controlled only via `ProgressColor`/`BasePaletteColor`.

Full property list (from the properties panel, confirmed 2026-07-05): `AccessibleLabel`, `BasePaletteColor`, `ContentLanguage`, `DisplayMode`, `Height`, `Indeterminate`, `Max`, `OnChange`, `ProgressColor`, `Shape`, `Thickness`, `Value`, `Visible`, `Width`, `X`, `Y`.

**Why this entry exists:** built for the Policy Tracker Main screen redesign's readiness bar and Release Pipeline widget — first went in as hand-rolled `Rectangle` pairs (track + coloured fill) because this control wasn't in this file yet, and its exact syntax couldn't be safely guessed for a full-screen YAML paste. Real control export from the user's own tenant is what unblocked it.

## Modern Badge (`Badge@0.0.24`)

Already in live use in `Main.yaml` (`Version` control) — confirmed real formulas, not just docs:

```
Appearance: ='BadgeCanvas.Appearance'.Tint
ThemeColor: ='BadgeCanvas.ThemeColor'.Success
Shape: ='BadgeCanvas.Shape'.Rounded
```

**Contrast this with Progress bar above: Badge uses typed `'XCanvas.Y'.Z` enums, Progress bar uses plain string literals for what look like equivalent style properties (Shape, colour state). The two controls do NOT share a syntax convention — always verify per-control, never assume.**

Other properties (per docs, not yet confirmed live): `Content`, `ThemeColor` (docs list `brand`/`danger`/`important`/`informative`/`severe`/`subtle`/`success`/`warning` — note the real app uses `.Success` capitalised as a typed enum member, and `Tint` appears as a real `Appearance` value that isn't in the docs' filled/outline/ghost/inverted list, so the docs are incomplete here — trust the live export over the prose), `BasePaletteColor`, standard Font* properties, `AccessibleLabel`, `DisplayMode`.

## Modern Avatar (`ModernAvatar`, exact version unconfirmed)

Not yet used in any app in this family — worth using instead of hand-rolled initials-circle Labels (the pattern currently used for owner avatars on Policy Tracker's Main screen cards).

Verified key properties (per docs, not live-confirmed):

- `Name` – drives the initials shown when there's no image.
- `Image` – photo, e.g. `ThisItem.Owner.Picture` or `Office365Users.UserPhotoV2(...)`.
- `Badge` – small status decoration.
- `Shape` – Circular or Square.
- `Appearance` – `Brand` (theme colour), `Neutral` (grayscale), or `Colorful` (hash-of-Name colour — useful for auto-varied owner colours without hand-picking a palette).
- `BasePaletteColor`, standard Font* properties, `Out of office` (adjusts the badge icon).

Get a live export before using in a full-screen paste — exact enum syntax (typed vs. string literal) unconfirmed, same caveat as everything below not yet used live in this app family.

## Modern Checkbox

Same trap as Modern Toggle above:

- Read/set state via `Checked`, not `.Value` and not `Default`.
- `Label` is the caption text (not `Text`).
- `OnCheck` / `OnUncheck` / `OnSelect`.

## Modern Date Picker

- `Format` – `Short` / `LongAbbreviated` / `YearMonth` / `Custom` (custom takes a format string like `"dd/mm/yyyy"`). Exact literal syntax (typed enum vs string) unconfirmed — verify live before use.
- `SelectedDate` – the output property (local time).
- `StartDate` / `EndDate` – bounds.
- `StartOfWeek`, `IsEditable`, `Required`.
- `ValidationState` – `Error` / `None`, red border on `Error`.
- `PlaceHolder`, `OnChange`.

## Modern Number Input (`ModernNumberInput@1.0.0`)

- `Default` (input, initial value) vs. `Value` (output, read-only) — **same input/output split pattern as Modern Slider below.** Don't try to set `Value` directly.
- `Min` / `Max` / `Step` (default step is 1).
- `Precision` – typed enum `DecimalPrecision.Auto` / `DecimalPrecision.'0'` / `'1'` / `'2'` / `'3'` (note the quoted numeral syntax).
- `Appearance` – typed enum `Appearance.Filled` / `Appearance.FilledDarker` (default) / `Appearance.Outline`.
- `ValidationState` – `ValidationState.None` / `ValidationState.Error`.
- `OnChange` fires on blur/step-click, not every keystroke.
- Recent rename history (already-migrated apps may have old names): `FontColor`→`Color`, `FontSize`→`Size`, `FontItalic`→`Italic`, `FontStrikethrough`→`Strikethrough`, `FontUnderline`→`Underline`, `BorderRadius`→ four separate `RadiusTopLeft/Right/BottomLeft/Right`. `TriggerOutput` removed entirely.

## Modern Radio Group (`ModernRadio@1.0.0`)

- `Items`, `ItemDisplayText` (formula using `ThisItem`), `Default`, `Selected` (output), `OnChange`.
- `Layout` – typed enum `Layout.Vertical` (default) / `Layout.Horizontal`.
- Best for 2-7 mutually exclusive options; use Combo Box beyond that.
- Same Font* property renames as Number Input above apply here too — this whole modern-control generation was refactored together, expect the same rename list on any control touched in the same wave.

## Modern Slider (`ModernSlider@1.0.0`)

- `Default` (input, initial value) vs. `Value` (output, read-only) — **this was a breaking rename**: the old version took `Value` as the input property; the new version reserves `Value` for output only and uses `Default` for the initial value. If copying an old example from a blog, this will silently misbehave rather than error.
- `Min` (default 0) / `Max` (default 100).
- `LayoutDirection` – typed enum `LayoutDirection.Horizontal` (default) / `LayoutDirection.Vertical`. Previously a plain string `"Horizontal"`/`"Vertical"` — another breaking enum-format change.
- `Size` – typed enum `SliderSize.Small` / `SliderSize.Medium` (default) / `SliderSize.Large`. Previously a plain string.
- `OnChange`, `Tooltip`, `AccessibleLabel`.

**This control is the single clearest illustration of the Baseline Warning at the top of this file** — same control name, completely different formula syntax (string → typed enum, input/output property swap) between versions. Never trust an old example without checking the current docs' "Recent updates" section first.

## Modern Spinner

For loading states (page/table loading), distinct from Progress Bar's indeterminate mode — Spinner has no track/value concept at all, it's a pure animated icon + optional label.

- `Label`, `LabelPosition`, `SpinnerSize`.
- `Appearance` – Primary or Inverted.
- `AccessibleLabel`, `DisplayMode`, `OnChange`.

## Modern Tab List (`ModernTabList@1.0.0`)

**Directly relevant to this app family** — this is the real control for what Policy Tracker's Main_1 redesign hand-built as a `GroupContainer` + `Classic/Button` row (the segmented dashboard tab strip). Worth revisiting as a real upgrade once its exact live syntax is confirmed.

- `Items`, `Default`, `Selected` (output — drive content visibility off this, e.g. `ContentSection.Visible = TabList1.Selected.Value = "Overview"`).
- `OnChange` (fires on tab switch) vs. `OnSelect` (fires on any tab click, including re-clicking the active one).
- `Appearance` – typed enum `TabListAppearance.Transparent` / `.Subtle` / `.Underline` / `.Filled`.
- `Alignment` – typed enum `TabListAlignment.Start` / `.Center` (default) / `.End` — this is the whole tab list's position, distinct from `Align` (individual tab text alignment).
- 2-7 tabs recommended; no auto horizontal scroll if too many tabs are added.

## Modern Header

A prebuilt app-header control (logo + title + user photo). Deliberately NOT used as a replacement for this app family's fully custom top bars — it explicitly does **not** support colour customisation or app navigation, and doesn't auto-replicate across screens (must be added per screen manually). Documented here so it isn't reached for by mistake when a "modern header" is wanted; the custom `conTopBar`/`conHeader` pattern already used across Main/ViewItem/Main_1/ViewItem_1 remains the right approach for this app family.

- `Title`, `IsTitleVisible`, `Logo`, `IsLogoVisible`, `LogoMaxHeight`, `LogoToolTip`, `OnSelectLogo`, `IsProfilePictureVisible`, `Style`, `TitleFontSize`.

## Modern Link (`ModernLink@1.0.0`)

- `Text`, `Url` (blocks unsafe schemes like `javascript:`), `Wrap` (default true).
- `Type` – typed enum `LinkAppearance.Default` / `LinkAppearance.Subtle`. Renamed from `Appearance` in an earlier version.
- Standard Font*/Border*/Radius* properties.

## Modern Info Button (`ModernInformationButton@1.0.0`)

Inline "?" help icon that opens a flyout on click/hover — good candidate for field-level hint text instead of a separate hidden `lblHint` Label pattern already used elsewhere in this app family (e.g. `lblHighPriorityHint` in `ViewItem.yaml`).

- `Content` (flyout text), `IconColor`, `OnSelect`.
- Default size 32x32 — docs explicitly recommend not going smaller for tap targets.

## Modern Text (`ModernText@1.0.0`)

Already in live use throughout `Main.yaml` (the `Published`/`ReadyForRelease`/`ApprovedBy`/`LinkCount` pill labels on release cards) — confirmed real control, not just docs.

- `Text`, `Size`, `Color`, `FontWeight`, `Align`, `VerticalAlign` (default is now Middle), `Wrap`, `AutoHeight`.
- `Fill`, `BorderColor`, `BorderThickness`, `RadiusTopLeft/Right/BottomLeft/Right` — this control CAN look like a pill/badge on its own (fill + border + radius), which is exactly how the real app already uses it for the release-card pills.
- **`DisplayMode` was removed from the properties panel** in a recent update — the property still technically exists for backward compatibility but has no visible effect. Don't rely on it to lock down a `ModernText` control; use `Visible` instead if it needs to disappear.
- `OnSelect` now exists (didn't used to) — a `ModernText` can be a clickable label directly now, no need to layer an invisible Button on top purely for click behaviour (though the full-card-click pattern documented in `known-bad-patterns.md`/live-build-lessons may still prefer a Rectangle/Button for other reasons — this doesn't override that, just noting the option exists).

## Modern Card (`ModernCard@1.0.0`, preview)

**Preview control — treat with extra suspicion in a full-screen YAML paste.** The prose docs and the code examples on the same page don't even agree with each other: prose says the image-position property is `ImagePosition`, but every YAML example on the page uses `ImagePlacement` instead. That kind of doc/example mismatch is exactly the sort of thing that has broken pastes in this app before — get a live export before trusting either name.

- `Title`, `Subtitle`, `Description`, `Image`, `ImageAltText`, `HeaderImage`, `HeaderImageAltText`.
- `Direction` (prose) / `LayoutDirection` (example) — same naming inconsistency as above, `LayoutDirection.Horizontal` is what the actual YAML examples use.
- `Fill` auto-contrasts title/subtitle/description text colour unless `TitleColor`/`SubtitleColor`/`DescriptionColor` are set explicitly.
- Could be a real upgrade path for Policy Tracker's hand-built release-list item cards eventually, but not until this control's real property names are confirmed live — don't use it in a full-paste screen override until then.
