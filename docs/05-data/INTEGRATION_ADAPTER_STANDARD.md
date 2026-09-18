# Integration Adapter Standard

## Purpose
Define how external systems connect to the Realestate data contract without becoming the source of truth for business rules.

## Adapter responsibilities
Every adapter must:
1. Accept or emit the versioned pipeline contract.
2. Validate records before they enter the operating pipeline.
3. Preserve source, verification, compliance, DNC, stage, attribution and audit fields.
4. Record import/export timestamps and adapter identity.
5. Quarantine invalid or ambiguous records.
6. Avoid silently overwriting verified information.

## Adapter boundary
External system → Mapping → Contract validation → Operating rules → Queue/record

The external system may provide data. It does not decide whether that data is Qualified, compliant, revenue, or otherwise authoritative.

## Required adapter metadata
Each synchronization event should record:
- sync_id
- adapter_name
- schema_version
- direction
- started_at
- completed_at
- records_received
- records_accepted
- records_quarantined
- records_rejected
- errors
- warnings
- source_system_reference

## Conflict handling
When external data conflicts with an existing verified record:
- Preserve the existing verified value.
- Capture the conflicting value and source.
- Mark the affected field for review.
- Do not silently select the newest value merely because it is newer.
- Re-verify against an authoritative source when material use is required.

## Idempotency
Repeated synchronization of the same source event must not create duplicate business records.
Adapters should use stable external identifiers plus the Realestate record ID where available.

## Write permissions
### Read-only
May discover, inspect and summarize external information.

### Proposed write
May prepare a mapped record or change for review.

### Controlled write
May make an approved low-risk change after validation.

### Restricted write
Regulated activity, contracts, financial commitments, licensing-sensitive actions and other material commitments require the appropriate human authorization.

## Security requirements
- Do not store credentials in repository files.
- Use environment-managed secrets for integrations.
- Minimize data transferred to what the workflow requires.
- Preserve audit references without exposing unnecessary sensitive information.
- Fail closed when authentication or authorization is uncertain.

## Testing requirements
Every adapter should have tests for:
- Valid record import.
- Required-field failure.
- Invalid controlled value.
- DNC/opt-out preservation.
- Compliance status preservation.
- Estimate/revenue separation.
- Duplicate synchronization.
- Conflicting source data.
- Malformed external payload.

## Deployment gate
An adapter is production-ready only when its mapping, validation, failure handling, permissions, audit behavior and tests are documented.

## Definition of done
The adapter can exchange records repeatedly without corrupting business semantics, losing compliance controls, creating duplicate records, or converting uncertain external information into verified business facts.