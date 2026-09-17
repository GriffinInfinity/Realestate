# Prospect Research Runbook

## Purpose

Provide a repeatable method for turning publicly available business information into verified, qualified real-estate relationship records without fabricating facts, bypassing licensing requirements, or optimizing for raw outreach volume.

This runbook is the operating procedure for Phase 1D: **Populate the Verified Prospect Pipeline**.

## Operating Principles

1. **Evidence before entry.** A prospect is not qualified because it looks promising; the record must have a legitimate source and business reason.
2. **Public does not mean permanent.** Public information can become stale. Preserve the source and research date.
3. **Never invent missing data.** Use `Unknown` or `Needs Review`.
4. **Relationship first.** Optimize for legitimate conversations and qualified opportunities, not message count.
5. **Compliance is a gate.** A potentially regulated activity pauses until the applicable authorization/licensing path is established.
6. **One next action.** Every qualified, engaged, opportunity, or active record has one concrete dated next action.
7. **Estimated value is not revenue.** Forecasts remain separate from realized revenue.

## Source Hierarchy

Use the strongest reasonably available source for each fact:

1. Government/regulatory sources and official public records.
2. Official company, brokerage, developer, lender, law firm, title company, or professional website.
3. Established professional association or institutional directory.
4. Reputable business/news publication used as corroboration rather than sole proof when practical.
5. Search-engine discovery results only as a starting point; verify important facts against a stronger source.

Do not treat scraped, unverifiable, anonymous, or obviously stale information as sufficient evidence for a critical field.

## Research Workflow

### Step 1 — Define the target

Before searching, specify:

- Relationship type.
- Texas market and whether DFW is the immediate focus.
- Relevant asset/property type, if applicable.
- Intended legitimate business reason.
- Potential service or relationship outcome.

### Step 2 — Discover candidates

Search for organizations or professionals that plausibly match the target. Favor identifiable businesses and professional relationships over indiscriminate contact lists.

Examples of useful relationship segments:

- Property owners and operators.
- Buyers and investors.
- Developers.
- Licensed brokers and brokerage partners.
- Lenders and finance professionals.
- Attorneys and title professionals.
- Property managers.
- Contractors, inspectors, and appraisers.
- Referral sources and complementary vendors.

### Step 3 — Verify identity

Confirm, where reasonably possible:

- Correct organization/person identity.
- Current role or relationship.
- Relevant market.
- Official business presence.
- Source URL/reference.
- Research date.

If identity or role cannot be established, keep `Verification Status = Needs Review` or `Unverified`.

### Step 4 — Verify business relevance

Document why the relationship is relevant **now**, not merely why the organization exists.

A useful business reason identifies a concrete relationship or service context such as:

- Active or recurring real-estate activity.
- Development or property operations.
- Financing relationships.
- Professional referral potential.
- A service need that can legitimately be discussed without performing regulated brokerage activity.

Avoid unsupported assumptions about property ownership, transaction intent, financial condition, motivation, or willingness to sell/buy.

### Step 5 — Preserve evidence

For every qualified record, capture:

- Source.
- Source URL/reference.
- Source date.
- Verification status.
- The specific fact supported by the source.

Do not copy unnecessary personal information into the pipeline.

### Step 6 — Deduplicate

Before creating a record, search the existing pipeline for matching:

- Organization.
- Person + organization.
- Domain.
- Property/business identifier, when legitimately available.

If a duplicate exists, update the existing relationship rather than creating a second record unless there is a documented reason for separate records.

### Step 7 — Apply communication controls

Before outreach preparation or sending:

- Confirm recipient identity and business relevance.
- Confirm the reason contact is appropriate.
- Check the do-not-contact/opt-out status.
- Use truthful sender identity and subject matter.
- Apply the commercial email standard.
- Ensure required business disclosures and opt-out controls are present.
- Do not imply a license, representation, authority, transaction status, or property fact that has not been established.

### Step 8 — Apply the licensing/compliance gate

Classify the intended action:

- **Clear:** ordinary relationship development, research, administrative organization, or other activity not requiring the unresolved exercise of a regulated real-estate function.
- **Review Required:** the planned action could involve Texas-regulated brokerage activity or another material compliance question.
- **Blocked:** the action cannot proceed under the currently verified authority/conditions.

Do not advance a compliance-sensitive opportunity simply because the prospect is valuable.

### Step 9 — Qualify the relationship

A record can move from `New` to `Qualified` only when the minimum evidence standard is met:

