# Power Apps Canvas Control Bible v0.1
A local, source-backed reference for Power Apps canvas controls, classic and modern. Built from the research session on 5 July 2026.
This is deliberately honest: it separates confirmed Microsoft documentation from inferred/common properties and known gaps. It is useful now, but it is not pretending Microsoft has published a perfect canonical metadata dump.
## Status
| Area | Status | Notes |
| --- | --- | --- |
| Control inventory | Strong | Modern and classic/legacy documented control pages are listed from Microsoft Learn and the MicrosoftDocs GitHub tree. |
| Property dictionary | Strong for shared/common properties | Core, text, accessibility, size/location, colour/border and behaviour properties are normalised. |
| Full per-control property lists | Partial | Text input and Button are captured in detail for both classic and modern. Other controls are inventoried and marked for extraction/verification. |
| Enums and dropdown values | Partial | Some enum families are known, but exact accepted values vary by control/version. These must be checked in the individual page or Studio. |
| Hidden/generated/runtime properties | Known gap | SearchItems, PowerBIIntegration and hostControl-style objects need live/tooling verification. |

## Source map
| Source | URL |
| --- | --- |
| Microsoft Learn, controls and properties in canvas apps | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/reference-properties |
| Microsoft Learn, modern controls reference | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-reference |
| Microsoft Learn, modern control updates | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-updates |
| Microsoft Learn, core properties | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-core |
| Microsoft Learn, text properties | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-text |
| Microsoft Learn, accessibility properties | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-accessibility |
| Microsoft Learn, size and location properties | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-size-location |
| Microsoft Learn, color and border properties | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/properties-color-border |
| Microsoft Learn, code view | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/code-view |
| Microsoft Learn, .pa.yaml source files | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/power-apps-yaml |
| Microsoft Docs GitHub repo, classic controls folder | https://github.com/MicrosoftDocs/powerapps-docs/tree/main/powerapps-docs/maker/canvas-apps/controls |
| Microsoft Docs GitHub repo, modern controls folder | https://github.com/MicrosoftDocs/powerapps-docs/tree/main/powerapps-docs/maker/canvas-apps/controls/modern-controls |
| Power Platform Skills issue 101, hidden/generated property gap | https://github.com/microsoft/power-platform-skills/issues/101 |
| Power Platform Skills issue 146, PowerBIIntegration host control gap | https://github.com/microsoft/power-platform-skills/issues/146 |
| Hardit Bhatia, The Power Addict modern control posts | https://thepoweraddict.com/text-input-everything-you-want-to-know-about-modern-control-21/ |

## Control inventory: modern controls
| Control | Page slug | Notes |
| --- | --- | --- |
| Avatar | modern-control-avatar | Modern control. Public summary page lists it. Exact complete property list should be harvested from the individual page/code view. |
| Badge | modern-control-badge | Modern control. Used for compact status/metadata labels. |
| Button | modern-control-button | Modern control. Full property list captured from research report. |
| Card | modern-control-card | Modern control. Separate page found in repo/docs. |
| Checkbox | modern-control-checkbox | Modern control. Boolean input. |
| Combobox | modern-control-combobox | Modern control. Choice picker with search, single or multiple selection depending configuration. |
| Copilot answer | modern-control-copilot-answer | Modern control. AI response display/control. Preview and tenant availability can vary. |
| Data Grid | modern-control-data-grid | Modern control. Page dated June 2026 in research. Uses Data Grid Column subcontrols. |
| Date picker | modern-control-date-picker | Modern control. Date input. |
| Dropdown | modern-control-dropdown | Modern control. Updated 2026 property naming noted in research. |
| Header | modern-control-header | Modern control. App/page header. |
| Icon | modern-control-icon | Modern control. Dedicated page found although not always listed on summary page. |
| Info button | modern-control-info-button | Modern control. Contextual help flyout/info. |
| Link | modern-control-link | Modern control. Hyperlink/clickable text. |
| Number input | modern-control-number-input | Modern control. Numeric input. |
| Progress bar | modern-control-progress-bar | Modern control. Progress/status display. |
| Radio group | modern-controls-radio-group | Modern control. Single selection from list. |
| Rating | modern-control-rating | Modern control. Dedicated page found although not always listed on summary page. |
| Slider | modern-control-slider | Modern control. Numeric range selector. |
| Spinner | modern-control-spinner | Modern control. Loading/progress indicator. |
| Stream | modern-control-stream | Modern control. Stream video/media integration. |
| Table | modern-control-table | Modern control. Preview status noted by Microsoft search snippet in research. |
| Tabs or tab list | modern-control-tabs-or-tabs-list | Modern control. Tabbed navigation/selection. |
| Text | modern-control-text | Modern control. Display text. |
| Text input | modern-control-text-input | Modern control. Full property list captured from research report. |
| Toggle | modern-control-toggle | Modern control. Boolean on/off input. |

