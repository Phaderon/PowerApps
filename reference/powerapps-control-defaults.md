# Power Apps Control Defaults

Last checked: 2026-06-20

This reference is generated from fresh controls inserted into the live Power Apps editor without manual edits.

## Source Evidence

- Classic fresh-control lab: `.sources/default-lab/LabClassic.txt` (18 parsed controls)
- Modern fresh-control lab: `.sources/default-lab/LabModern.txt` (49 parsed controls)

## Interpretation Rules

- Treat these as observed defaults from the user's tenant/editor, not universal Microsoft documentation.
- A serialized property means the fresh control export explicitly contained that property.
- An omitted property means the fresh control did not serialize it; do not invent a literal default value from absence alone.
- `X` and `Y` came from the repeated insert positions in the lab. Do not use them as default evidence.
- `Width`, `Height`, theme colors, font values, generated gallery children, and generated template formulas can be useful evidence, but still check whether the guide is intentionally changing behavior.
- Future guide rows should use this file to remove or label default-only properties as `leave default` or `default/safety check`.

## Quick Summary

| Source | Control | Example | Variant/Layout | Serialized properties excluding X/Y |
|---|---|---|---|---|
| Classic fresh-control lab | `Label@2.5.1` | `Label3` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'` |
| Classic fresh-control lab | `Classic/Button@2.2.0` | `Button6` | - | `BorderColor` -> `=ColorFade(Self.Fill, -15%)`; `Color` -> `=RGBA(255, 255, 255, 1)`; `DisabledBorderColor` -> `=RGBA(166, 166, 166, 1)`; `Fill` -> `=RGBA(56, 96, 178, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverBorderColor` -> `=ColorFade(Self.BorderColor, 20%)`; `HoverColor` -> `=RGBA(255, 255, 255, 1)`; `HoverFill` -> `=ColorFade(RGBA(56, 96, 178, 1), -20%)`; `PressedBorderColor` -> `=Self.Fill`; `PressedColor` -> `=Self.Fill`; `PressedFill` -> `=Self.Color` |
| Classic fresh-control lab | `Gallery@2.15.0` | `Gallery4` | Vertical | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Gallery@2.15.0` | `Gallery5` | Horizontal | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Gallery@2.15.0` | `Gallery6` | VariableHeight | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Form@2.4.4` | `Form2` | Classic, Vertical | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `FormViewer@2.3.4` | `FormViewer1` | Vertical | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Classic/TextInput@2.3.2` | `TextInput3` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverBorderColor` -> `=RGBA(0, 18, 107, 1)`; `HoverFill` -> `=RGBA(186, 202, 226, 1)` |
| Classic fresh-control lab | `Classic/DropDown@2.3.1` | `Dropdown1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `ChevronBackground` -> `=RGBA(56, 96, 178, 1)`; `ChevronFill` -> `=RGBA(255, 255, 255, 1)`; `ChevronHoverBackground` -> `=ColorFade(RGBA(56, 96, 178, 1), -20%)`; `ChevronHoverFill` -> `=RGBA(255, 255, 255, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverFill` -> `=RGBA(186, 202, 226, 1)`; `Items.Value` -> `=Value`; `PressedColor` -> `=RGBA(255, 255, 255, 1)`; `PressedFill` -> `=RGBA(0, 18, 107, 1)`; `SelectionColor` -> `=RGBA(255, 255, 255, 1)`; `SelectionFill` -> `=RGBA(56, 96, 178, 1)` |
| Classic fresh-control lab | `Classic/ComboBox@2.4.0` | `ComboBox1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `ChevronBackground` -> `=RGBA(56, 96, 178, 1)`; `ChevronFill` -> `=RGBA(255, 255, 255, 1)`; `ChevronHoverBackground` -> `=ColorFade(RGBA(56, 96, 178, 1), -20%)`; `ChevronHoverFill` -> `=RGBA(255, 255, 255, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverFill` -> `=RGBA(186, 202, 226, 1)`; `PressedColor` -> `=RGBA(255, 255, 255, 1)`; `PressedFill` -> `=RGBA(0, 18, 107, 1)`; `SelectionColor` -> `=RGBA(255, 255, 255, 1)`; `SelectionFill` -> `=RGBA(56, 96, 178, 1)` |
| Classic fresh-control lab | `DataTable@1.0.3` | `DataTable1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'`; `HeadingColor` -> `=RGBA(255, 255, 255, 1)`; `HeadingFill` -> `=RGBA(56, 96, 178, 1)`; `HeadingFont` -> `=Font.'Open Sans'`; `HoverFill` -> `=RGBA(186, 202, 226, .2)`; `SelectedFill` -> `=RGBA(56, 96, 178, .2)` |
| Classic fresh-control lab | `Classic/DatePicker@2.6.0` | `DatePicker2` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'`; `IconBackground` -> `=RGBA(56, 96, 178, 1)`; `IconFill` -> `=RGBA(255, 255, 255, 1)` |
| Classic fresh-control lab | `Classic/CheckBox@2.1.0` | `Checkbox1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `CheckboxBorderColor` -> `=RGBA(0, 18, 107, 1)`; `CheckmarkFill` -> `=RGBA(0, 0, 0, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverColor` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Classic/Radio@2.3.0` | `Radio2` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverColor` -> `=RGBA(0, 18, 107, 1)`; `Items.Value` -> `=Value`; `RadioBorderColor` -> `=RGBA(0, 18, 107, 1)`; `RadioSelectionFill` -> `=RGBA(0, 0, 0, 1)` |
| Classic fresh-control lab | `Classic/Toggle@2.1.0` | `Toggle2` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'`; `TrueFill` -> `=RGBA(56, 96, 178, 1)` |
| Classic fresh-control lab | `Classic/Slider@2.1.0` | `Slider2` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `ValueFill` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Rating@2.1.0` | `Rating1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `RatingFill` -> `=RGBA(0, 18, 107, 1)` |
| Classic fresh-control lab | `Classic/Icon@2.5.0` | `Icon2` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Color` -> `=RGBA(0, 18, 107, 1)`; `Icon` -> `=Icon.Alarm` |
| Modern fresh-control lab | `GroupContainer@1.5.0` | `Container1` | ManualLayout | `none beyond placement` |
| Modern fresh-control lab | `GroupContainer@1.5.0` | `Container2` | AutoLayout | `LayoutAlignItems` -> `=LayoutAlignItems.Center`; `LayoutDirection` -> `=LayoutDirection.Horizontal`; `PaddingBottom` -> `=8`; `PaddingLeft` -> `=8`; `PaddingRight` -> `=8`; `PaddingTop` -> `=8` |
| Modern fresh-control lab | `GroupContainer@1.5.0` | `Container3` | AutoLayout | `LayoutAlignItems` -> `=LayoutAlignItems.Center`; `LayoutDirection` -> `=LayoutDirection.Vertical`; `LayoutMinHeight` -> `=16`; `LayoutMinWidth` -> `=16`; `PaddingBottom` -> `=8`; `PaddingLeft` -> `=8`; `PaddingRight` -> `=8`; `PaddingTop` -> `=8` |
| Modern fresh-control lab | `GroupContainer@1.5.0` | `Container4` | GridLayout | `LayoutMinHeight` -> `=16`; `LayoutMinWidth` -> `=16` |
| Modern fresh-control lab | `Gallery@2.15.0` | `Gallery1` | BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0 | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=168`; `Width` -> `=468` |
| Modern fresh-control lab | `Image@2.2.3` | `Image1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=72`; `OnSelect` -> `=Select(Parent)`; `RadiusBottomLeft` -> `=8`; `RadiusBottomRight` -> `=8`; `RadiusTopLeft` -> `=8`; `RadiusTopRight` -> `=8`; `Width` -> `=72` |
| Modern fresh-control lab | `Label@2.5.1` | `Title1` | - | `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Color` -> `=RGBA(50, 49, 48, 1)`; `Font` -> `=Font.'Open Sans'`; `FontWeight` -> `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)`; `Height` -> `=Self.Size * 1.8`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=0`; `PaddingLeft` -> `=0`; `PaddingRight` -> `=0`; `PaddingTop` -> `=0`; `Size` -> `=14`; `Text` -> `=ThisItem.SampleHeading`; `VerticalAlign` -> `=VerticalAlign.Top`; `Width` -> `=Parent.TemplateWidth - 173` |
| Modern fresh-control lab | `Label@2.5.1` | `Subtitle1` | - | `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Font` -> `=Font.'Open Sans'`; `FontWeight` -> `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)`; `Height` -> `=Self.Size * 1.8`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=0`; `PaddingLeft` -> `=0`; `PaddingRight` -> `=0`; `PaddingTop` -> `=0`; `Size` -> `=12`; `Text` -> `=ThisItem.SampleText`; `VerticalAlign` -> `=VerticalAlign.Top`; `Width` -> `=Title1.Width` |
| Modern fresh-control lab | `Classic/Icon@2.5.0` | `NextArrow1` | - | `AccessibleLabel` -> `=Self.Tooltip`; `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Color` -> `=RGBA(166, 166, 166, 1)`; `DisabledBorderColor` -> `=RGBA(56, 56, 56, 1)`; `DisabledColor` -> `=RGBA(119, 119, 119, 1)`; `Height` -> `=50`; `Icon` -> `=Icon.ChevronRight`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=16`; `PaddingLeft` -> `=16`; `PaddingRight` -> `=16`; `PaddingTop` -> `=16`; `Tooltip` -> `="View item details"`; `Width` -> `=50` |
| Modern fresh-control lab | `Rectangle@2.3.0` | `Separator1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Fill` -> `=RGBA(255, 255, 255, 1)`; `Height` -> `=8`; `OnSelect` -> `=Select(Parent)`; `Width` -> `=Parent.TemplateWidth` |
| Modern fresh-control lab | `Rectangle@2.3.0` | `Rectangle1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Fill` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=Parent.TemplateHeight - Separator1.Height`; `OnSelect` -> `=Select(Parent)`; `Visible` -> `=ThisItem.IsSelected`; `Width` -> `=1` |
| Modern fresh-control lab | `Gallery@2.15.0` | `Gallery2` | BrowseLayout_Horizontal_TwoTextOneImageVariant_ver5.0 | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=168`; `Width` -> `=468` |
| Modern fresh-control lab | `Image@2.2.3` | `Image2` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=72`; `ImagePosition` -> `=ImagePosition.Fill`; `OnSelect` -> `=Select(Parent)`; `RadiusBottomLeft` -> `=8`; `RadiusBottomRight` -> `=8`; `RadiusTopLeft` -> `=8`; `RadiusTopRight` -> `=8`; `Width` -> `=Parent.TemplateWidth - 32` |
| Modern fresh-control lab | `Label@2.5.1` | `Title2` | - | `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Color` -> `=RGBA(50, 49, 48, 1)`; `Font` -> `=Font.'Open Sans'`; `FontWeight` -> `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)`; `Height` -> `=Self.Size * 1.8`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=0`; `PaddingLeft` -> `=0`; `PaddingRight` -> `=0`; `PaddingTop` -> `=0`; `Size` -> `=14`; `Text` -> `=ThisItem.SampleHeading`; `VerticalAlign` -> `=VerticalAlign.Top`; `Width` -> `=Parent.TemplateWidth - 64` |
| Modern fresh-control lab | `Label@2.5.1` | `Subtitle2` | - | `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Font` -> `=Font.'Open Sans'`; `FontWeight` -> `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)`; `Height` -> `=Self.Size * 1.8`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=0`; `PaddingLeft` -> `=0`; `PaddingRight` -> `=0`; `PaddingTop` -> `=0`; `Size` -> `=12`; `Text` -> `=ThisItem.SampleText`; `VerticalAlign` -> `=VerticalAlign.Top`; `Width` -> `=Title2.Width` |
| Modern fresh-control lab | `Gallery@2.15.0` | `Gallery3` | BrowseLayout_Flexible_SocialFeed_ver5.0 | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=168`; `Width` -> `=468` |
| Modern fresh-control lab | `Image@2.2.3` | `ProfileImage1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=12`; `ImagePosition` -> `=ImagePosition.Fill`; `OnSelect` -> `=Select(Parent)`; `RadiusBottomLeft` -> `=8`; `RadiusBottomRight` -> `=8`; `RadiusTopLeft` -> `=8`; `RadiusTopRight` -> `=8`; `Width` -> `=64` |
| Modern fresh-control lab | `Label@2.5.1` | `Title3` | - | `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Color` -> `=RGBA(50, 49, 48, 1)`; `Font` -> `=Font.'Open Sans'`; `FontWeight` -> `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)`; `Height` -> `=12`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=0`; `PaddingLeft` -> `=0`; `PaddingRight` -> `=0`; `PaddingTop` -> `=0`; `Size` -> `=14`; `Text` -> `=ThisItem.SampleHeading`; `VerticalAlign` -> `=VerticalAlign.Top`; `Width` -> `=Parent.TemplateWidth - 112` |
| Modern fresh-control lab | `Image@2.2.3` | `Image3` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Height` -> `=Min(Self.Width, Parent.TemplateHeight - 180)`; `ImagePosition` -> `=ImagePosition.Fill`; `OnSelect` -> `=Select(Parent)`; `RadiusBottomLeft` -> `=8`; `RadiusBottomRight` -> `=8`; `RadiusTopLeft` -> `=8`; `RadiusTopRight` -> `=8`; `Width` -> `=Parent.TemplateWidth - 32` |
| Modern fresh-control lab | `Label@2.5.1` | `Body1` | - | `AutoHeight` -> `=true`; `BorderColor` -> `=RGBA(0, 0, 0, 1)`; `Font` -> `=Font.'Open Sans'`; `FontWeight` -> `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)`; `Height` -> `=12`; `OnSelect` -> `=Select(Parent)`; `PaddingBottom` -> `=0`; `PaddingLeft` -> `=0`; `PaddingRight` -> `=0`; `PaddingTop` -> `=0`; `Size` -> `=12`; `Text` -> `=ThisItem.SampleText`; `VerticalAlign` -> `=VerticalAlign.Top`; `Width` -> `=Parent.TemplateWidth - 32` |
| Modern fresh-control lab | `Header@0.0.44` | `Header1` | - | `none beyond placement` |
| Modern fresh-control lab | `Form@2.4.4` | `Form1` | Vertical | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Modern fresh-control lab | `ModernButton@1.0.0` | `Button5` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernTextInput@1.1.0` | `TextInput2` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernNumberInput@1.1.0` | `NumberInput1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernDropdown@1.0.1` | `modernDropdown2` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernCombobox@1.1.0` | `Combobox3` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernDatePicker@1.0.0` | `DatePicker1` | - | `none beyond placement` |
| Modern fresh-control lab | `CheckBox@0.0.30` | `CheckboxCanvas1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernRadio@1.0.0` | `Radio1` | - | `none beyond placement` |
| Modern fresh-control lab | `Toggle@1.1.5` | `Toggle1` | - | `none beyond placement` |
| Modern fresh-control lab | `PenInput@2.3.0` | `PenInput1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Modern fresh-control lab | `ModernTabList@1.0.0` | `TabList1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernSlider@1.0.0` | `Slider1` | - | `none beyond placement` |
| Modern fresh-control lab | `ListBox@2.2.0` | `ListBox1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverFill` -> `=RGBA(186, 202, 226, 1)`; `Items.Value` -> `=Value`; `PressedColor` -> `=RGBA(255, 255, 255, 1)`; `PressedFill` -> `=RGBA(0, 18, 107, 1)`; `SelectionColor` -> `=RGBA(255, 255, 255, 1)`; `SelectionFill` -> `=RGBA(56, 96, 178, 1)` |
| Modern fresh-control lab | `RichTextEditor@2.7.0` | `RichTextEditor1` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Modern fresh-control lab | `ModernText@1.0.0` | `Text1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernInformationButton@1.0.0` | `InformationButton1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernIcon@1.1.0` | `Icon1` | - | `none beyond placement` |
| Modern fresh-control lab | `Avatar@1.0.40` | `Avatar1` | - | `none beyond placement` |
| Modern fresh-control lab | `Badge@0.0.24` | `BadgeCanvas1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernCard@1.2.0` | `Card1` | - | `none beyond placement` |
| Modern fresh-control lab | `Progress@1.1.34` | `Progress1` | - | `none beyond placement` |
| Modern fresh-control lab | `Spinner@1.4.6` | `Spinner1` | - | `none beyond placement` |
| Modern fresh-control lab | `ModernLink@1.0.0` | `Link1` | - | `none beyond placement` |
| Modern fresh-control lab | `Timer@2.1.0` | `Timer1` | - | `BorderColor` -> `=ColorFade(Self.Fill, -15%)`; `Color` -> `=RGBA(255, 255, 255, 1)`; `DisabledBorderColor` -> `=ColorFade(Self.BorderColor, 70%)`; `DisabledColor` -> `=ColorFade(Self.Fill, 90%)`; `DisabledFill` -> `=ColorFade(Self.Fill, 70%)`; `Fill` -> `=RGBA(56, 96, 178, 1)`; `Font` -> `=Font.'Open Sans'`; `HoverBorderColor` -> `=ColorFade(Self.BorderColor, 20%)`; `HoverColor` -> `=RGBA(255, 255, 255, 1)`; `HoverFill` -> `=ColorFade(RGBA(56, 96, 178, 1), -20%)`; `PressedBorderColor` -> `=Self.Fill`; `PressedColor` -> `=Self.Fill`; `PressedFill` -> `=Self.Color` |
| Modern fresh-control lab | `HtmlViewer@2.1.0` | `HtmlText1` | - | `Font` -> `=Font.'Open Sans'` |
| Modern fresh-control lab | `Image@2.2.3` | `Image4` | - | `BorderColor` -> `=RGBA(0, 18, 107, 1)` |
| Modern fresh-control lab | `PDFViewer@2.5.0` | `PdfViewer1` | - | `none beyond placement` |

