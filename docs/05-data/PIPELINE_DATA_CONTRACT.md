# Pipeline Data Contract

## Purpose
Define a stable JSON contract for pipeline records so future Airtable, Outlook, web, dashboard, or automation integrations can exchange records without changing business semantics.

## Envelope
The standard envelope is an object containing schema_version, generated_at, and records.

## Record contract
Required fields:
- record_id
- organization_or_person
- relationship_type
- market
- source
- source_date
- verification_status
- business_reason
- potential_service
- stage
- compliance_status
- dnc_opt_out

Required after qualification:
- next_action
- next_action_date

Required for Won:
- actual_revenue
- revenue_date
- revenue_evidence

Optional:
- asset_property_type
- source_url
- last_contact
- estimated_value
- estimate_basis
- notes
- source_requires_refresh

## Controlled values
### Stage
New, Qualified, Engaged, Opportunity, Active, Won, Nurture, Disqualified

### Verification status
Unverified, Partially Verified, Verified, Needs Review

### Compliance status
Clear, Review Required, Blocked

### DNC / opt-out
Boolean. A true value always suppresses commercial outreach.

## Data rules
1. Dates use ISO-8601 date format unless a timestamp is explicitly required.
2. Monetary values are numeric amounts, not formatted currency strings.
3. Unknown information must be represented explicitly rather than invented.
4. Source and source date must travel with externally discovered records.
5. Estimated value and actual revenue are separate fields.
6. A record may not be considered Qualified without the qualification gate defined in the Prospect Record Schema.
7. A Won record requires evidence of realized revenue.
8. DNC/opt-out is an overriding suppression flag.
9. Compliance-sensitive records retain their compliance status when transferred between systems.
10. Integrations must not silently discard fields that affect compliance, verification, stage, attribution, or auditability.

## Integration behavior
### Import
- Validate schema version.
- Validate required fields.
- Reject or quarantine invalid records.
- Preserve source metadata.
- Deduplicate by record_id and documented identity rules.

### Export
- Include schema version.
- Include source/evidence fields.
- Preserve current stage and compliance status.
- Preserve DNC/opt-out state.
- Never export estimated value as realized revenue.

### Migration
When fields change:
- Increment schema version when semantics change.
- Document the migration.
- Preserve historical values where material.
- Run the validator against migrated data.

## Compatibility principle
Business rules remain authoritative even if an integration has different field names or UI terminology. Mapping layers should translate external representations into this contract rather than weakening the underlying controls.

## Definition of done
An integration is ready when it can import, validate, export, and migrate records without losing evidence, compliance status, DNC controls, opportunity stage, attribution fields, or the distinction between estimates and realized revenue.