## Control inventory: classic, legacy, structural and related objects
| Control/object | Page slug | Notes |
| --- | --- | --- |
| Add picture | control-add-picture | Image upload/capture style input. |
| Attachments | control-attachments | Dataverse/SharePoint attachment editing control. |
| Audio | control-audio-video | Media playback. |
| Barcode reader | control-barcodereader | Modern-ish scanner experience in canvas apps, device dependent. |
| Barcode scanner | control-new-barcode-scanner | Legacy scanner control, platform dependent. |
| Button | control-button | Classic action button. Full list captured. |
| Camera | control-camera | Device camera capture. Platform limitations apply. |
| Card | control-card | Form card structural object, not normal top-level insertable in the same sense as Button. |
| Check box | control-check-box | Classic boolean input. |
| Column chart | control-column-line-chart | Chart display. |
| Line chart | control-column-line-chart | Chart display. |
| Column | control-column | Data table column subcontrol/object. |
| Combo box | control-combo-box | Classic searchable choice picker. |
| Container | control-container | Manual layout container. |
| Data table | control-data-table | Legacy data table display/editing surface with known limitations. |
| Date Picker | control-date-picker | Classic date input. |
| Drop down | control-drop-down | Classic single selection list. |
| Export | control-export-import | Export data from collections. |
| Import | control-export-import | Import data into collections. |
| Display form | control-form-detail | Read-only form. |
| Edit form | control-form-detail | Editable form. |
| Gallery | control-gallery | Repeated layout/control template for records. |
| Grid container | control-grid-layout | Layout container. |
| Horizontal container | control-horizontal-container | Auto-layout container. |
| HTML text | control-html-text | HTML rendering control. |
| Image | control-image | Image display. |
| List Box | control-list-box | List selector. |
| Microphone | control-microphone | Audio recording input. |
| PDF viewer | control-pdf-viewer | PDF display. |
| Pen input | control-pen-input | Ink/drawing input. |
| Pie chart | control-pie-chart | Chart display. |
| Power BI tile | control-power-bi-tile | Power BI embed tile. |
| Radio | control-radio | Classic single selection. |
| Rating | control-rating | Classic rating input/display. |
| Rich text editor | control-richtexteditor | HTML rich text input. |
| Screen | control-screen | Canvas screen object. |
| Shape | control-shapes-icons | Visual shape. |
| Icon | control-shapes-icons | Classic icon. |
| Label | control-text-box | Classic display text label. |
| Slider | control-slider | Numeric range selector. |
| Text input | control-text-input | Classic text input. Full list captured. |
| Timer | control-timer | Timer for delayed/repeated actions. |
| Toggle | control-toggle | Classic boolean toggle. |
| Vertical container | control-vertical-container | Auto-layout container. |
| Video | control-audio-video | Media playback. |

## Reliability labels used in this Bible
| Label | Meaning |
| --- | --- |
| High | Directly listed in Microsoft docs or captured in the research report from a Microsoft page. |
| Medium | Supported by Microsoft docs/repo structure, but exact per-control applicability still needs verification. |
| Gap flagged | Control exists, but full property list has not yet been harvested. |
| Community/tooling gap | Known through community issue, MCP/tooling behaviour, or runtime host object behaviour. |
| Studio verification required | Must be checked by inserting the control into a current canvas app and using code view or exported .pa.yaml. |

