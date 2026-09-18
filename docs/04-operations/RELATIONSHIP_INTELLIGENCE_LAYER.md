# Relationship Intelligence Layer

## Purpose
Turn individual prospect records into a connected relationship graph that can reveal legitimate referral paths, missing capabilities, and high-value follow-up priorities.

This layer does not assume that a relationship creates revenue. It identifies documented connections that can be researched and developed.

## Relationship nodes
Use the existing Prospect Record Schema for the underlying record. Add relationship edges using:

| Field | Standard |
|---|---|
| From Record ID | Existing record |
| To Record ID | Existing record |
| Relationship Type | Referral, Introduction, Service Provider, Transaction Party, Ownership/Control, Professional Advisor, Industry Association, Project Connection, Other |
| Evidence | Source or message supporting the connection |
| Evidence Date | Date verified |
| Confidence | C0 Unknown, C1 Suggested, C2 Source-verified, C3 Directly confirmed |
| Last Verified | Date |
| Next Action | One concrete action when active |

## Graph rules
1. Never infer a personal relationship solely because two people work in the same industry.
2. Never treat a directory listing as an introduction.
3. A referral becomes a documented edge only when the referral is actually made.
4. A project connection must be supported by a reliable source.
5. Ownership/control relationships require authoritative evidence.
6. Preserve conflicting evidence rather than silently selecting a preferred interpretation.
7. Re-verify time-sensitive relationships before material commercial use.

## Priority signals
The relationship graph should surface:
- Contacts connected to multiple legitimate DFW market segments.
- Introductions that create a new verified relationship.
- Repeated service needs across unrelated prospects.
- Missing capability clusters such as title, insurance, contractors, and property management.
- Market signals connected to an identifiable organization.
- Opportunities where a documented relationship can provide a legitimate next step.

These are research priorities, not predictions of revenue.

## Referral flywheel
Market Signal → Verified Organization → Relationship → Conversation → Introduction → Qualified Relationship → Legitimate Service Need → Opportunity Review → Revenue

A stage cannot be skipped merely because the graph contains many connections.

## Weekly graph review
Review:
1. New verified nodes.
2. New evidence-backed edges.
3. Introductions received or made.
4. Relationship clusters with missing capabilities.
5. Stalled relationships requiring a legitimate reason to reconnect.
6. Compliance-sensitive edges requiring review.
7. Realized revenue attributable to documented relationships.

## Data-quality controls
- Every edge has evidence.
- Every evidence-backed edge has a verification date.
- Unknown relationships remain unknown.
- DNC/opt-out status overrides outreach.
- No graph metric should be presented as revenue unless actual revenue was realized and recorded.