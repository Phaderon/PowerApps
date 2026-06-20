# SharePoint And Office365Users Reference

Last checked: 2026-06-20

Sources:

- Office 365 Users connector in Power Apps: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections/connection-office365-users
- Patch function: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-patch
- Filter, Search, LookUp: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-filter-lookup
- Tables and records: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-tables

## SharePoint List Names

List names containing spaces must be quoted in formulas:

```powerfx
'TT Personnel'
'TT Courses'
'TT TrainingRecords'
```

Do not write unquoted names such as `TT Personnel`.

## SharePoint Choice Fields

Single choice fields use a record shape:

```powerfx
{Status: {Value: "Active"}}
```

Multi-choice fields use a table of choice records:

```powerfx
{ApplicableTo: ForAll(cmbApplicable.SelectedItems As T, {Value: T.Value})}
```

## SharePoint IDs

SharePoint-backed galleries usually expose `ThisItem.ID`. Collections only expose `ID` if the collection was built from data that includes it. Do not use `ThisItem.ID` in a collection-based gallery unless the collection schema is explicit.

## Office365Users

The connector has inconsistent casing across operations in the Training Tracker build.

Observed and preserved in this guide:

- `Office365Users.SearchUserV2(...).value` rows expose PascalCase fields such as `.DisplayName` and `.Mail`.
- `Office365Users.UserProfileV2(...)` returns lowercase camelCase fields such as `.displayName`, `.jobTitle`, and `.mail`.

Do not normalize these names by instinct. Verify the exact connector output for the operation used.

## People Search Combo Box

For a modern Combo box searching users:

```powerfx
Office365Users.SearchUserV2({searchTerm: cmbNewPerson.SearchText, top: 15}).value
```

Set display text to the returned display-name field:

```powerfx
ItemDisplayText=ThisItem.DisplayName
```

Set single-select explicitly where needed:

```powerfx
SelectMultiple=false
```

Use `InputTextPlaceholder`, not `Placeholder`, for the modern Combo box hint text.
