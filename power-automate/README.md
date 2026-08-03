# Power Automate Reference Pack

Last checked: 2026-08-03

Purpose: reusable, source-linked guidance for building future Power Automate cloud-flow guides and pasteable designer payloads without guessing trigger schemas, connector metadata, or dynamic-content shapes.

This is a separate reference pack from the Power Apps Bible. Power Apps and Power Automate overlap in app-triggered flows, but they fail in different ways and need different build rules.

## Files

- `power-automate-bible.md` - entry point for official docs, verified designer behavior, flow-building rules, and Training Tracker certificate-flow architecture.
- `designer-clipboard-format.md` - notes on Power Automate's copied trigger/action/container payloads, what has been verified to paste, and what still needs tenant-specific templates.

## Relationship To The Power Apps Reference Pack

- Power Apps reference: `../reference/`
- Power Automate reference: this folder.
- When a canvas app calls a flow, update both sides when needed:
  - Power Apps side: app data source, `.Run(...)` argument order, response object fields.
  - Power Automate side: trigger input order/internal keys, connector actions, response outputs, connection/run-only behavior.

## Rule

Do not invent Power Automate clipboard JSON, connector fields, or dynamic-content names. Use one of:

- Microsoft Learn pages linked in `power-automate-bible.md`.
- A real copied designer payload from the user's tenant.
- A generated payload pattern that has been pasted back into Power Automate and confirmed working.

Mark anything based on raw designer clipboard JSON as experimental unless it has been pasted successfully in the user's designer.
