# Revenue Operations Data Model

## Purpose
Define the minimum linked records needed to operate the Realestate venture as a measurable business while preserving evidence, compliance controls, and the distinction between estimates and realized results.

## Core entities

| Entity | Purpose | Primary identifier |
|---|---|---|
| Prospect | Verified organization/person relationship | Record ID |
| Relationship Edge | Evidence-backed connection between records | Edge ID |
| Outreach | Individual commercial/business communication | Outreach ID |
| Conversation | Meaningful two-way interaction | Conversation ID |
| Introduction | Referral or introduction actually made | Introduction ID |
| Opportunity | Candidate commercial need | Opportunity ID |
| Activity | Observable operational action | Activity ID |
| Compliance Review | Licensing/commercial/compliance gate | Review ID |
| Revenue Event | Realized revenue | Revenue ID |
| Source | Evidence origin | Source ID |

## Linkage

`Source → Prospect → Outreach → Conversation → Introduction → Opportunity → Activity → Revenue Event`

Relationship edges can connect any two verified prospects when the connection is supported by evidence.

## Minimum audit fields
Every mutable business record should preserve:
- Created date
- Last updated date
- Owner/operator
- Source or originating record
- Evidence/reference
- Current status
- Previous material status when changed
- Next action where applicable
- Next action date where applicable

## Opportunity economics
Store estimated economics separately from realized revenue:
- Estimated gross value
- Estimate basis
- Estimate confidence
- Expected timing, when evidence supports it
- Actual revenue amount
- Actual revenue date
- Supporting revenue record

Never calculate revenue from an estimate.

## Funnel metrics
Use counts and conversion rates only where the underlying records meet their respective gates:
- Verified prospects
- Meaningful conversations
- Verified introductions
- Qualified opportunities
- Active opportunities
- Won opportunities
- Realized revenue

Conversion metrics must state the denominator and measurement period.

## Operational health metrics
- Records missing required fields
- Qualified records missing a next action
- Overdue next actions
- Opportunities aging beyond the operating threshold
- Compliance reviews awaiting resolution
- DNC/opt-out records
- Duplicate candidates
- Sources requiring re-verification

These metrics measure process health; they are not financial performance claims.

## Attribution model
Use direct factual attribution first:
- Originating prospect
- Referral/introduction source
- Market-intelligence source
- Service category
- Revenue event

Do not assign subjective contribution percentages unless a documented agreement supports them.

## Automation boundaries
Automation may:
- identify missing fields
- detect stale records
- suggest research priorities
- prepare follow-up queues
- calculate operational metrics
- connect records using documented evidence
- prepare compliant drafts for authorized execution

Automation must not:
- invent missing facts
- infer authority or licensing
- convert estimates into revenue
- bypass DNC/opt-out controls
- execute regulated or contractual actions without required authorization

## Management reporting standard
Every management report should identify:
1. Measurement period.
2. Population included.
3. Source of the data.
4. Counts versus dollars.
5. Estimated versus realized economics.
6. Material data-quality limitations.

## Definition of done
The data model is operationally sound when another operator can trace a realized revenue event backward to the originating opportunity, relationship, conversation or referral, and evidence source without relying on undocumented assumptions.