## Master property dictionary
| Property | What it does | Applies to | Value/options notes | Source confidence |
| --- | --- | --- | --- | --- |
| Default | Initial value for an input/control before user interaction or reset. | Input controls, many classic and modern controls | Value type depends on control: text, number, Boolean, date, record, or table. | Official/shared |
| Text | Displayed text or current typed text, depending on control. | Labels, buttons, text input, text modern control, links | For Text input, Text is output/current value, Default is initial value. | Official/control-specific |
| Value | Current numeric/Boolean/rating value. | Slider, toggle, rating, timer-like and numeric controls | Often output/readable. Some controls use Checked or Selected instead. | Official/shared |
| Items | Table/list of records or values displayed by a selector/data control. | Gallery, dropdown, combo box, list box, radio, data table, table | Usually a table formula. Column names and Selected shape depend on control. | Official/shared |
| Selected | Currently selected record/item. | Gallery, dropdown, radio, table, data table | Shape depends on Items. Often read-only output. | Official/shared |
| SelectedItems | Selected records when multi-select is enabled. | Combo box and multi-select controls | Usually a table of records. | Official/control-specific |
| DefaultSelectedItems | Initial selected records for multi-select controls. | Combo box | Must match Items record shape. | Official/control-specific |
| DisplayFields | Fields shown in list/search results. | Combo box | Array/table of field names depending syntax. | Official/control-specific |
| SearchFields | Fields searched by user input. | Combo box | Array/table of field names. Delegation can matter. | Official/control-specific |
| SearchText | Current search text entered into searchable selector. | Combo box | Output style property, not always shown by tooling. | Needs Studio verification |
| SearchItems | Auto-generated searchable item table used internally by some combo/search controls. | Combo box and searchable controls | Community issue indicates describe_control may omit it. Treat as generated/hidden. | Community/tooling gap |
| OnSelect | Formula run when user selects/clicks/taps a control. | Button, gallery, icons, labels, many controls | Behaviour property. Can contain Power Fx actions. | Official/shared |
| OnChange | Formula run when a value changes. | Input controls | Modern Text input changed: fires on blur, with TriggerOutput controlling downstream updates. | Official/update |
| OnCheck | Formula run when a checkbox/toggle becomes true. | Classic check box/toggle | Some modern controls use OnChange instead. | Official/control-specific |
| OnUncheck | Formula run when a checkbox/toggle becomes false. | Classic check box/toggle | Some modern controls use OnChange instead. | Official/control-specific |
| OnTimerStart | Formula run when a timer starts. | Timer | Behaviour. | Official/control-specific |
| OnTimerEnd | Formula run when a timer ends. | Timer | Behaviour. | Official/control-specific |
| Reset | When true, resets control to default value. | Many classic inputs; not all modern controls | Modern controls often lack Reset property; use Reset(control) where available. | Official/community |
| DisplayMode | Interaction state of control. | Most interactive controls | Common values: Edit, View, Disabled. | Official/shared |
| Visible | Whether the control is shown. | Almost all controls | Boolean formula. Hidden controls usually do not receive input. | Official/shared |
| X | Horizontal position. | Most visual controls | Number in canvas units. | Official/size-location |
| Y | Vertical position. | Most visual controls | Number in canvas units. | Official/size-location |
| Width | Control width. | Most visual controls | Number in canvas units. | Official/size-location |
| Height | Control height. | Most visual controls | Number in canvas units. | Official/size-location |
| PaddingTop | Internal top spacing. | Many controls | Number. Modern controls use same split padding names. | Official/size-location |
| PaddingBottom | Internal bottom spacing. | Many controls | Number. | Official/size-location |
| PaddingLeft | Internal left spacing. | Many controls | Number. | Official/size-location |
| PaddingRight | Internal right spacing. | Many controls | Number. | Official/size-location |
| RadiusTopLeft | Top-left corner radius. | Buttons, inputs, modern controls | Modern updates replaced some BorderRadius use with per-corner radius. | Official/update |
| RadiusTopRight | Top-right corner radius. | Buttons, inputs, modern controls | Number. | Official/update |
| RadiusBottomLeft | Bottom-left corner radius. | Buttons, inputs, modern controls | Number. | Official/update |
| RadiusBottomRight | Bottom-right corner radius. | Buttons, inputs, modern controls | Number. | Official/update |
| BorderColor | Border colour. | Many visual controls | Colour formula or theme token depending control. | Official/color-border |
| BorderStyle | Border line style. | Many visual controls | Common values include Solid, Dashed, Dotted, None depending control/version. | Official/color-border |
| BorderThickness | Border width. | Many visual controls | Number. | Official/color-border |
| Fill | Background fill colour. | Many visual controls | Colour formula. | Official/color-border |
| Color | Text/foreground colour. | Textual controls, modern controls | Modern update renamed FontColor to Color. | Official/update |
| Font | Font family. | Textual controls | Text enum/name. | Official/text |
| Size | Text size. | Textual controls | Modern update renamed FontSize to Size. | Official/update |
| FontWeight | Weight of text. | Textual controls | Common values: Lighter, Normal, Semibold, Bold. | Official/text |
| Italic | Italic text. | Textual controls | Boolean. Modern update renamed FontItalic to Italic. | Official/update |
| Underline | Underlined text. | Textual controls | Boolean. Modern update renamed FontUnderline to Underline. | Official/update |
| Strikethrough | Strikethrough text. | Textual controls | Boolean. Modern update renamed FontStrikethrough to Strikethrough. | Official/update |
| Align | Horizontal text/content alignment. | Textual controls, buttons, inputs | Common values: Left, Center, Right, Justify depending control. | Official/text |
| VerticalAlign | Vertical text/content alignment. | Buttons/labels and some controls | Common values: Top, Middle, Bottom. | Official/text |
| LineHeight | Height of each text line. | Text input, labels, rich text-like controls | Number. | Official/control-specific |
| AccessibleLabel | Screen-reader label. | Most interactive/non-text controls | Required for accessibility if visible text is not enough. | Official/accessibility |
| Tooltip | Hover/help text. | Many controls | Can improve accessibility and usability. | Official/shared |
| TabIndex | Keyboard navigation order. | Interactive classic controls | Modern controls may differ. Values <= -1 can remove from tab order in classic docs. | Official/accessibility |
| ContentLanguage | Language tag for control content. | Textual controls and modern controls | Useful for screen readers/language handling. | Official/accessibility |
| FocusedBorderColor | Border colour when focused. | Classic controls | Classic styling property. Modern controls may not expose same property. | Official/color-border |
| FocusedBorderThickness | Border thickness when focused. | Classic controls | Classic styling property. | Official/color-border |
| HoverColor | Foreground colour on hover. | Classic buttons and inputs | Classic interaction styling. | Official/color-border |
| HoverFill | Background colour on hover. | Classic buttons and inputs | Classic interaction styling. | Official/color-border |
| HoverBorderColor | Border colour on hover. | Classic controls | Classic interaction styling. | Official/color-border |
| PressedColor | Foreground colour when pressed. | Classic buttons/icons | Classic interaction styling. | Official/color-border |
| PressedFill | Background when pressed. | Classic buttons/icons | Classic interaction styling. | Official/color-border |
| PressedBorderColor | Border colour when pressed. | Classic buttons/icons | Classic interaction styling. | Official/color-border |
| DisabledColor | Foreground colour when disabled. | Classic controls | Classic disabled styling. | Official/color-border |
| DisabledFill | Background when disabled. | Classic controls | Classic disabled styling. | Official/color-border |
| DisabledBorderColor | Border when disabled. | Classic controls | Classic disabled styling. | Official/color-border |
| Appearance | Modern visual style variant. | Modern controls | Enum-based after 2026 updates. Values vary by control, e.g. Primary/Secondary/Subtle/Transparent style families. Verify per control. | Official/update, verify |
| BasePaletteColor | Modern theme palette base colour. | Modern controls | Theme/palette value. Exact accepted values should be validated in Studio. | Official/modern |
| Icon | Icon name or icon value. | Classic Icon, modern Icon, modern Button, Badge maybe | Modern Icon page says Fluent icon library, approximately 180 icons. | Official/modern |
| IconStyle | Modern icon style. | Modern Button/Icon-like controls | Enum. Exact values vary and should be harvested from individual page. | Official/update |
| IconRotation | Rotation applied to icon. | Modern Button/Icon-like controls | Number/enum depending control. Verify. | Official/modern |
| Layout | Arrangement of icon/text or options. | Modern Button, radio, tabs, containers | Enum values vary by control. | Official/update |
| Type | Input type. | Modern Text input | Enum TextInputType. E.g. text/password/email/number style values should be verified from docs/Studio. | Official/control-specific |
| TriggerOutput | When Text input outputs updates to dependent formulas. | Modern Text input | Controls live vs delayed updates after 2026 behaviour changes. | Official/update |
| ValidationState | Validation visual state. | Modern inputs/dropdowns | Enum, typically None/Error/Success/Warning style. Verify exact values. | Official/modern |
| Required | Whether input is required. | Modern input controls | Boolean. Used for validation visuals, not always data enforcement alone. | Official/modern |
| Placeholder | Placeholder text. | Modern Text input and similar inputs | Modern equivalent to HintText in many cases. | Official/modern |
| HintText | Placeholder/hint text. | Classic Text input, dropdown/search controls | Classic text property. | Official/text |
| MaxLength | Maximum text length. | Text input controls | Number. 0 or blank semantics should be verified. | Official/control-specific |
| Mode | Control mode. | Classic Text input and others | For Text input: single-line, multi-line, password style options depending version. | Official/control-specific |
| Format | Data/text format. | Text input, date picker, numeric controls | Enum/control-specific. | Official/control-specific |
| Clear | Shows clear button. | Classic Text input | Boolean. | Official/control-specific |
| DelayOutput | Delay text output until user pauses typing. | Classic Text input | Boolean. Modern equivalent is not identical, see TriggerOutput. | Official/control-specific |
| EnableSpellCheck | Spellchecking. | Classic Text input | Boolean. Browser/platform dependent. | Official/control-specific |
| VirtualKeyboardMode | Mobile virtual keyboard preference. | Classic Text input | Enum/control-specific. | Official/control-specific |
| AutoDisableOnSelect | Temporarily disables button while OnSelect runs. | Classic Button | Boolean. Helps prevent double-submit. | Official/control-specific |
| Pressed | Whether a button/control is being pressed. | Classic Button and some controls | Output Boolean. | Official/control-specific |
| Start | Starts timer/media/camera behaviour depending control. | Timer, media controls | Control-specific. | Official/control-specific |
| Duration | Timer duration. | Timer | Milliseconds. | Official/control-specific |
| Repeat | Repeats timer. | Timer | Boolean. | Official/control-specific |
| AutoStart | Starts automatically when visible/screen opens. | Timer/media controls | Boolean. | Official/control-specific |
| AutoPause | Pauses media automatically. | Audio/video | Boolean. | Official/control-specific |
| Media | Media file/stream source. | Audio, Video, Image | Type varies. | Official/control-specific |
| Image | Image source. | Image, Add picture, Avatar | Media/image value. | Official/control-specific |
| Camera | Selected device camera index. | Camera control | Number/device dependent. | Official/control-specific |
| Photo | Captured camera/photo output. | Camera/Add picture | Media output. | Official/control-specific |
| Stream | Live camera/video stream. | Camera | Media stream output. | Official/control-specific |
| BarcodeType | Barcode type/symbology. | Barcode controls | Enum/control-specific. Device support varies. | Official/control-specific |
| DataSource | Connected data source. | Forms, galleries, data table, attachments | Table/data source reference. | Official/control-specific |
| Item | Current record. | Forms, cards, galleries | Record. | Official/control-specific |
| Updates | Record of changes to submit. | Edit form/Data card | Record. | Official/control-specific |
| Valid | Whether form/card data is valid. | Forms/cards | Boolean output. | Official/control-specific |
| Error | Current validation/data error. | Forms/cards | Text output. | Official/control-specific |
| ErrorKind | Kind/category of error. | Forms | Enum output. | Official/control-specific |
| SubmitForm | Function, not property. Submits an Edit form. | Forms | Include in Bible because form controls depend on it. | Official/function |
| ResetForm | Function, not property. Resets an Edit form. | Forms | Include in Bible because form controls depend on it. | Official/function |