- Identity/source verified sufficiently.
- Geographic relevance established.
- Legitimate business reason documented.
- Intended communication is appropriate.
- No known do-not-contact restriction.
- Compliance implications identified.

### Step 10 — Create the record

Use `docs/02-growth/PROSPECT_RECORD_SCHEMA.md` exactly. Required fields should be populated or explicitly marked `Unknown`/`Needs Review` rather than guessed.

### Step 11 — Set the next action

Every qualified relationship receives exactly one dated next action. Examples:

- Research a missing business fact.
- Prepare compliant introduction.
- Send approved outreach.
- Review a response.
- Schedule a relationship call.
- Introduce a qualified partner.
- Review licensing requirements.
- Move to nurture.

The next action should advance the relationship rather than create activity for its own sake.

### Step 12 — Measure outcomes

Track separately:

- New verified prospects.
- Qualified relationships.
- Meaningful conversations.
- Follow-ups completed.
- Opportunities created/advanced.
- Estimated pipeline value.
- Closed revenue.
- Referral/partner relationships.
- Compliance reviews.
- Disqualified records.

## Qualification Evidence Standard

### Minimum evidence for `Qualified`

| Field | Standard |
|---|---|
| Identity | Supported by a credible source |
| Role/relationship | Supported by a credible source or clearly documented relationship |
| Market | Texas relevance established; DFW tracked separately where applicable |
| Business reason | Specific and defensible |
| Source | URL/reference preserved |
| Source date | Recorded |
| Communication | Appropriate for the intended contact |
| DNC/opt-out | Checked and recorded |
| Compliance | Clear, Review Required, or Blocked |
| Next action | One concrete dated action |

## Handling Uncertainty

Use these statuses deliberately:

- `Unverified` — candidate discovered but not sufficiently checked.
- `Partially Verified` — some material facts confirmed, but important gaps remain.
- `Verified` — material identity, role, market, and source requirements are supported.
- `Needs Review` — a human/compliance review is required before advancement or action.

Never convert uncertainty into a confident-looking record.

## Outreach Readiness Gate

A record is outreach-ready only when all applicable controls pass:

- Verified identity.
- Legitimate business reason.
- Correct recipient information.
- No DNC/opt-out conflict.
- Truthful personalization.
- Commercial email requirements satisfied.
- Required physical address included.
- Clear opt-out mechanism included.
- No misleading claims.
- Licensing-sensitive activity reviewed where applicable.

## Data Freshness

For active research, record the date the information was checked. Re-verify material facts when:

- The relationship becomes an opportunity.
- A significant follow-up is planned after a long gap.
- The source appears stale.
- Contact/role information changes.
- A property, company, or transaction fact becomes material to the next action.

## Automation Boundaries

Automation may assist with:

- Discovery queues.
- Duplicate detection.
- Missing-field checks.
- Source/date reminders.
- Follow-up reminders.
- Pipeline routing.
- Response categorization.
- Weekly metrics.
- Stalled-record detection.

Automation must not be used to:

- Fabricate prospect information.
- Circumvent do-not-contact requests.
- Misrepresent identity or authority.
- Perform Texas-regulated brokerage activity without the required authorization.
- Treat an estimated opportunity as realized revenue.
- Replace required human/compliance review.

## Daily Research Loop

1. Review the target segment and market.
2. Research a focused batch of candidates.
3. Verify each candidate before qualification.
4. Deduplicate against the existing pipeline.
5. Apply communication and compliance gates.
6. Create/update records.
7. Assign one dated next action.
8. Prepare or execute only outreach that passes the readiness gate.
9. Process responses and advance legitimate opportunities.
10. End the session with no qualified record lacking a next action.

## Weekly Quality Review

Review:

- Which sources produce verified relationships?
- Which segments produce meaningful conversations?
- Where are records failing verification?
- Which opportunities are stalled?
- Which follow-ups are overdue?
- Which compliance questions recur?
- Which relationships produce referrals or revenue?
- Which processes should be automated next?

Do not use raw contact count as the primary success metric.

## Definition of Done

The research system is operational when another operator can take any prospect record and answer:

1. Who is this?
2. What is the relationship type?
3. Why is this relationship relevant?
4. Where did the information come from?
5. When was it verified?
6. What is the current stage?
7. Is outreach appropriate?
8. Is there a licensing/compliance gate?
9. What happened most recently?
10. What is the one next action and when is it due?
11. What is estimated opportunity value, if any?
12. What revenue has actually been realized?

That standard is the foundation for scaling the Texas relationship engine into additional markets without sacrificing data quality, compliance, or operational control.
