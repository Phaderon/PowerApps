# powerappsui.com Component Reference

Source: https://www.powerappsui.com/components — MIT-licensed open-source Power Apps component library. YAML captured verbatim (licensed for reuse); documentation notes below are original summaries, not copies of the site's text.

Each component has its own file: `<slug>.md`, containing the full component YAML plus condensed original notes on properties and behavior.

## Bible Audit (2026-07-25)

Every component's YAML was scrubbed against `../known-bad-patterns.md` and `../verified-control-reference.md` after capture — this is copy-paste-from-a-website YAML, not hand-authored against this Bible, so it was audited rather than trusted. Most files with fixes or unresolved risk have their own "Bible Audit" section; summary:

- **Bare `Text: =` (21 sites, 3 files):** fixed to `Text: =""`.
- **Bare `PropName: =` on other properties (new pattern, not previously in the Bible — same defect class as `Text: =` but not limited to it; now documented in `known-bad-patterns.md`):** found and fixed in 13 files — mostly component `Event` custom-property `Default`s, plus a few real control properties (`OnSelect`, `Height`, `Width`, `LayoutMaxHeight`/`LayoutMaxWidth`). All 23 files now parse as syntactically valid YAML (verified with a YAML parser, not just visual inspection).
- **`Set(varName, Blank())` (known-bad Bible pattern):** fixed where the variable was clearly Text-typed (`activity-timeline.md`, `navigation-menu.md`'s `_navOpenMenu`). Left flagged, not guessed, where Record- or Date-typed (`navigation-menu.md`'s `_navSelectedItem`, `data-table.md`, `date-picker.md`) — a wrong guessed shape risks a worse error than the one being avoided.
- **`GroupContainer` missing `DropShadow` (known-bad Bible pattern — defaults ON when unset):** fixed on 13 clearly-structural containers in `activity-timeline.md`. Left flagged, not auto-fixed, on 5 card/popover-shaped containers (`kpi-cards.md`, `date-picker.md`, `file-upload.md`, `loading-overlay.md`) where a shadow may be the intended design.
- **`LayoutOverflowX` (Bible's own "Unverified" section — speculated, never live-confirmed):** flagged in `data-table.md`, `breadcrumbs.md`, `chips.md`. All three are on the correct `AutoLayout` variant (not the confirmed `LayoutOverflowY`-on-ManualLayout bug), so the remaining risk is only "might not be formula-bar-authorable at all."
- **`ModernCombobox` (activity-timeline.md):** checked clean against every documented Bible trap (no invalid `FontWeight`/`Appearance`, correct `DefaultSelectedItems`/`ItemDisplayText`, no `Reset()` call).
- **Checked and clean everywhere:** no missing `Variant:` on any `GroupContainer`/`Gallery`, no blacklisted controls (`ModernHeader`, `Copilot answer`, `ModernCard`, `ModernTabList`), no stale `Image@2.2.x`, no `ModernDatePicker.SelectedDate`.
- **Literal middle-dot separators in Power Fx strings:** replaced remaining literal `·` formula separators with `Char(183)` to match the Training Tracker/Power Fx string rule.
- **Component-scoped state variables** (the underscore-prefixed/`var`-prefixed globals each component uses, e.g. `_navOpenMenu`, `varCT_SelectedItem`): these are real app-global `Set()` variables namespaced by convention, not truly component-local — checked for name collisions across all 23 components and found none (the only repeated short names are `With()`-scoped locals, which are safely lexically scoped). Still worth a quick grep against your app's existing globals before pasting a second component that reuses a generic-sounding name.

## Data Display & Visualization

- [Activity Timeline](activity-timeline.md) (`activity-timeline`) — filterable vertical audit-trail log with self-sizing cards and an email-style sub-detail panel.
- [Bar List](bar-list.md) (`bar-list`) — ranked horizontal bar rows with palette color cycling, native controls only, no SVG.
- [Line Chart](line-chart.md) (`line-chart`) — single-series animated SVG line chart with smooth Bézier curves and gradient area fill.
- [Stacked Bar Chart](bar-chart.md) (`bar-chart`) — animated SVG 2-series stacked bar chart with auto-scaling Y-axis.
- [KPI Cards](kpi-cards.md) (`kpi-cards`) — responsive stat cards in 5 style variants with optional sparklines and trend badges.
- [Pie Chart](pie-chart.md) (`pie-chart`) — animated SVG pie/donut chart with legend and percentage labels.
- [Heatmap](heatmap.md) (`heatmap`) — SVG day-of-week × hour intensity grid for activity/usage patterns.
- [Data Table](data-table.md) (`data-table`) — table/card/list view switcher with context menus, status/priority pills, and progress bars.

## Form Controls & Input

- [Date Picker (Calendar)](date-picker.md) (`date-picker`) — Material Design 3 calendar with single/range/multi-select, weekend blocking, and built-in US federal holidays.
- [Segmented Control](segmented-control.md) (`segmented-control`) — gallery-driven exclusive-choice control with text/icon/both display modes.
- [Chips](chips.md) (`chips`) — stateless input/filter/choice chip group; host app owns selection state via `UpdateIf`.
- [File Upload](file-upload.md) (`file-upload`) — SharePoint-targeted file upload built on the native Attachments control, with type/size/count validation.

## Navigation

- [Sidebar](sidebar.md) (`sidebar`) — collapsible left nav with parent/child tree, badges, and app-scoped expand state.
- [Navigation Menu](navigation-menu.md) (`navigation-menu`) — horizontal top bar with 1- or 2-column mega-menu dropdowns.
- [Breadcrumbs](breadcrumbs.md) (`breadcrumbs`) — 5-slot breadcrumb trail with pixel-perfect label widths and smart ellipsis collapse.
- [Bottom Navigation Bar](bottom-navigation-bar.md) (`bottom-navigation-bar`) — mobile tab bar with 4 active-indicator styles and 3 label modes.

## Feedback & Overlays

- [Loading Screen](loading-screen.md) (`loading-screen`) — full-screen branded splash with animated ring, step messages, and a minimum-display-time gate.
- [Loading Overlay](loading-overlay.md) (`loading-overlay`) — full-screen blurred-backdrop overlay with a native spinner, toggled via `Visible`.
- [Dialog](dialog.md) (`dialog`) — modal with backdrop blur supporting Alert/Confirmation/Form types and a dynamic button table.
- [Badge](badge.md) (`badge`) — notification bell with auto-sizing count pill and pulse animation.

## Other

- [Stepper](stepper.md) (`stepper`) — multi-step progress indicator with Bar/Step types and 3 density levels.
- [Floating Action Button](floating-action-button.md) (`floating-action-button`) — Material Design 3 FAB with an optional speed-dial menu.
- [Photo Upload](photo-upload.md) (`photo-upload`) — two-section photo capture grid with a self-contained in-component camera overlay.
