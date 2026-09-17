# Prospect Research Runbook

## Purpose

Provide a repeatable, evidence-first method for turning publicly available business information into verified, qualified real-estate relationship records without fabricating facts, bypassing licensing requirements, or optimizing for raw outreach volume.

This runbook is the operating procedure for the live market-intelligence and verified-prospect queue.

## Operating Principle

**Signal → Source → Verify → Deduplicate → Qualify → Compliance → Record → Next Action → Relationship → Opportunity → Revenue**

A market signal is not a prospect. A prospect is not an opportunity. An estimated opportunity is not revenue.

## 1. Define the Research Target

Before searching, specify:

- Relationship segment.
- Texas market; track DFW separately.
- Relevant asset/property type, if applicable.
- Legitimate business reason.
- Potential service or relationship outcome.

Do not perform broad contact harvesting without a defined business purpose.

## 2. Source Hierarchy

Prefer the strongest reasonably available evidence:

1. Government/regulatory sources and official public records.
2. Official company, brokerage, developer, lender, law firm, title company, or professional websites.
3. Established professional associations and institutional directories.
4. Reputable business/trade publications used as corroboration when practical.
5. Search results only as discovery; verify material facts against stronger sources.

Preserve the source URL/reference and research date.

## 3. Identify the Signal

Useful signals include:

- Development/redevelopment announcement.
- Public incentive application or award.
- Zoning/planning action.
- Expansion, relocation, or major investment.
- Financing/development milestone.
- Property or portfolio change supported by reliable evidence.
- New professional relationship opportunity.

Record the factual signal. Do not infer ownership, financial condition, intent, motivation, or need for services unless supported.

## 4. Verify the Candidate

Establish, where reasonably possible:

- Identity.
- Organization and role.
- Geographic relevance.
- Relevant property/business context.
- Official business presence.
- Source reliability.
- Research date.
- Legitimate reason communication would be appropriate.
- DNC/opt-out status when applicable.
- Licensing/compliance implications of the intended action.

Missing information must be `Unknown` or `Needs Review`, never guessed.

## 5. Preserve Evidence

For each material fact, capture:

- Source.
- Source URL/reference.
- Research date.
- Verification status.
- Fact supported by the source.

Do not copy unnecessary personal information into the pipeline.

## 6. Deduplicate Before Qualification

Search existing pipeline records using available combinations of:

- Organization.
- Person + organization.
- Website/domain.
- Property/project identifier.
- Existing contact identity.

If a duplicate exists, update the existing relationship. If duplication cannot be resolved confidently, route to `Needs Review`.

## 7. Qualification Gate

A candidate may move from `New` to `Qualified` only when:

- Identity/source is sufficiently verified.
- Geographic relevance is established.
- A specific business reason is documented.
- Intended communication is appropriate.
- No known DNC/opt-out restriction blocks contact.
- Compliance implications are classified.

## 8. Communication-Readiness Gate

Before outreach preparation or sending:

- Confirm recipient identity and business relevance.
- Use accurate sender identity and truthful subject matter.
- Apply the commercial email standard.
- Include required business identification and physical postal address.
- Include a working opt-out mechanism where required.
- Check DNC/opt-out status.
- Do not misrepresent licensing, representation, authority, property facts, transaction status, or relationships.

If a material control is unresolved, set `Compliance Status = Review Required` and stop the affected outreach.

## 9. Licensing Gate

Classify the intended action:

- **Clear:** research, ordinary relationship development, administrative organization, or another activity that does not require unresolved regulated authority.
- **Review Required:** the action could involve Texas-regulated brokerage activity or another material compliance question.
- **Blocked:** the action cannot proceed under currently verified authority/conditions.

A valuable opportunity does not override the gate.

## 10. Create the Prospect Record

Use `docs/02-growth/PROSPECT_RECORD_SCHEMA.md`.

Minimum evidence package:

- Record ID.
- Organization/person.
- Relationship type.
- Market.
- Asset/service context.
- Source and source URL/reference.
- Research date.
- Verification status.
- Business reason.
- Potential service.
- Stage.
- Compliance status.
- Notes/evidence.

Never fabricate contact information.

## 11. Assign Exactly One Next Action

Every `Qualified`, `Engaged`, `Opportunity`, or `Active` record receives:

- One concrete next action.
- One due date.

Examples: verify a missing fact, prepare a compliant introduction, review a response, schedule a relationship call, research a partner, or escalate a licensing question.

## 12. Outlook Routing

Use the Real Estate categories to make queues visible:

- `Real Estate - Research Queue`
- `Real Estate - Verified Prospect`
- `Real Estate - Follow Up Due`
- `Real Estate - Conversation`
- `Real Estate - Opportunity Review`
- `Real Estate - Needs Review`
- `Real Estate - Stalled`
- `Real Estate - Revenue`
- `Real Estate - Compliance`
- `Real Estate - Email Compliance`
- `Real Estate - Closed Won`

The category is a workflow aid; the prospect record remains the source of truth.

## 13. Outcome Metrics

Review weekly:

- Candidates researched.
- Candidates with sufficient evidence.
- Verification rate.
- Duplicate rate.
- Qualified relationships created.
- Meaningful conversations.
- Opportunities created/advanced.
- Compliance escalations.
- Stalled records.
- Realized revenue.
- Revenue by source/relationship segment when enough data exists.

Do not optimize for searches, contacts, or emails sent.

## 14. Data Freshness

Every material signal retains its source date. Re-verify time-sensitive information before relying on it for outreach or an opportunity decision.

Re-check material facts when an opportunity advances, a long follow-up gap occurs, the source appears stale, contact/role information changes, or the fact becomes material to a next action.

## 15. Automation Boundaries

Automation may assist with:

- Discovery queues.
- Source capture.
- Duplicate detection.
- Missing-field checks.
- Follow-up reminders.
- Pipeline routing.
- Response categorization.
- Stalled-record detection.
- Weekly metrics.

Automation must not:

- Fabricate prospect information.
- Circumvent DNC/opt-out requests.
- Misrepresent identity or authority.
- Perform Texas-regulated brokerage activity without required authorization.
- Treat estimated pipeline value as realized revenue.
- Replace required human/compliance review.

## 16. Daily Research Loop

1. Review target segment and market.
2. Research a focused batch of candidates.
3. Verify each candidate.
4. Deduplicate against the pipeline.
5. Apply communication and compliance gates.
6. Create/update records.
7. Assign one dated next action.
8. Prepare or execute only outreach that passes the readiness gate.
9. Process responses and advance legitimate opportunities.
10. End with no qualified record lacking a next action.

## 17. Weekly Quality Review

Ask:

- Which sources produce verified relationships?
- Which segments produce meaningful conversations?
- Where do records fail verification?
- Which opportunities are stalled?
- Which follow-ups are overdue?
- Which compliance questions recur?
- Which relationships produce referrals or revenue?
- What should be automated next?

Raw contact count is not the primary success metric.

## Definition of Done

A research cycle is complete when every material candidate has a documented source/date, verification state, business reason, compliance classification, and next action—or is explicitly rejected, stalled, nurtured, or marked for review.

Another operator must be able to answer for any active record: **who, why, source, when verified, stage, compliance status, last event, next action, estimated value, and realized revenue.**