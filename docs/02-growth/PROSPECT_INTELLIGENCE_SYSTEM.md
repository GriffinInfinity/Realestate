# Prospect Intelligence System

## Purpose

Create a repeatable system that turns market information into verified, relevant relationship opportunities without relying on unverified contact data, indiscriminate outreach, or licensing-sensitive activity before the required authorization exists.

## Operating Flow

`Market signal → Prospect discovery → Source verification → Qualification → Relationship mapping → Compliance gate → Outreach opportunity → Pipeline record → Next action`

The system is designed for Texas first, with DFW tracked as a distinct market. The data model must support expansion into additional U.S. markets and, later, international markets without redesigning the core pipeline.

## 1. Target Relationship Segments

### Property owners
- Residential owners where a legitimate business reason exists
- Commercial property owners
- Landowners
- Developers and development groups
- Multifamily owners/operators
- Distressed or changing-portfolio situations only when sourced legitimately and handled appropriately

### Capital and demand relationships
- Buyers
- Investors
- Developers seeking acquisition opportunities
- Lenders and financing professionals
- Family-office or institutional contacts where publicly identifiable and relevant

### Professional partners
- Licensed brokers and sales agents
- Title professionals
- Real-estate attorneys
- Inspectors
- Appraisers
- Contractors
- Property managers
- Insurance professionals
- Accountants and other adjacent professional-service providers

## 2. Source Verification Standard

Every prospect should have a source trail before being treated as qualified.

Required source fields:

| Field | Requirement |
|---|---|
| Source | Where the prospect was discovered |
| Source URL/reference | Direct reference when available |
| Source date | Date research was performed |
| Identity verified | Yes/No |
| Organization verified | Yes/No |
| Role verified | Yes/No |
| Geographic relevance | Texas / DFW / Other |
| Business reason | Why the relationship is relevant |
| Property/asset context | If applicable |
| Contact method | Public business email, phone, website, referral, etc. |
| Verification notes | Evidence supporting the record |

Do not fabricate missing fields. Unknown information stays unknown until verified.

## 3. Qualification Gates

A prospect becomes **Qualified** only when the following are sufficiently established:

1. The person or organization can be identified.
2. The business relationship is relevant to the company's current strategy.
3. There is a legitimate reason for contact.
4. The contact source is appropriate and traceable.
5. Outreach is legally and operationally appropriate.
6. Any required licensing or brokerage boundary has been identified.
7. A useful next action can be defined.

Qualification is not the same as predicted revenue. A prospect can be highly relevant while having no known monetary value yet.

## 4. Relationship Mapping

For each qualified record, capture the relationship type and potential path to value:

- Owner → potential property conversation
- Investor → potential acquisition/investment relationship
- Buyer → potential demand relationship subject to applicable representation rules
- Broker → referral/co-broker/market relationship subject to licensing and brokerage structure
- Lender → financing relationship
- Attorney/title → transaction-support relationship
- Contractor/vendor → property-services relationship
- Property manager → operations relationship
- Developer → development/acquisition relationship

The system should record the relationship pathway rather than assume a transaction exists.

## 5. Pipeline Record Schema

Each prospect/opportunity should support these fields:

```text
record_id
organization
contact_name
role
relationship_type
market
submarket
property_or_asset_context
source
source_url
source_date
identity_verified
organization_verified
role_verified
business_reason
potential_service
stage
compliance_status
licensing_status
last_contact_date
last_contact_type
last_contact_summary
next_action
next_action_date
opt_out_status
do_not_contact
estimated_value
realized_revenue
opportunity_created_date
closed_date
outcome
owner_notes
```

## 6. Stage Discipline

Use the controlled stages defined in `docs/04-operations/PIPELINE_STAGE_DEFINITION.md`:

`New → Qualified → Engaged → Opportunity → Active → Won`

Alternate paths:

`Qualified → Nurture`

`Any pre-closed stage → Disqualified`

A record may not advance merely because more messages were sent. Advancement requires a meaningful change in relationship or opportunity status.

## 7. Outreach Preparation Gate

Before a prospect enters an outreach queue:

- Identity and business relevance are verified.
- Reason for contact is documented.
- Sender identity will be accurate.
- Subject/content will be truthful.
- Required commercial-email disclosures are handled.
- Physical mailing-address requirement is satisfied.
- Working opt-out mechanism is available where required.
- Do-not-contact status is clear.
- No fabricated property, licensing, representation, authority, or transaction claims are present.
- Texas licensing boundaries have been reviewed where applicable.

See `docs/03-compliance/COMMERCIAL_EMAIL_AND_OUTREACH_STANDARD.md` for the controlling outreach standard.

## 8. Research Priority Framework

Research effort should concentrate on prospects where the available evidence supports a concrete business reason. Priority can increase when several of these conditions are present:

- Clear geographic relevance
- Identifiable property or portfolio context
- Relevant professional role
- Current business activity
- Existing relationship or warm introduction
- Clear service need
- Timely event or change
- Strong fit with the current operating model

This is a research-prioritization framework, not a promise of conversion or revenue.

## 9. Market Expansion Architecture

### Stage A — Texas launch

Establish repeatable prospect intelligence and relationship development in Texas, with DFW separately tracked.

### Stage B — Texas coverage

Add additional Texas markets only after the operating loop produces reliable records, conversations, opportunities, and compliant workflows.

### Stage C — U.S. expansion

Replicate the data model and operating controls market by market, adding jurisdiction-specific licensing/compliance gates.

### Stage D — International expansion

Add country-specific legal, tax, licensing, entity, data-protection, and transaction requirements before operating in each new jurisdiction.

## 10. Daily Research Loop

1. Review new market signals.
2. Identify legitimate prospects.
3. Verify source and identity.
4. Record business reason.
5. Classify relationship and market.
6. Apply compliance/licensing gate.
7. Add qualified prospects to pipeline.
8. Define one next action and date.
9. Prepare only appropriate outreach.
10. Record responses and relationship changes.
11. Move records between stages only when stage conditions are met.

## 11. Data Quality Controls

The system must reject or flag:

- Duplicate prospects
- Unverified identities
- Unsupported claims
- Missing source information
- Missing next action on active records
- Missing next-action date
- Conflicting DNC/opt-out status
- Unresolved compliance gates
- Estimated revenue represented as realized revenue
- Contacts with no documented business reason

## 12. Management Metrics

Track:

- New verified prospects
- Qualified prospects
- Meaningful conversations
- Follow-ups completed
- Opportunities created
- Opportunities advanced
- Qualified relationships by segment
- Referral/partner relationships
- Closed revenue
- Realized revenue versus estimates
- Pipeline aging
- Compliance escalations
- DNC/opt-out events
- Source-to-opportunity conversion
- Time from discovery to qualified relationship

Do not optimize the company around raw contact volume. The primary operating objective is legitimate relationship creation and qualified opportunity development.

## Definition of Done

The Prospect Intelligence System is operational when a new prospect can move from discovery to a verified, classified, compliance-reviewed pipeline record with a documented business reason, traceable source, appropriate next action, and measurable outcome — without requiring a redesign of the process when the company expands into another market.
