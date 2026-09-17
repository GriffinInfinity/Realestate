# Verified Prospect Pipeline

This directory is reserved for **verified, operational prospect data** supporting the Texas/DFW launch.

## Data policy

- Store only information necessary for legitimate business operations.
- Never fabricate names, roles, emails, phone numbers, properties, transaction history, or financial information.
- Preserve the source/reference and research date for material facts.
- Treat public information as potentially stale.
- Record `Unknown` or `Needs Review` when a fact cannot be established.
- Honor do-not-contact and opt-out status.
- Do not use this directory to bypass licensing, privacy, or other legal requirements.

## Record standard

The canonical record schema is:

`docs/02-growth/PROSPECT_RECORD_SCHEMA.md`

The research procedure is:

`docs/02-growth/PROSPECT_RESEARCH_RUNBOOK.md`

The acquisition workflow is:

`docs/02-growth/PROSPECT_ACQUISITION_ENGINE.md`

## Recommended record lifecycle

`New → Qualified → Engaged → Opportunity → Active → Won`

Alternative outcomes:

`Nurture` or `Disqualified`

Every record at `Qualified`, `Engaged`, `Opportunity`, or `Active` must have exactly one concrete dated next action.

## Market scope

Launch market:

- Texas statewide
- DFW tracked separately

Do not expand the operating footprint merely to increase record count. Expansion should follow evidence that the local relationship and revenue process is repeatable.

## Safe storage guidance

Do not commit passwords, API keys, access tokens, payment credentials, government identifiers, sensitive personal data, or unnecessary private contact information.

For outreach operations, use the connected Outlook system as the operational communication record and preserve only the minimum repository data needed for pipeline control, analytics, and reproducibility.
