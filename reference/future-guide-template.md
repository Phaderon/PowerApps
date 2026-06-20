# Future Guide Template

Last checked: 2026-06-20

Use this structure for new app guides.

## Folder

```text
new-app-guide/
  index.html
```

## Required Guide Sections

1. Version panel
   - Current version.
   - Last checked date.
   - Known tenant/editor assumptions.

2. Overview
   - What the app does.
   - Who uses it.
   - What problem it solves.

3. Data model
   - SharePoint lists or Dataverse tables.
   - Required columns.
   - Column types and exact internal/display names where known.

4. App setup
   - Canvas app type.
   - Data connections.
   - Theme/colors.
   - App-level formulas.

5. Screens
   - Purpose.
   - Controls table.
   - Formulas.
   - Validation notes.

6. Critical technical notes
   - Control/property traps.
   - Connector casing traps.
   - SharePoint field-shape traps.

7. Final audit checklist
   - Run `python3 tools/audit-guide.py guide-folder/index.html`.
   - Run `git diff --check`.
   - Browser preview.
   - Responsive check.
   - Copy button check.

## Control Table Columns

Use this table shape:

```html
<table>
<thead>
<tr>
<th>Control</th>
<th>Type</th>
<th>Key properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>txtExample</td>
<td>Text input (modern)</td>
<td>X=32,Y=120,W=400,H=40, Placeholder=<code>"Enter text"</code>, Text: read with <code>txtExample.Text</code></td>
</tr>
</tbody>
</table>
```

Rules:

- Never omit modern/classic from control type where both families exist.
- Do not write long inline paragraphs for controls when a table is clearer.
- Use code tags for formulas, enum values, and exact strings.
- If a property is unverified, do not include it as an instruction.

## Landing Page Card Template

```html
<a class="guide-card" href="new-guide/">
  <div class="guide-top">
    <span class="guide-kicker">Draft</span>
    <h2>New Guide Name</h2>
    <p>Short app purpose, user group, and data source summary.</p>
  </div>
  <div>
    <div class="guide-meta">
      <span class="pill">Canvas app</span>
      <span class="pill">SharePoint lists</span>
      <span class="pill">Reference checked</span>
    </div>
    <span class="open-row">Open guide <span aria-hidden="true">→</span></span>
  </div>
</a>
```

