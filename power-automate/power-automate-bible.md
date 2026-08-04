# Power Automate Bible

Last checked: 2026-08-03

## Purpose

This is the Power Automate companion to the Power Apps Bible. Keep it separate from Power Apps control/YAML guidance. Use it for cloud flows, Power Apps-triggered flows, SharePoint/Outlook actions, designer copy-paste payloads, and flow migration/security patterns.

## Official Sources

- Cloud flows designer, including Code View and copy/paste actions:
  - https://learn.microsoft.com/en-us/power-automate/flows-designer
- Export/import non-solution flow packages:
  - https://learn.microsoft.com/en-us/power-automate/export-import-flow-non-solution
- Export solution-aware cloud flows:
  - https://learn.microsoft.com/en-us/power-automate/export-flow-solution
- Work with cloud flows using code:
  - https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code
- Connection references:
  - https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference
- Share cloud flows and run-only/connection behavior:
  - https://learn.microsoft.com/en-us/power-automate/create-team-flows
  - https://learn.microsoft.com/en-us/power-automate/guide-to-cloud-flow-sharing-permissions
- Dynamic content missing from previous steps:
  - https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/flow-creation/dynamic-content-picker-missing-dynamic-content-from-previous-steps
- Workflow definition language and expressions:
  - https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-schema
  - https://learn.microsoft.com/en-us/azure/logic-apps/expression-functions-reference

## Verified Rules From Training Tracker

### Power Apps (V2) Trigger Inputs

The new designer copies the `Power Apps (V2)` trigger as a JSON clipboard payload containing:

- `nodeId`
- `nodeData.nodeInputs.parameterGroups.default.parameters`
- trigger input schema as a JSON string
- `nodeOutputs` and `nodeTokenData` for dynamic-content tokens
- `nodeOperationInfo` with connector `PowerApps`, operation `PowerAppsButtonV2`, type `Request`, kind `PowerAppV2`

Confirmed live by user, 2026-08-03:

- Power Automate can copy a `Power Apps (V2)` trigger payload containing a full schema.
- Important correction, confirmed 2026-08-04: the designer does not allow a trigger to be pasted into the trigger slot. A flow's trigger is created when the flow is created. If the trigger is deleted, the designer still does not provide a usable paste target for a copied trigger.
- Therefore, create `Power Apps (V2)` triggers and their inputs manually unless/until Microsoft changes this behavior.
- Generated initializer payloads for `varSuccess` Boolean and `varMessage` String are now treated as confirmed shortcuts in the Training Tracker migration guide.

Generated action-paste buttons are still viable for actions after the trigger. Be careful with new action families because Microsoft documents copy/paste behavior, not the raw clipboard JSON as a public authoring format.

### Internal Trigger Keys Matter

For the 11-input save trigger, Power Automate generated these internal body keys:

| Display title | Type | Internal key |
| --- | --- | --- |
| `DateCompleted` | Date | `date` |
| `HasNewFile` | Boolean | `boolean` |
| `FileName` | Text | `text` |
| `FileContent` | File | `file` |
| `PersonEmail` | Text | `text_1` |
| `CourseName` | Text | `text_2` |
| `ActorEmail` | Text | `text_3` |
| `ViewingForSelf` | Boolean | `boolean_1` |
| `RecordID` | Number | `number` |
| `CourseID` | Number | `number_1` |
| `IsAdmin` | Boolean | `boolean_2` |

Do not guess these keys in instructions when the dynamic-content picker can be used. For generated clipboard payloads, preserve the order exactly if Power Apps formulas already call `.Run(...)` in that order.

### Boolean Values

When comparing or setting true/false values in Power Automate, prefer the expression editor with bare `true` or `false`. Do not rely on Yes/No dropdown text when the target is a real boolean. This avoided Training Tracker conditions silently comparing a boolean to text.

### Dynamic Content With Repeated Field Names

Power Automate's dynamic-content picker groups tokens by action, but many SharePoint and trigger fields have identical display names. Do not write guide steps like "pick `CourseName`" when the flow has several `CourseName` tokens from different actions. Always name the source action group.

Use this wording pattern:

- `CourseName` from `When Power Apps calls a flow (V2)`.
- `PersonEmail` from `Get item`.
- `ItemId` from `Create file`.
- `Identifier` from `Get files (properties only)`.
- file content/body from `Get file content`.

Training Tracker confirmed this matters live: while filling `TT AuditLog.EventDescription`, the dynamic-content picker showed `CourseName` under `Update item`, `Update file properties`, `Get files (properties only)`, `Get item`, and `When Power Apps calls a flow (V2)`. The intended value for audit/log/library metadata in the certificate save flow is usually the trigger value from `When Power Apps calls a flow (V2)`, not the similarly named values from later SharePoint actions.

### Respond To A PowerApp Or Flow

Avoid multiple `Respond to a PowerApp or flow` actions in separate Condition branches when the app depends on the response schema. Training Tracker hit a persistent Power Apps schema-recognition failure where only some outputs appeared. The robust pattern is:

1. Initialize top-level variables before the Condition.
2. Set those variables inside each branch.
3. Place exactly one `Respond to a PowerApp or flow` action after the branches rejoin.

For simple flows where both branches return exactly the same two fields and the app already works, do not rebuild solely for purity. But do not copy the two-Respond pattern into new flows.

### Designer Clipboard Payloads

Confirmed copied action/container templates:

- `Initialize variable` Boolean action.
- `Initialize variable` String action.
- `Respond to a PowerApp or flow` action.
- Basic `Condition` container using `serializedValue`.

Not yet captured from the user's tenant:

- SharePoint `Get item`.
- SharePoint `Get files (properties only)`.
- SharePoint `Delete file`.
- SharePoint `Create file`.
- SharePoint `Update file properties`.
- SharePoint `Update item`.
- SharePoint `Create item`.
- Office 365 Outlook `Send an email (V2)`.

Until those connector templates are captured, do not generate full SharePoint/Outlook action paste blocks except as clearly experimental stubs. The connector payloads may include tenant/list/library/connection metadata that should come from a real copied action.

## Training Tracker Certificate Architecture

Agreed direction, 2026-08-03:

- Keep `TT TrainingRecords` as ordinary training metadata: person, email, course, date, status.
- Move certificate files into a separate locked SharePoint document library created as `TT Certificates_LTD`, optionally renamed for display as `TT Certificates (LTD)`.
- Use Power Automate as the gate:
  - Save flow writes/replaces the library file and updates metadata.
  - Email flow validates the requester and emails the certificate.
- Do not lock the whole `TT TrainingRecords` list to 2-3 admins; it would break normal users seeing their own training data.
- Do not default back to list attachments plus per-item permissions unless the user explicitly asks to revisit that route.

Published migration guide:

- `../training-tracker/certificate-library-migration.html`

## Future Work: When Tenant Access Is Available

User currently does not have access to the target tenant, so SharePoint/Outlook connector payload capture is paused.

When access is available again, ask for copied payloads from real actions in this order:

1. SharePoint `Get item` against `TT TrainingRecords`.
2. SharePoint `Get files (properties only)` against `TT Certificates_LTD` / `TT Certificates (LTD)`.
3. SharePoint `Create file` against `TT Certificates_LTD` / `TT Certificates (LTD)`.
4. SharePoint `Update file properties` against `TT Certificates_LTD` / `TT Certificates (LTD)`.
5. SharePoint `Update item` against `TT TrainingRecords`.
6. SharePoint `Create item` against `TT AuditLog`.
7. Outlook `Send an email (V2)`.

After each captured template, generate one pasteable chunk and have the user paste-test it before building bigger flow sections.
