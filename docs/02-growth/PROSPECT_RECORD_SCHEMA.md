# Prospect Record Schema

## Purpose
Create one consistent record for every legitimate prospect, relationship, partner, or market lead entering the Realestate operating system.

The record is designed to support research, compliant outreach, follow-up, opportunity conversion, reporting, and eventual automation without confusing estimated economics with realized revenue.

## Required record

| Field | Required | Standard |
|---|---:|---|
| Record ID | Yes | Unique internal identifier |
| Organization / Person | Yes | Verified name |
| Relationship Type | Yes | Owner, Buyer, Investor, Broker Partner, Lender, Attorney, Title, Contractor, Inspector, Appraiser, Property Management, Developer, Vendor, Referral Source, Other |
| Market | Yes | City/metro, state, country |
| Asset / Property Type | When applicable | Residential, Commercial, Land, Development, Multifamily, Industrial, Retail, Office, Other |
| Source | Yes | Where the record was discovered |
| Source URL / Reference | Yes | Direct source or documented reference |
| Source Date | Yes | Date research was performed |
| Verification Status | Yes | Unverified, Partially Verified, Verified, Needs Review |
| Business Reason | Yes | Specific factual reason the relationship may be relevant |
| Potential Service | Yes | The legitimate service or relationship opportunity being explored |
| Stage | Yes | New, Qualified, Engaged, Opportunity, Active, Won, Nurture, Disqualified |
| Compliance Status | Yes | Clear, Review Required, Blocked |
| Last Contact | If contacted | Date and channel |
| Next Action | Required after qualification | One concrete action |
| Next Action Date | Required after qualification | Calendar date |
| Estimated Value | If applicable | Planning estimate only |
| Estimate Basis | If value entered | Evidence or assumptions supporting estimate |
| Actual Revenue | After revenue | Realized amount only |
| Revenue Date | After revenue | Date received/recognized |
| DNC / Opt-Out | Yes | No, Do Not Contact |
| Notes | As needed | Factual context and decision history |

## Verification standard

A prospect should not move from `New` to `Qualified` until the business relevance can be explained from a legitimate source.

Verification should establish, where applicable:

1. Identity or organization name.
2. Role or relationship to the relevant property/business.
3. Geographic relevance.
4. Asset or service context.
5. Source reliability.
6. Reason the contact is appropriate.
7. Whether outreach or activity has a licensing/compliance implication.

Do not fabricate missing information. Use `Unknown`, `Needs Review`, or another explicit status instead.

## Relationship mapping

A prospect may connect to multiple relationships. Capture the relationship that created the opportunity and any meaningful adjacent relationships.

Example:

`Property Owner → Broker Partner → Lender → Title → Contractor`

The relationship graph should help the business identify referral paths without treating an introduction as guaranteed revenue.

## Qualification rules

A record is `Qualified` when:

- The identity/source is sufficiently verified.
- There is a legitimate business reason for contact.
- The intended communication is appropriate.
- No known do-not-contact restriction applies.
- Any required compliance/licensing review has been identified.

Qualification is not a prediction of willingness to transact.

## Outreach controls

Before commercial outreach, confirm the applicable commercial-email standard, including accurate sender information, truthful subject/content, required physical-address disclosure, working opt-out mechanism, and do-not-contact controls.

Never claim to be a licensed broker, agent, representative, property owner, buyer, or authorized transaction party unless that status is actually established.

## Licensing gate

If an intended action could constitute Texas-regulated real-estate brokerage activity, mark `Compliance Status = Review Required` and pause the regulated action until the required authorization is verified.

Relationship development, research, administrative coordination, and general business communication must remain distinct from activities requiring a real-estate license.

## Opportunity economics

Estimated value is not revenue.

Record:

- Estimate amount.
- Estimate basis.
- Confidence/quality of underlying information.
- Actual realized revenue separately.

Never report estimated pipeline value as closed revenue.

## Next-action rule

Every qualified, engaged, opportunity, and active record must have exactly one clearly defined next action and date.

Good next actions are observable and specific:

- Research ownership/source information.
- Send compliant introduction.
- Reply to prospect.
- Schedule permitted meeting.
- Request missing business information.
- Route licensing-sensitive activity for review.
- Follow up on a stated need.
- Move to nurture after a no-now response.

Avoid vague actions such as `work on this`, `check later`, or `follow up sometime`.

## Data-quality rules

- One person/organization should not be duplicated without a documented reason.
- Preserve the original source.
- Preserve source date.
- Record material changes rather than silently overwriting history.
- Never invent contact information.
- Treat public information as potentially stale and re-verify before material use.
- Preserve opt-outs and compliance flags prominently.

## Automation readiness

This schema is intentionally machine-readable in concept. Future automation can use it to:

1. discover candidates,
2. verify records,
3. route records by relationship type,
4. identify missing fields,
5. create follow-up tasks,
6. prepare compliant outreach for authorized review/execution,
7. detect stalled opportunities,
8. summarize weekly performance,
9. identify repeatable revenue patterns.

Automation must not bypass licensing, consent, compliance, or human authorization requirements for regulated activity.

## Definition of done

A prospect record is production-ready when another operator can understand who the relationship is, why it matters, where the information came from, what stage it occupies, what compliance gate applies, what happened last, what happens next, and which economics are estimated versus realized.