## Confirmed full property maps
### Classic Text input
Captured from the classic Text input control page in the research report.
| Property |
| --- |
| Default |
| Text |
| AccessibleLabel |
| Align |
| BorderColor |
| BorderStyle |
| BorderThickness |
| Clear |
| Color |
| DelayOutput |
| DisplayMode |
| DisabledBorderColor |
| DisabledColor |
| DisabledFill |
| EnableSpellCheck |
| Fill |
| FocusedBorderColor |
| FocusedBorderThickness |
| Font |
| FontWeight |
| Format |
| Height |
| HintText |
| HoverBorderColor |
| HoverColor |
| HoverFill |
| Italic |
| LineHeight |
| MaxLength |
| Mode |
| OnChange |
| OnSelect |
| PaddingBottom |
| PaddingLeft |
| PaddingRight |
| PaddingTop |
| PressedBorderColor |
| PressedColor |
| PressedFill |
| RadiusBottomLeft |
| RadiusBottomRight |
| RadiusTopLeft |
| RadiusTopRight |
| Reset |
| Size |
| Strikethrough |
| TabIndex |
| Tooltip |
| Underline |
| VirtualKeyboardMode |
| Visible |
| Width |
| X |
| Y |

### Modern Text input
Captured from the modern Text input page and modern updates page in the research report.
| Property |
| --- |
| Default |
| Text |
| Placeholder |
| Visible |
| OnChange |
| OnSelect |
| Type |
| TriggerOutput |
| MaxLength |
| Required |
| ValidationState |
| DisplayMode |
| Align |
| X |
| Y |
| Width |
| Height |
| PaddingTop |
| PaddingBottom |
| PaddingLeft |
| PaddingRight |
| Appearance |
| BasePaletteColor |
| Font |
| Size |
| Color |
| FontWeight |
| Italic |
| Underline |
| Strikethrough |
| Fill |
| BorderColor |
| BorderStyle |
| BorderThickness |
| RadiusTopLeft |
| RadiusTopRight |
| RadiusBottomLeft |
| RadiusBottomRight |
| AccessibleLabel |
| ContentLanguage |

