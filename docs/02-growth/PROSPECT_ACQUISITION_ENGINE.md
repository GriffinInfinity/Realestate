# Prospect Acquisition Engine

## Purpose
Create a repeatable, measurable system for turning legitimate market relationships into qualified real-estate opportunities while preserving a hard separation between relationship development and activities that require a Texas real-estate license.

## 1. Target relationship segments

### A. Property owners
Focus on owners with a plausible reason to discuss a property, portfolio, disposition, acquisition, management, or other real-estate need.

Capture:
- Owner/company name
- Property or portfolio location
- Property type
- Publicly documented business context
- Contact channel
- Reason for relevance
- Last contact
- Next action
- Licensing/compliance flag

### B. Buyers and investors
Focus on people or organizations that have an identifiable acquisition or investment objective.

Capture:
- Buyer/investor name
- Entity/company
- Target geography
- Property type
- Stated objective
- Approximate timing
- Financing status when voluntarily provided
- Contact channel
- Next action
- Licensing/compliance flag

### C. Professional partners
Build relationships with:
- Licensed brokers
- Lenders
- Title/escrow professionals
- Insurance professionals
- Real-estate attorneys
- Contractors and trades
- Property managers
- Appraisers and inspectors
- Tax/accounting professionals
- Developers and other relevant operators

The objective is a dependable referral and execution network, not merely a contact list.

## 2. Qualification model

Every prospect receives a simple operational status:

| Status | Meaning | Required action |
|---|---|---|
| New | Identified but not reviewed | Research relevance |
| Qualified | Relevant relationship with a credible business reason | Initiate appropriate contact |
| Engaged | Contact established and conversation underway | Schedule next action |
| Opportunity | Specific business need identified | Define next step and compliance gate |
| Active | Opportunity is progressing through an authorized process | Execute next action |
| Won | Revenue-generating outcome completed | Record economics and lessons |
| Nurture | Legitimate relationship, no immediate opportunity | Schedule future touch |
| Disqualified | Not relevant, invalid, or unsuitable | Close with reason |

## 3. Opportunity qualification

An opportunity should answer five questions:

1. Who is the decision-maker?
2. What real-estate problem or objective exists?
3. Where is the relevant property or market?
4. What is the expected timing?
5. What is the next concrete action?

If the answer to #5 is missing, the record is not considered actively managed.

## 4. Outreach sequence

Use targeted, relevant, business-purpose communication rather than indiscriminate bulk messaging.

### Touch 1 — Relevance
Introduce the business purpose and explain why the recipient was contacted.

### Touch 2 — Value
Follow up with a concise, useful reason to continue the conversation.

### Touch 3 — Qualification
Ask one or two focused questions that determine whether a legitimate need exists.

### Touch 4 — Close or nurture
If there is no active need, respectfully move the relationship to nurture rather than repeatedly contacting the person.

### Rules
- Personalize every meaningful outreach.
- Do not misrepresent licensing status or brokerage authority.
- Do not imply representation where none exists.
- Do not provide transaction advice when operating outside the authority required to provide it.
- Honor opt-outs and do-not-contact requests.
- Record substantive business communications when they relate to an active opportunity.

## 5. Pipeline data model

Minimum record fields:

```text
record_id
relationship_type
person_or_company
email
phone
market
property_address_or_area
property_type
opportunity_type
source
qualification_status
reason_for_contact
last_contact_at
next_action
next_action_at
estimated_value
probability_basis
compliance_flag
license_required
broker_relationship
notes
created_at
updated_at
```

## 6. Compliance gate

Before an opportunity moves from relationship development into regulated brokerage activity, explicitly classify the activity.

### Gate A — Relationship development
General business networking, research, introductions, and other activity that does not constitute regulated brokerage activity may proceed within applicable law and company policy.

### Gate B — Licensing-sensitive activity
Stop and verify authorization before performing activities that may constitute brokerage services, including representing a buyer or seller, negotiating a transaction, soliciting or accepting brokerage agreements, or other activity requiring a license.

Texas TREC states that a sales agent must be sponsored by a licensed broker to perform real-estate services, and that an inactive license cannot be used to practice. citehttps://www.trec.texas.gov/node/122

### Gate C — Residential buyer workflow
For Texas residential buyers, current 2026 rules require written agreements in specified circumstances before showing residential property or presenting an offer on the buyer's behalf. Non-representation showings have separate restrictions. citehttps://www.trec.texas.gov/article/what-changes-2026-about-buyertenant-representation-texas

### Gate D — Compensation
Do not structure or accept transaction compensation outside the applicable broker/licensing framework. TREC states that sales-agent compensation must be handled through or with the written consent of the sponsoring broker. citehttps://www.trec.texas.gov/agency-information/rules-and-laws/trec-rules

## 7. Daily operating loop

1. Review new prospects.
2. Qualify only those with a legitimate business reason.
3. Research before outreach.
4. Send targeted outreach where appropriate.
5. Log the contact and response.
6. Assign exactly one next action and date.
7. Advance qualified conversations.
8. Apply the compliance gate before any licensing-sensitive step.
9. Move inactive relationships to nurture instead of allowing stale pipeline records.

## 8. Weekly metrics

Track:
- New qualified relationships
- First conversations
- Follow-ups completed
- Opportunities created
- Opportunities advanced
- Opportunities won
- Revenue generated
- Pipeline economic value
- Partner relationships added
- Average time from qualification to opportunity
- Opportunities blocked by compliance/licensing requirements
- Nurture relationships retained

Do not optimize for raw email volume. Optimize for legitimate relationships, qualified opportunities, revenue, and repeatability.

## 9. Market sequencing

Initial operating market: Texas.

Dallas-Fort Worth receives separate tracking because it is a major initial market and current market conditions can differ from the statewide picture.

Expansion into additional Texas markets should follow evidence of repeatable pipeline generation, documented processes, and sufficient operating capacity.

## 10. Source discipline

For every prospect or market claim, preserve the source and date. Prefer official records, company websites, recognized professional organizations, and reputable market-data providers. Never fabricate contact information, property facts, transaction history, or decision-maker status.

## Definition of done
The acquisition engine is operational when:

- Every prospect has a defined relationship type and source.
- Every qualified prospect has a next action.
- Outreach is targeted and auditable.
- Opportunity stages are consistent.
- Licensing-sensitive actions are explicitly gated.
- Follow-ups can be reviewed from Outlook and the operating record.
- Weekly metrics show whether the pipeline is actually producing qualified opportunities and revenue.