## Full Parsed Details

### Classic fresh-control lab

#### `Label3` - `Label@2.5.1`

- Path: `Label3`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `X` | `=40` | placement from lab insert order; ignore as default evidence |
| `Y` | `=40` | placement from lab insert order; ignore as default evidence |

#### `Button6` - `Classic/Button@2.2.0`

- Path: `Button6`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=ColorFade(Self.Fill, -15%)` |  |
| `Color` | `=RGBA(255, 255, 255, 1)` |  |
| `DisabledBorderColor` | `=RGBA(166, 166, 166, 1)` |  |
| `Fill` | `=RGBA(56, 96, 178, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverBorderColor` | `=ColorFade(Self.BorderColor, 20%)` |  |
| `HoverColor` | `=RGBA(255, 255, 255, 1)` |  |
| `HoverFill` | `=ColorFade(RGBA(56, 96, 178, 1), -20%)` |  |
| `PressedBorderColor` | `=Self.Fill` |  |
| `PressedColor` | `=Self.Fill` |  |
| `PressedFill` | `=Self.Color` |  |
| `X` | `=60` | placement from lab insert order; ignore as default evidence |
| `Y` | `=60` | placement from lab insert order; ignore as default evidence |

#### `Gallery4` - `Gallery@2.15.0` - variant `Vertical`

- Path: `Gallery4`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=80` | placement from lab insert order; ignore as default evidence |
| `Y` | `=80` | placement from lab insert order; ignore as default evidence |

#### `Gallery5` - `Gallery@2.15.0` - variant `Horizontal`

- Path: `Gallery5`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=100` | placement from lab insert order; ignore as default evidence |
| `Y` | `=100` | placement from lab insert order; ignore as default evidence |

#### `Gallery6` - `Gallery@2.15.0` - variant `VariableHeight`

- Path: `Gallery6`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=120` | placement from lab insert order; ignore as default evidence |
| `Y` | `=120` | placement from lab insert order; ignore as default evidence |

#### `Form2` - `Form@2.4.4` - variant `Classic` - layout `Vertical`

- Path: `Form2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=140` | placement from lab insert order; ignore as default evidence |
| `Y` | `=140` | placement from lab insert order; ignore as default evidence |

#### `FormViewer1` - `FormViewer@2.3.4` - layout `Vertical`

- Path: `FormViewer1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=160` | placement from lab insert order; ignore as default evidence |
| `Y` | `=160` | placement from lab insert order; ignore as default evidence |

#### `TextInput3` - `Classic/TextInput@2.3.2`

- Path: `TextInput3`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverBorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `HoverFill` | `=RGBA(186, 202, 226, 1)` |  |
| `X` | `=180` | placement from lab insert order; ignore as default evidence |
| `Y` | `=180` | placement from lab insert order; ignore as default evidence |

#### `Dropdown1` - `Classic/DropDown@2.3.1`

- Path: `Dropdown1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `ChevronBackground` | `=RGBA(56, 96, 178, 1)` |  |
| `ChevronFill` | `=RGBA(255, 255, 255, 1)` |  |
| `ChevronHoverBackground` | `=ColorFade(RGBA(56, 96, 178, 1), -20%)` |  |
| `ChevronHoverFill` | `=RGBA(255, 255, 255, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverFill` | `=RGBA(186, 202, 226, 1)` |  |
| `Items.Value` | `=Value` |  |
| `PressedColor` | `=RGBA(255, 255, 255, 1)` |  |
| `PressedFill` | `=RGBA(0, 18, 107, 1)` |  |
| `SelectionColor` | `=RGBA(255, 255, 255, 1)` |  |
| `SelectionFill` | `=RGBA(56, 96, 178, 1)` |  |
| `X` | `=200` | placement from lab insert order; ignore as default evidence |
| `Y` | `=200` | placement from lab insert order; ignore as default evidence |

#### `ComboBox1` - `Classic/ComboBox@2.4.0`

- Path: `ComboBox1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `ChevronBackground` | `=RGBA(56, 96, 178, 1)` |  |
| `ChevronFill` | `=RGBA(255, 255, 255, 1)` |  |
| `ChevronHoverBackground` | `=ColorFade(RGBA(56, 96, 178, 1), -20%)` |  |
| `ChevronHoverFill` | `=RGBA(255, 255, 255, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverFill` | `=RGBA(186, 202, 226, 1)` |  |
| `PressedColor` | `=RGBA(255, 255, 255, 1)` |  |
| `PressedFill` | `=RGBA(0, 18, 107, 1)` |  |
| `SelectionColor` | `=RGBA(255, 255, 255, 1)` |  |
| `SelectionFill` | `=RGBA(56, 96, 178, 1)` |  |
| `X` | `=220` | placement from lab insert order; ignore as default evidence |
| `Y` | `=220` | placement from lab insert order; ignore as default evidence |

#### `DataTable1` - `DataTable@1.0.3`

- Path: `DataTable1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HeadingColor` | `=RGBA(255, 255, 255, 1)` |  |
| `HeadingFill` | `=RGBA(56, 96, 178, 1)` |  |
| `HeadingFont` | `=Font.'Open Sans'` |  |
| `HoverFill` | `=RGBA(186, 202, 226, .2)` |  |
| `SelectedFill` | `=RGBA(56, 96, 178, .2)` |  |
| `X` | `=240` | placement from lab insert order; ignore as default evidence |
| `Y` | `=240` | placement from lab insert order; ignore as default evidence |

#### `DatePicker2` - `Classic/DatePicker@2.6.0`

- Path: `DatePicker2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `IconBackground` | `=RGBA(56, 96, 178, 1)` |  |
| `IconFill` | `=RGBA(255, 255, 255, 1)` |  |
| `X` | `=260` | placement from lab insert order; ignore as default evidence |
| `Y` | `=260` | placement from lab insert order; ignore as default evidence |

#### `Checkbox1` - `Classic/CheckBox@2.1.0`

- Path: `Checkbox1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `CheckboxBorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `CheckmarkFill` | `=RGBA(0, 0, 0, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=280` | placement from lab insert order; ignore as default evidence |
| `Y` | `=280` | placement from lab insert order; ignore as default evidence |

#### `Radio2` - `Classic/Radio@2.3.0`

- Path: `Radio2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Items.Value` | `=Value` |  |
| `RadioBorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `RadioSelectionFill` | `=RGBA(0, 0, 0, 1)` |  |
| `X` | `=300` | placement from lab insert order; ignore as default evidence |
| `Y` | `=300` | placement from lab insert order; ignore as default evidence |

#### `Toggle2` - `Classic/Toggle@2.1.0`

- Path: `Toggle2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `TrueFill` | `=RGBA(56, 96, 178, 1)` |  |
| `X` | `=320` | placement from lab insert order; ignore as default evidence |
| `Y` | `=320` | placement from lab insert order; ignore as default evidence |

#### `Slider2` - `Classic/Slider@2.1.0`

- Path: `Slider2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `ValueFill` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=340` | placement from lab insert order; ignore as default evidence |
| `Y` | `=340` | placement from lab insert order; ignore as default evidence |

#### `Rating1` - `Rating@2.1.0`

- Path: `Rating1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `RatingFill` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=360` | placement from lab insert order; ignore as default evidence |
| `Y` | `=360` | placement from lab insert order; ignore as default evidence |

#### `Icon2` - `Classic/Icon@2.5.0`

- Path: `Icon2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Color` | `=RGBA(0, 18, 107, 1)` |  |
| `Icon` | `=Icon.Alarm` |  |
| `X` | `=380` | placement from lab insert order; ignore as default evidence |
| `Y` | `=380` | placement from lab insert order; ignore as default evidence |

### Modern fresh-control lab

#### `Container1` - `GroupContainer@1.5.0` - variant `ManualLayout`

- Path: `Container1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=40` | placement from lab insert order; ignore as default evidence |
| `Y` | `=40` | placement from lab insert order; ignore as default evidence |

#### `Container2` - `GroupContainer@1.5.0` - variant `AutoLayout`

- Path: `Container1 > Container2`
- Depth: `1`

| Property | Observed fresh value | Note |
|---|---|---|
| `LayoutAlignItems` | `=LayoutAlignItems.Center` |  |
| `LayoutDirection` | `=LayoutDirection.Horizontal` |  |
| `PaddingBottom` | `=8` |  |
| `PaddingLeft` | `=8` |  |
| `PaddingRight` | `=8` |  |
| `PaddingTop` | `=8` |  |

#### `Container3` - `GroupContainer@1.5.0` - variant `AutoLayout`

- Path: `Container1 > Container2 > Container3`
- Depth: `2`

| Property | Observed fresh value | Note |
|---|---|---|
| `LayoutAlignItems` | `=LayoutAlignItems.Center` |  |
| `LayoutDirection` | `=LayoutDirection.Vertical` |  |
| `LayoutMinHeight` | `=16` |  |
| `LayoutMinWidth` | `=16` |  |
| `PaddingBottom` | `=8` |  |
| `PaddingLeft` | `=8` |  |
| `PaddingRight` | `=8` |  |
| `PaddingTop` | `=8` |  |

#### `Container4` - `GroupContainer@1.5.0` - variant `GridLayout`

- Path: `Container1 > Container2 > Container3 > Container4`
- Depth: `3`

| Property | Observed fresh value | Note |
|---|---|---|
| `LayoutMinHeight` | `=16` |  |
| `LayoutMinWidth` | `=16` |  |

#### `Gallery1` - `Gallery@2.15.0` - variant `BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1`
- Depth: `4`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=168` |  |
| `Width` | `=468` |  |
| `X` | `=40` | placement from lab insert order; ignore as default evidence |
| `Y` | `=40` | placement from lab insert order; ignore as default evidence |

#### `Image1` - `Image@2.2.3`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1 > Image1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=72` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `RadiusBottomLeft` | `=8` |  |
| `RadiusBottomRight` | `=8` |  |
| `RadiusTopLeft` | `=8` |  |
| `RadiusTopRight` | `=8` |  |
| `Width` | `=72` |  |
| `Y` | `=(Parent.TemplateHeight / 2) - (Self.Height / 2)` | placement from lab insert order; ignore as default evidence |

#### `Title1` - `Label@2.5.1`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1 > Title1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Color` | `=RGBA(50, 49, 48, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `FontWeight` | `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)` |  |
| `Height` | `=Self.Size * 1.8` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=0` |  |
| `PaddingLeft` | `=0` |  |
| `PaddingRight` | `=0` |  |
| `PaddingTop` | `=0` |  |
| `Size` | `=14` |  |
| `Text` | `=ThisItem.SampleHeading` |  |
| `VerticalAlign` | `=VerticalAlign.Top` |  |
| `Width` | `=Parent.TemplateWidth - 173` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |
| `Y` | `=(Parent.TemplateHeight - (Self.Size * 1.8 + Subtitle1.Size * 1.8)) / 2` | placement from lab insert order; ignore as default evidence |

#### `Subtitle1` - `Label@2.5.1`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1 > Subtitle1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `FontWeight` | `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)` |  |
| `Height` | `=Self.Size * 1.8` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=0` |  |
| `PaddingLeft` | `=0` |  |
| `PaddingRight` | `=0` |  |
| `PaddingTop` | `=0` |  |
| `Size` | `=12` |  |
| `Text` | `=ThisItem.SampleText` |  |
| `VerticalAlign` | `=VerticalAlign.Top` |  |
| `Width` | `=Title1.Width` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |
| `Y` | `=Title1.Y + Title1.Height` | placement from lab insert order; ignore as default evidence |

#### `NextArrow1` - `Classic/Icon@2.5.0`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1 > NextArrow1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `AccessibleLabel` | `=Self.Tooltip` |  |
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Color` | `=RGBA(166, 166, 166, 1)` |  |
| `DisabledBorderColor` | `=RGBA(56, 56, 56, 1)` |  |
| `DisabledColor` | `=RGBA(119, 119, 119, 1)` |  |
| `Height` | `=50` |  |
| `Icon` | `=Icon.ChevronRight` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=16` |  |
| `PaddingLeft` | `=16` |  |
| `PaddingRight` | `=16` |  |
| `PaddingTop` | `=16` |  |
| `Tooltip` | `="View item details"` |  |
| `Width` | `=50` |  |
| `Y` | `=(Parent.TemplateHeight / 2) - (Self.Height / 2)` | placement from lab insert order; ignore as default evidence |

#### `Separator1` - `Rectangle@2.3.0`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1 > Separator1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Fill` | `=RGBA(255, 255, 255, 1)` |  |
| `Height` | `=8` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `Width` | `=Parent.TemplateWidth` |  |
| `Y` | `=Parent.TemplateHeight - Self.Height` | placement from lab insert order; ignore as default evidence |

#### `Rectangle1` - `Rectangle@2.3.0`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery1 > Rectangle1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Fill` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=Parent.TemplateHeight - Separator1.Height` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `Visible` | `=ThisItem.IsSelected` |  |
| `Width` | `=1` |  |

#### `Gallery2` - `Gallery@2.15.0` - variant `BrowseLayout_Horizontal_TwoTextOneImageVariant_ver5.0`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery2`
- Depth: `4`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=168` |  |
| `Width` | `=468` |  |
| `X` | `=40` | placement from lab insert order; ignore as default evidence |
| `Y` | `=40` | placement from lab insert order; ignore as default evidence |

#### `Image2` - `Image@2.2.3`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery2 > Image2`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=72` |  |
| `ImagePosition` | `=ImagePosition.Fill` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `RadiusBottomLeft` | `=8` |  |
| `RadiusBottomRight` | `=8` |  |
| `RadiusTopLeft` | `=8` |  |
| `RadiusTopRight` | `=8` |  |
| `Width` | `=Parent.TemplateWidth - 32` |  |
| `X` | `=(Parent.TemplateWidth / 2) - (Self.Width / 2)` | placement from lab insert order; ignore as default evidence |

#### `Title2` - `Label@2.5.1`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery2 > Title2`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Color` | `=RGBA(50, 49, 48, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `FontWeight` | `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)` |  |
| `Height` | `=Self.Size * 1.8` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=0` |  |
| `PaddingLeft` | `=0` |  |
| `PaddingRight` | `=0` |  |
| `PaddingTop` | `=0` |  |
| `Size` | `=14` |  |
| `Text` | `=ThisItem.SampleHeading` |  |
| `VerticalAlign` | `=VerticalAlign.Top` |  |
| `Width` | `=Parent.TemplateWidth - 64` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |
| `Y` | `=47` | placement from lab insert order; ignore as default evidence |

#### `Subtitle2` - `Label@2.5.1`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery2 > Subtitle2`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `FontWeight` | `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)` |  |
| `Height` | `=Self.Size * 1.8` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=0` |  |
| `PaddingLeft` | `=0` |  |
| `PaddingRight` | `=0` |  |
| `PaddingTop` | `=0` |  |
| `Size` | `=12` |  |
| `Text` | `=ThisItem.SampleText` |  |
| `VerticalAlign` | `=VerticalAlign.Top` |  |
| `Width` | `=Title2.Width` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |
| `Y` | `=51` | placement from lab insert order; ignore as default evidence |

#### `Gallery3` - `Gallery@2.15.0` - variant `BrowseLayout_Flexible_SocialFeed_ver5.0`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery3`
- Depth: `4`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=168` |  |
| `Width` | `=468` |  |
| `X` | `=40` | placement from lab insert order; ignore as default evidence |
| `Y` | `=40` | placement from lab insert order; ignore as default evidence |

#### `ProfileImage1` - `Image@2.2.3`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery3 > ProfileImage1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=12` |  |
| `ImagePosition` | `=ImagePosition.Fill` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `RadiusBottomLeft` | `=8` |  |
| `RadiusBottomRight` | `=8` |  |
| `RadiusTopLeft` | `=8` |  |
| `RadiusTopRight` | `=8` |  |
| `Width` | `=64` |  |

#### `Title3` - `Label@2.5.1`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery3 > Title3`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Color` | `=RGBA(50, 49, 48, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `FontWeight` | `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)` |  |
| `Height` | `=12` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=0` |  |
| `PaddingLeft` | `=0` |  |
| `PaddingRight` | `=0` |  |
| `PaddingTop` | `=0` |  |
| `Size` | `=14` |  |
| `Text` | `=ThisItem.SampleHeading` |  |
| `VerticalAlign` | `=VerticalAlign.Top` |  |
| `Width` | `=Parent.TemplateWidth - 112` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |

#### `Image3` - `Image@2.2.3`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery3 > Image3`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Height` | `=Min(Self.Width, Parent.TemplateHeight - 180)` |  |
| `ImagePosition` | `=ImagePosition.Fill` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `RadiusBottomLeft` | `=8` |  |
| `RadiusBottomRight` | `=8` |  |
| `RadiusTopLeft` | `=8` |  |
| `RadiusTopRight` | `=8` |  |
| `Width` | `=Parent.TemplateWidth - 32` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |
| `Y` | `=12` | placement from lab insert order; ignore as default evidence |

#### `Body1` - `Label@2.5.1`

- Path: `Container1 > Container2 > Container3 > Container4 > Gallery3 > Body1`
- Depth: `5`

| Property | Observed fresh value | Note |
|---|---|---|
| `AutoHeight` | `=true` |  |
| `BorderColor` | `=RGBA(0, 0, 0, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `FontWeight` | `=If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)` |  |
| `Height` | `=12` |  |
| `OnSelect` | `=Select(Parent)` |  |
| `PaddingBottom` | `=0` |  |
| `PaddingLeft` | `=0` |  |
| `PaddingRight` | `=0` |  |
| `PaddingTop` | `=0` |  |
| `Size` | `=12` |  |
| `Text` | `=ThisItem.SampleText` |  |
| `VerticalAlign` | `=VerticalAlign.Top` |  |
| `Width` | `=Parent.TemplateWidth - 32` |  |
| `X` | `=1` | placement from lab insert order; ignore as default evidence |

#### `Header1` - `Header@0.0.44`

- Path: `Container1 > Container2 > Container3 > Container4 > Header1`
- Depth: `4`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=40` | placement from lab insert order; ignore as default evidence |
| `Y` | `=40` | placement from lab insert order; ignore as default evidence |

#### `Form1` - `Form@2.4.4` - layout `Vertical`

- Path: `Form1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=60` | placement from lab insert order; ignore as default evidence |
| `Y` | `=60` | placement from lab insert order; ignore as default evidence |

#### `Button5` - `ModernButton@1.0.0`

- Path: `Button5`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=80` | placement from lab insert order; ignore as default evidence |
| `Y` | `=80` | placement from lab insert order; ignore as default evidence |

#### `TextInput2` - `ModernTextInput@1.1.0`

- Path: `TextInput2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=100` | placement from lab insert order; ignore as default evidence |
| `Y` | `=100` | placement from lab insert order; ignore as default evidence |

#### `NumberInput1` - `ModernNumberInput@1.1.0`

- Path: `NumberInput1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=120` | placement from lab insert order; ignore as default evidence |
| `Y` | `=120` | placement from lab insert order; ignore as default evidence |

#### `modernDropdown2` - `ModernDropdown@1.0.1`

- Path: `modernDropdown2`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=140` | placement from lab insert order; ignore as default evidence |
| `Y` | `=140` | placement from lab insert order; ignore as default evidence |

#### `Combobox3` - `ModernCombobox@1.1.0`

- Path: `Combobox3`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=160` | placement from lab insert order; ignore as default evidence |
| `Y` | `=160` | placement from lab insert order; ignore as default evidence |

#### `DatePicker1` - `ModernDatePicker@1.0.0`

- Path: `DatePicker1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=180` | placement from lab insert order; ignore as default evidence |
| `Y` | `=180` | placement from lab insert order; ignore as default evidence |

#### `CheckboxCanvas1` - `CheckBox@0.0.30`

- Path: `CheckboxCanvas1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=200` | placement from lab insert order; ignore as default evidence |
| `Y` | `=200` | placement from lab insert order; ignore as default evidence |

#### `Radio1` - `ModernRadio@1.0.0`

- Path: `Radio1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=220` | placement from lab insert order; ignore as default evidence |
| `Y` | `=220` | placement from lab insert order; ignore as default evidence |

#### `Toggle1` - `Toggle@1.1.5`

- Path: `Toggle1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=240` | placement from lab insert order; ignore as default evidence |
| `Y` | `=240` | placement from lab insert order; ignore as default evidence |

#### `PenInput1` - `PenInput@2.3.0`

- Path: `PenInput1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=260` | placement from lab insert order; ignore as default evidence |
| `Y` | `=260` | placement from lab insert order; ignore as default evidence |

#### `TabList1` - `ModernTabList@1.0.0`

- Path: `TabList1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=280` | placement from lab insert order; ignore as default evidence |
| `Y` | `=280` | placement from lab insert order; ignore as default evidence |

#### `Slider1` - `ModernSlider@1.0.0`

- Path: `Slider1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=300` | placement from lab insert order; ignore as default evidence |
| `Y` | `=300` | placement from lab insert order; ignore as default evidence |

#### `ListBox1` - `ListBox@2.2.0`

- Path: `ListBox1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverFill` | `=RGBA(186, 202, 226, 1)` |  |
| `Items.Value` | `=Value` |  |
| `PressedColor` | `=RGBA(255, 255, 255, 1)` |  |
| `PressedFill` | `=RGBA(0, 18, 107, 1)` |  |
| `SelectionColor` | `=RGBA(255, 255, 255, 1)` |  |
| `SelectionFill` | `=RGBA(56, 96, 178, 1)` |  |
| `X` | `=320` | placement from lab insert order; ignore as default evidence |
| `Y` | `=320` | placement from lab insert order; ignore as default evidence |

#### `RichTextEditor1` - `RichTextEditor@2.7.0`

- Path: `RichTextEditor1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=340` | placement from lab insert order; ignore as default evidence |
| `Y` | `=340` | placement from lab insert order; ignore as default evidence |

#### `Text1` - `ModernText@1.0.0`

- Path: `Text1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=360` | placement from lab insert order; ignore as default evidence |
| `Y` | `=360` | placement from lab insert order; ignore as default evidence |

#### `InformationButton1` - `ModernInformationButton@1.0.0`

- Path: `InformationButton1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=380` | placement from lab insert order; ignore as default evidence |
| `Y` | `=380` | placement from lab insert order; ignore as default evidence |

#### `Icon1` - `ModernIcon@1.1.0`

- Path: `Icon1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=400` | placement from lab insert order; ignore as default evidence |
| `Y` | `=400` | placement from lab insert order; ignore as default evidence |

#### `Avatar1` - `Avatar@1.0.40`

- Path: `Avatar1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=420` | placement from lab insert order; ignore as default evidence |
| `Y` | `=420` | placement from lab insert order; ignore as default evidence |

#### `BadgeCanvas1` - `Badge@0.0.24`

- Path: `BadgeCanvas1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=440` | placement from lab insert order; ignore as default evidence |
| `Y` | `=440` | placement from lab insert order; ignore as default evidence |

#### `Card1` - `ModernCard@1.2.0`

- Path: `Card1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=460` | placement from lab insert order; ignore as default evidence |
| `Y` | `=460` | placement from lab insert order; ignore as default evidence |

#### `Progress1` - `Progress@1.1.34`

- Path: `Progress1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=480` | placement from lab insert order; ignore as default evidence |
| `Y` | `=480` | placement from lab insert order; ignore as default evidence |

#### `Spinner1` - `Spinner@1.4.6`

- Path: `Spinner1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=500` | placement from lab insert order; ignore as default evidence |
| `Y` | `=500` | placement from lab insert order; ignore as default evidence |

#### `Link1` - `ModernLink@1.0.0`

- Path: `Link1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=520` | placement from lab insert order; ignore as default evidence |
| `Y` | `=520` | placement from lab insert order; ignore as default evidence |

#### `Timer1` - `Timer@2.1.0`

- Path: `Timer1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=ColorFade(Self.Fill, -15%)` |  |
| `Color` | `=RGBA(255, 255, 255, 1)` |  |
| `DisabledBorderColor` | `=ColorFade(Self.BorderColor, 70%)` |  |
| `DisabledColor` | `=ColorFade(Self.Fill, 90%)` |  |
| `DisabledFill` | `=ColorFade(Self.Fill, 70%)` |  |
| `Fill` | `=RGBA(56, 96, 178, 1)` |  |
| `Font` | `=Font.'Open Sans'` |  |
| `HoverBorderColor` | `=ColorFade(Self.BorderColor, 20%)` |  |
| `HoverColor` | `=RGBA(255, 255, 255, 1)` |  |
| `HoverFill` | `=ColorFade(RGBA(56, 96, 178, 1), -20%)` |  |
| `PressedBorderColor` | `=Self.Fill` |  |
| `PressedColor` | `=Self.Fill` |  |
| `PressedFill` | `=Self.Color` |  |
| `X` | `=540` | placement from lab insert order; ignore as default evidence |
| `Y` | `=540` | placement from lab insert order; ignore as default evidence |

#### `HtmlText1` - `HtmlViewer@2.1.0`

- Path: `HtmlText1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `Font` | `=Font.'Open Sans'` |  |
| `X` | `=560` | placement from lab insert order; ignore as default evidence |
| `Y` | `=560` | placement from lab insert order; ignore as default evidence |

#### `Image4` - `Image@2.2.3`

- Path: `Image4`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `BorderColor` | `=RGBA(0, 18, 107, 1)` |  |
| `X` | `=580` | placement from lab insert order; ignore as default evidence |
| `Y` | `=580` | placement from lab insert order; ignore as default evidence |

#### `PdfViewer1` - `PDFViewer@2.5.0`

- Path: `PdfViewer1`
- Depth: `0`

| Property | Observed fresh value | Note |
|---|---|---|
| `X` | `=600` | placement from lab insert order; ignore as default evidence |
| `Y` | `=288` | placement from lab insert order; ignore as default evidence |