### Classic Button
Captured from the classic Button control page in the research report.
| Property |
| --- |
| OnSelect |
| Text |
| Align |
| AutoDisableOnSelect |
| BorderColor |
| BorderStyle |
| BorderThickness |
| Color |
| ContentLanguage |
| DisplayMode |
| DisabledBorderColor |
| DisabledColor |
| DisabledFill |
| FocusedBorderColor |
| FocusedBorderThickness |
| Fill |
| Font |
| FontWeight |
| Height |
| HoverBorderColor |
| HoverColor |
| HoverFill |
| Italic |
| PaddingBottom |
| PaddingLeft |
| PaddingRight |
| PaddingTop |
| Pressed |
| PressedBorderColor |
| PressedColor |
| PressedFill |
| RadiusBottomLeft |
| RadiusBottomRight |
| RadiusTopLeft |
| RadiusTopRight |
| Size |
| Strikethrough |
| TabIndex |
| Tooltip |
| Underline |
| VerticalAlign |
| Visible |
| Width |
| X |
| Y |

### Modern Button
Captured from the modern Button page and modern updates page in the research report.
| Property |
| --- |
| Text |
| Visible |
| OnSelect |
| DisplayMode |
| X |
| Y |
| Width |
| Height |
| Align |
| VerticalAlign |
| PaddingTop |
| PaddingBottom |
| PaddingLeft |
| PaddingRight |
| Appearance |
| BasePaletteColor |
| Icon |
| IconStyle |
| IconRotation |
| Layout |
| Font |
| Size |
| Color |
| FontWeight |
| Italic |
| Underline |
| Strikethrough |
| BorderColor |
| BorderStyle |
| BorderThickness |
| RadiusTopLeft |
| RadiusTopRight |
| RadiusBottomLeft |
| RadiusBottomRight |
| AccessibleLabel |
| Tooltip |
| ContentLanguage |

