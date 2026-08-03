# Designer Clipboard Format Notes

Last checked: 2026-08-03

## Status

Experimental but useful. The Power Automate new designer officially supports copying and pasting triggers/actions/containers. Microsoft does not document the raw clipboard JSON as a stable authoring contract, so generated payloads must be paste-tested.

Official designer copy/paste docs:

- https://learn.microsoft.com/en-us/power-automate/flows-designer

## Confirmed Working

Generated `Power Apps (V2)` trigger payloads pasted successfully in the user's Power Automate designer:

- `TT - Save Certificate Library TEST` trigger with 11 inputs.
- `TT - Email Certificate Library TEST` trigger with 3 inputs.
- `Initialize variable` payloads for `varSuccess` Boolean and `varMessage` String are exposed as confirmed copy buttons in the migration guide.

These were added as copy buttons on:

- `../training-tracker/certificate-library-migration.html`

## Observed Payload Shapes

### Trigger Or Action Payload

Typical top-level keys:

```json
{
  "nodeId": "...",
  "nodeData": {},
  "nodeTokenData": {},
  "nodeOperationInfo": {},
  "nodeConnectionData": null,
  "isScopeNode": false,
  "mslaNode": true
}
```

### Condition Container Payload

Copied Conditions can be much smaller and use `serializedValue`:

```json
{
  "nodeId": "Condition",
  "serializedValue": {
    "type": "If",
    "expression": {},
    "actions": {},
    "else": {
      "actions": {}
    },
    "runAfter": {}
  },
  "allConnectionData": {},
  "staticResults": {},
  "isScopeNode": true,
  "mslaNode": true
}
```

This suggests Conditions, Scopes, and loops may be easier to generate than connector actions, but fake dynamic tokens in copied test Conditions should not be reused blindly.

## Captured Local Templates

The user provided local copied payload files with trailing newline characters in their filenames:

- `/var/home/Phaderon/Initialize variable - Boolean\n`
- `/var/home/Phaderon/Initialize variable - String\n`
- `/var/home/Phaderon/Respond to a PowerApp or flow\n`
- `/var/home/Phaderon/Condition container\n`

These confirmed the basic payload shapes. Future cleanup can move normalized examples into this folder if they are useful, but do not publish raw tenant-specific connector IDs without reviewing them first.

## Generation Rules

- Prefer generating small pasteable chunks over one giant flow until each connector family has been tested.
- Preserve trigger input order once Power Apps formulas depend on `.Run(...)`.
- Prefer dynamic-content picker instructions over raw `triggerBody()['text_2']` expressions in human-facing guide steps.
- Mark generated clipboard buttons as experimental unless the exact button has been pasted successfully.
- After a payload is proven, record:
  - source template action,
  - target action generated,
  - paste result,
  - any fields Power Automate required the user to reselect.

## Current Gap

No real SharePoint or Outlook connector action templates have been captured from the target tenant yet. Do not claim full-flow paste generation is ready until those are captured and tested.
