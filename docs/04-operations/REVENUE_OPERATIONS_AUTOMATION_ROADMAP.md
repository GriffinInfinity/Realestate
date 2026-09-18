# Revenue Operations Automation Roadmap

## Purpose
Define the sequence for automating the Realestate operating system without automating unsupported assumptions or regulated activity.

## Automation tiers
### Tier 0 — Data integrity
Automate:
- Required-field checks.
- Duplicate detection.
- DNC/opt-out flag propagation.
- Stale-source detection.
- Missing next-action detection.
- Date and status consistency checks.

### Tier 1 — Queue management
Automate:
- Daily research queue generation.
- Follow-up queue generation from documented next actions.
- Compliance-review queue visibility.
- Opportunity-aging alerts.
- Weekly management metric preparation.

### Tier 2 — Intelligence assistance
Automate:
- Candidate discovery from approved public sources.
- Source/date capture.
- Research summaries.
- Record enrichment suggestions.
- Relationship-edge suggestions that require evidence validation.
- Opportunity routing suggestions.

Automation at this tier proposes changes; it does not silently convert uncertain information into verified facts.

### Tier 3 — Communication assistance
Automate:
- Draft preparation using verified record data.
- Personalization from documented business reasons.
- Reply classification.
- Suggested next actions.
- Conversation and introduction extraction.

Commercial messages must continue to follow the outreach standard, including DNC/opt-out controls and required disclosures.

### Tier 4 — Controlled execution
Only authorized, low-risk actions should execute automatically after the required gates are satisfied.

Examples:
- Calendar task creation.
- Internal status updates.
- Non-material record maintenance.
- Internal reporting.

Regulated brokerage activity, contractual commitments, financial commitments, or actions requiring specific authority remain gated.

## Automation decision matrix
| Action | Automation posture |
|---|---|
| Detect missing CRM fields | Automatic |
| Detect duplicate candidates | Automatic suggestion |
| Flag overdue next action | Automatic |
| Prepare internal report | Automatic |
| Research public market signal | Automatic with source capture |
| Suggest prospect qualification | Human/data-quality gate |
| Draft commercial email | Prepare for authorized execution |
| Send commercial outreach | Controlled execution with compliance checks |
| Change DNC/opt-out to suppress outreach | Immediate automatic suppression |
| Classify licensing-sensitive activity | Flag for review |
| Perform regulated brokerage action | Authorization required |
| Sign agreement | Human authorization required |
| Commit company funds | Human authorization required |
| Record realized revenue | Evidence required |

## Daily control loop
1. Load current records.
2. Validate required fields and statuses.
3. Apply DNC/opt-out suppression.
4. Identify overdue and upcoming actions.
5. Refresh approved market-intelligence sources.
6. Route new candidates through verification.
7. Surface compliance-review items.
8. Prepare authorized outreach/replies.
9. Record outcomes.
10. Recalculate operational metrics.
11. Produce the next-day priority queue.

## Failure handling
When automation encounters uncertainty:
- Preserve the existing verified record.
- Mark the disputed field as Needs Review.
- Preserve the source and date.
- Do not invent a value.
- Do not advance the opportunity solely because automation failed to disprove it.
- Route the item to the appropriate review queue.

## Auditability
Every automated material change should preserve:
- Record affected.
- Action performed.
- Date/time.
- Source or triggering event.
- Previous value when materially changed.
- New value.
- Automation or operator responsible.
- Review status when required.

## Rollout principle
Build automation incrementally. Each tier should operate reliably before the next tier is enabled.

The goal is not maximum automation. The goal is maximum reliable operating leverage while preserving evidence, compliance, human control and business accuracy.

## Definition of done
The automation roadmap is production-ready when each recurring workflow has:
- A defined input.
- A deterministic gate.
- A documented output.
- An exception path.
- An audit trail.
- A clear authorization boundary.