## Current per-control property matrix
This is the practical working matrix. Rows marked as gaps are not safe to treat as exhaustive yet.
| Family | Control | Property | Meaning | Confidence | Primary source |
| --- | --- | --- | --- | --- | --- |
| Modern | Avatar | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-avatar |
| Modern | Badge | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-badge |
| Modern | Button | Text | Displayed text or current typed text, depending on control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Visible | Whether the control is shown. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | OnSelect | Formula run when user selects/clicks/taps a control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | DisplayMode | Interaction state of control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | X | Horizontal position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Y | Vertical position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Width | Control width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Height | Control height. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Align | Horizontal text/content alignment. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | VerticalAlign | Vertical text/content alignment. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | PaddingTop | Internal top spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | PaddingBottom | Internal bottom spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | PaddingLeft | Internal left spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | PaddingRight | Internal right spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Appearance | Modern visual style variant. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | BasePaletteColor | Modern theme palette base colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Icon | Icon name or icon value. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | IconStyle | Modern icon style. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | IconRotation | Rotation applied to icon. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Layout | Arrangement of icon/text or options. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Font | Font family. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Size | Text size. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Color | Text/foreground colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | FontWeight | Weight of text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Italic | Italic text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Underline | Underlined text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Strikethrough | Strikethrough text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | BorderColor | Border colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | BorderStyle | Border line style. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | BorderThickness | Border width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | RadiusTopLeft | Top-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | RadiusTopRight | Top-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | RadiusBottomLeft | Bottom-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | RadiusBottomRight | Bottom-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | AccessibleLabel | Screen-reader label. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | Tooltip | Hover/help text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Button | ContentLanguage | Language tag for control content. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-button |
| Modern | Card | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-card |
| Modern | Checkbox | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-checkbox |
| Modern | Combobox | Items | Table/list of records or values displayed by a selector/data control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | DefaultSelectedItems | Initial selected records for multi-select controls. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | Selected | Currently selected record/item. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | SelectedItems | Selected records when multi-select is enabled. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | DisplayFields | Fields shown in list/search results. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | SearchFields | Fields searched by user input. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | SearchText | Current search text entered into searchable selector. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | ValidationState | Validation visual state. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Combobox | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-combobox |
| Modern | Copilot answer | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-copilot-answer |
| Modern | Data Grid | Items | Table/list of records or values displayed by a selector/data control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | Selected | Currently selected record/item. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | OnSelect | Formula run when user selects/clicks/taps a control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | ReflowBehavior | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Data Grid | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-data-grid |
| Modern | Date picker | SelectedDate | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | DefaultSelectedDate | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | MinDate | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | MaxDate | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | Format | Data/text format. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | ValidationState | Validation visual state. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Date picker | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-date-picker |
| Modern | Dropdown | Items | Table/list of records or values displayed by a selector/data control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Default | Initial value for an input/control before user interaction or reset. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Selected | Currently selected record/item. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | ValidationState | Validation visual state. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Dropdown | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-dropdown |
| Modern | Header | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-header |
| Modern | Icon | Icon | Icon name or icon value. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | IconStyle | Modern icon style. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | IconRotation | Rotation applied to icon. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | Color | Text/foreground colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | Tooltip | Hover/help text. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Icon | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-icon |
| Modern | Info button | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-info-button |
| Modern | Link | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-link |
| Modern | Number input | Value | Current numeric/Boolean/rating value. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Default | Initial value for an input/control before user interaction or reset. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Min | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Max | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Step | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | ValidationState | Validation visual state. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Number input | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-number-input |
| Modern | Progress bar | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-progress-bar |
| Modern | Radio group | Items | Table/list of records or values displayed by a selector/data control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Selected | Currently selected record/item. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Default | Initial value for an input/control before user interaction or reset. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Layout | Arrangement of icon/text or options. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | ValidationState | Validation visual state. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Radio group | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-controls-radio-group |
| Modern | Rating | Value | Current numeric/Boolean/rating value. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Default | Initial value for an input/control before user interaction or reset. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Max | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Precision | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Icon | Icon name or icon value. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Rating | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-rating |
| Modern | Slider | Value | Current numeric/Boolean/rating value. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Default | Initial value for an input/control before user interaction or reset. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Min | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Max | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Step | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Slider | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-slider |
| Modern | Spinner | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-spinner |
| Modern | Stream | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-stream |
| Modern | Table | Items | Table/list of records or values displayed by a selector/data control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | Selected | Currently selected record/item. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | OnSelect | Formula run when user selects/clicks/taps a control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | ReflowBehavior | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Table | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-table |
| Modern | Tabs or tab list | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-tabs-or-tabs-list |
| Modern | Text | Text | Displayed text or current typed text, depending on control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Size | Text size. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Color | Text/foreground colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Font | Font family. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | FontWeight | Weight of text. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Italic | Italic text. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Underline | Underlined text. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Strikethrough | Strikethrough text. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Align | Horizontal text/content alignment. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text |
| Modern | Text input | Default | Initial value for an input/control before user interaction or reset. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Text | Displayed text or current typed text, depending on control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Placeholder | Placeholder text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Visible | Whether the control is shown. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | OnChange | Formula run when a value changes. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | OnSelect | Formula run when user selects/clicks/taps a control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Type | Input type. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | TriggerOutput | When Text input outputs updates to dependent formulas. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | MaxLength | Maximum text length. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Required | Whether input is required. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | ValidationState | Validation visual state. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | DisplayMode | Interaction state of control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Align | Horizontal text/content alignment. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | X | Horizontal position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Y | Vertical position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Width | Control width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Height | Control height. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | PaddingTop | Internal top spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | PaddingBottom | Internal bottom spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | PaddingLeft | Internal left spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | PaddingRight | Internal right spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Appearance | Modern visual style variant. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | BasePaletteColor | Modern theme palette base colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Font | Font family. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Size | Text size. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Color | Text/foreground colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | FontWeight | Weight of text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Italic | Italic text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Underline | Underlined text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Strikethrough | Strikethrough text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | Fill | Background fill colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | BorderColor | Border colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | BorderStyle | Border line style. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | BorderThickness | Border width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | RadiusTopLeft | Top-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | RadiusTopRight | Top-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | RadiusBottomLeft | Bottom-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | RadiusBottomRight | Bottom-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | AccessibleLabel | Screen-reader label. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Text input | ContentLanguage | Language tag for control content. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-text-input |
| Modern | Toggle | Checked | Control-specific property. Definition should be verified against the current control page or Studio code view. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | Default | Initial value for an input/control before user interaction or reset. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | OnChange | Formula run when a value changes. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | DisplayMode | Interaction state of control. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | Visible | Whether the control is shown. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | X | Horizontal position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | Y | Vertical position. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | Width | Control width. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | Height | Control height. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | AccessibleLabel | Screen-reader label. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | ContentLanguage | Language tag for control content. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | Appearance | Modern visual style variant. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Modern | Toggle | BasePaletteColor | Modern theme palette base colour. | Medium, needs per-control verification | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-control-toggle |
| Classic | Add picture | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-add-picture |
| Classic | Attachments | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-attachments |
| Classic | Audio | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-audio-video |
| Classic | Barcode reader | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-barcodereader |
| Classic | Barcode scanner | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-new-barcode-scanner |
| Classic | Button | OnSelect | Formula run when user selects/clicks/taps a control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Text | Displayed text or current typed text, depending on control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Align | Horizontal text/content alignment. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | AutoDisableOnSelect | Temporarily disables button while OnSelect runs. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | BorderColor | Border colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | BorderStyle | Border line style. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | BorderThickness | Border width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Color | Text/foreground colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | ContentLanguage | Language tag for control content. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | DisplayMode | Interaction state of control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | DisabledBorderColor | Border when disabled. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | DisabledColor | Foreground colour when disabled. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | DisabledFill | Background when disabled. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | FocusedBorderColor | Border colour when focused. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | FocusedBorderThickness | Border thickness when focused. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Fill | Background fill colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Font | Font family. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | FontWeight | Weight of text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Height | Control height. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | HoverBorderColor | Border colour on hover. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | HoverColor | Foreground colour on hover. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | HoverFill | Background colour on hover. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Italic | Italic text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PaddingBottom | Internal bottom spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PaddingLeft | Internal left spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PaddingRight | Internal right spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PaddingTop | Internal top spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Pressed | Whether a button/control is being pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PressedBorderColor | Border colour when pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PressedColor | Foreground colour when pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | PressedFill | Background when pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | RadiusBottomLeft | Bottom-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | RadiusBottomRight | Bottom-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | RadiusTopLeft | Top-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | RadiusTopRight | Top-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Size | Text size. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Strikethrough | Strikethrough text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | TabIndex | Keyboard navigation order. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Tooltip | Hover/help text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Underline | Underlined text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | VerticalAlign | Vertical text/content alignment. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Visible | Whether the control is shown. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Width | Control width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | X | Horizontal position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Button | Y | Vertical position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-button |
| Classic | Camera | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-camera |
| Classic | Card | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-card |
| Classic | Check box | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-check-box |
| Classic | Column chart | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-column-line-chart |
| Classic | Line chart | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-column-line-chart |
| Classic | Column | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-column |
| Classic | Combo box | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-combo-box |
| Classic | Container | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-container |
| Classic | Data table | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-data-table |
| Classic | Date Picker | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-date-picker |
| Classic | Drop down | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-drop-down |
| Classic | Export | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-export-import |
| Classic | Import | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-export-import |
| Classic | Display form | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-form-detail |
| Classic | Edit form | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-form-detail |
| Classic | Gallery | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-gallery |
| Classic | Grid container | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-grid-layout |
| Classic | Horizontal container | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-horizontal-container |
| Classic | HTML text | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-html-text |
| Classic | Image | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-image |
| Classic | List Box | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-list-box |
| Classic | Microphone | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-microphone |
| Classic | PDF viewer | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-pdf-viewer |
| Classic | Pen input | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-pen-input |
| Classic | Pie chart | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-pie-chart |
| Classic | Power BI tile | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-power-bi-tile |
| Classic | Radio | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-radio |
| Classic | Rating | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-rating |
| Classic | Rich text editor | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-richtexteditor |
| Classic | Screen | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-screen |
| Classic | Shape | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-shapes-icons |
| Classic | Icon | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-shapes-icons |
| Classic | Label | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-box |
| Classic | Slider | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-slider |
| Classic | Text input | Default | Initial value for an input/control before user interaction or reset. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Text | Displayed text or current typed text, depending on control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | AccessibleLabel | Screen-reader label. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Align | Horizontal text/content alignment. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | BorderColor | Border colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | BorderStyle | Border line style. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | BorderThickness | Border width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Clear | Shows clear button. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Color | Text/foreground colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | DelayOutput | Delay text output until user pauses typing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | DisplayMode | Interaction state of control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | DisabledBorderColor | Border when disabled. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | DisabledColor | Foreground colour when disabled. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | DisabledFill | Background when disabled. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | EnableSpellCheck | Spellchecking. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Fill | Background fill colour. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | FocusedBorderColor | Border colour when focused. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | FocusedBorderThickness | Border thickness when focused. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Font | Font family. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | FontWeight | Weight of text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Format | Data/text format. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Height | Control height. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | HintText | Placeholder/hint text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | HoverBorderColor | Border colour on hover. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | HoverColor | Foreground colour on hover. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | HoverFill | Background colour on hover. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Italic | Italic text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | LineHeight | Height of each text line. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | MaxLength | Maximum text length. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Mode | Control mode. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | OnChange | Formula run when a value changes. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | OnSelect | Formula run when user selects/clicks/taps a control. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PaddingBottom | Internal bottom spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PaddingLeft | Internal left spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PaddingRight | Internal right spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PaddingTop | Internal top spacing. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PressedBorderColor | Border colour when pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PressedColor | Foreground colour when pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | PressedFill | Background when pressed. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | RadiusBottomLeft | Bottom-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | RadiusBottomRight | Bottom-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | RadiusTopLeft | Top-left corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | RadiusTopRight | Top-right corner radius. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Reset | When true, resets control to default value. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Size | Text size. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Strikethrough | Strikethrough text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | TabIndex | Keyboard navigation order. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Tooltip | Hover/help text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Underline | Underlined text. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | VirtualKeyboardMode | Mobile virtual keyboard preference. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Visible | Whether the control is shown. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Width | Control width. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | X | Horizontal position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Text input | Y | Vertical position. | High | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input |
| Classic | Timer | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-timer |
| Classic | Toggle | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-toggle |
| Classic | Vertical container | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-vertical-container |
| Classic | Video | PROPERTY SET NOT YET FULLY HARVESTED | Individual Microsoft page exists or is inferred from docs tree, but exact property list needs extraction from Learn/GitHub and Studio code view. | Gap flagged | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-audio-video |

