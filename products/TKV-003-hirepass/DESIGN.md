# Design Notes

Use `../../DESIGN-SYSTEM.md` as the portfolio-level design governance source.

## Product Direction

HirePass should follow its product boundary and avoid borrowing patterns that imply excluded scope.

## Frontend Gate Rule

No full frontend rollout before D1-D3 are approved.

## Current State

No final screen design is approved yet. D1 product/UX principles are proposed below for orchestrator/founder review before D2 critical-screen exploration begins.

## D1 Product / UX Principles

### 1. Pass-First Product Model

HirePass is organised around controlled role-specific Passes. Candidates and hiring managers should primarily experience HirePass through Candidate Pass and Manager Pass surfaces, while HR uses a conventional internal workspace to issue, monitor and control those Passes.

### 2. Next Action First

Every external Pass should answer immediately: where the person is in the process, what is happening, what needs attention, what action is available now and what happens next. The user should not have to interpret a dashboard before acting.

### 3. Candidate Pass

Candidate Pass should reduce uncertainty without exposing unnecessary internal recruiting information. It should prioritise current hiring status, journey/progress, next required action, interview details, requested documents, messages or updates, offer response where applicable and clear reassurance that the process is active and controlled.

### 4. Manager Pass

Manager Pass should make participation exceptionally low-friction. It should prioritise pending decisions, the evidence required for each decision, JD/requisition approval where relevant, shortlist/reject actions, interview availability/preparation, structured evaluation and final hiring decision. A manager should not need to learn HirePass as a system.

### 5. HR Control

HR must be able to issue, expire, revoke, monitor and nudge Passes; identify stalled actions; understand outstanding candidate and manager steps; and preserve auditability. HR should not need manual chasing to discover whether an action is complete.

### 6. Pass State Model

HirePass should keep Pass/action state simple and separate from hiring-stage status. Hiring-stage status describes where the candidate/requisition is in recruitment. Pass/action state describes the external access object and current user action need.

Proposed Pass/action states:

- Active
- Action Required
- Waiting
- Completed
- Expired
- Revoked

### 7. Controlled Access

A Pass is a controlled-access object, not merely a shareable URL. D2 and later architecture must preserve expiry, revocation, least-necessary information, role-specific visibility, access traceability, secure document interaction and protection against accidental cross-candidate exposure.

### 8. Mobile-First External Experience

Candidate Pass and Manager Pass must work naturally on mobile. The primary action should be reachable without desktop navigation patterns, and the design must not shrink an ATS dashboard onto a phone.

### 9. Progressive Disclosure

External Passes should show only what is needed for the current decision or stage. Avoid internal recruitment data, unnecessary tabs, analytics, historical clutter and administrative controls in candidate or manager surfaces.

### 10. Memorable Without Gimmicks

HirePass should feel memorable because it makes hiring participation dramatically simpler. Motion, card treatment, QR/wallet concepts and live updates may be explored later only if they reinforce status, identity, progress, urgency, transition or action confirmation. The interaction model must remain valuable with animations removed.

## Product Personality

HirePass should be sharper than TeamFrame, identity/status-driven, confident, controlled, premium, immediate and modern without becoming playful or futuristic theatre. It should use the Takaven palette conceptually through restrained graphite/charcoal structure, clear status contrast and selective Electric Signal Green for action/status moments. No new master brand colours are introduced by D1.

## D2 Critical Experiences To Explore

1. Candidate Pass
2. Manager Pass
3. HR Pass Control / Hiring Action Workspace

These are D2 targets only. This D1 record does not approve wireframes, final visual design, frontend implementation or portfolio-wide visual harmonisation.