## Known gaps and traps
| Gap | Why it matters | How to verify/fill it |
| --- | --- | --- |
| Modern controls summary is not a complete index | Research found Icon and Rating dedicated pages even though the summary list can omit them. | Use the MicrosoftDocs repo tree as the inventory, not only the Learn summary page. |
| Shared property pages are separate from control pages | A control page may not make every shared property obvious. | Join control pages with core, text, accessibility, size/location and colour/border property pages. |
| Modern 2026 property renames | Older blogs/screenshots may use names such as FontColor, FontSize, FontItalic, BorderRadius. | Map old names to Color, Size, Italic, Radius* etc using modern-control-updates. |
| Modern Text input OnChange behaviour changed | Older assumptions about per-keystroke OnChange can be wrong. | Use TriggerOutput and test in Studio. |
| SearchItems and generated properties | Tooling issue reports hidden/generated properties not exposed by describe_control. | Export .pa.yaml and compare Studio code view against authoring tooling. |
| PowerBIIntegration host control | Runtime-injected object, not normal insertable control, can break offline compiler schema. | Keep runtime/host controls in a separate section. |
| Custom components | Properties are maker-defined, so there is no universal list. | Document component schema and each component separately from built-in controls. |
| Preview/tenant-gated controls | Controls such as Copilot-related or table/grid variants can vary by environment. | Record environment, Studio version, feature flags and tenant settings. |

## Recommended harvesting workflow
Use this workflow to turn v0.1 into a genuinely brutal local knowledge base.
| Step | Action | Output |
| --- | --- | --- |
| 1 | Clone or download MicrosoftDocs/powerapps-docs controls folder and modern-controls subfolder. | Local markdown source cache. |
| 2 | Parse every markdown page for Properties, Key properties, Additional properties and Applies to tables. | Raw property rows. |
| 3 | Merge shared property pages into every control where the page says the property applies. | Normalised property matrix. |
| 4 | Insert every control into a blank canvas app, open Code view, copy YAML, then export .msapp/.pa.yaml. | Studio-observed property baseline. |
| 5 | Compare docs properties vs Studio properties vs .pa.yaml. | Gap report: missing, renamed, hidden, generated, runtime-only. |
| 6 | Add community/tooling issues as annotations only, not as official truth. | Confidence notes. |
| 7 | Regenerate Markdown, CSV and optional DOCX monthly or before major builds. | Versioned local Bible. |

## Copy/paste prompt for Claude or Codex to continue the extraction
Use this as a build prompt if you want an agent to complete the harvester against a local clone:
```text
Build a Power Apps canvas control documentation harvester. Use the local MicrosoftDocs/powerapps-docs repository. Parse powerapps-docs/maker/canvas-apps/controls and controls/modern-controls. For every markdown file that represents a control, extract control name, classic/modern family, page path, description, key properties, additional properties, enum/value notes, deprecation/preview notes, and source line references where possible. Then parse shared property pages properties-core, properties-text, properties-accessibility, properties-size-location, and properties-color-border, and join shared properties to controls where the docs say they apply. Emit powerapps_controls.json, powerapps_properties.csv, gap_report.md, and bible.md. Mark each property confidence as direct, shared-inferred, community, runtime-only, or needs-studio-verification. Do not invent missing enum values.
```

## Version notes
v0.1 is a grounded starter Bible, not a final canonical dump. It prioritises truthfulness over fake completeness. The next version should automate extraction from the docs repository and then validate by Studio Code View.
