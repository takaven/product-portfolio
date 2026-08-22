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

## D2 Critical Experience Definition

This D2 proposal defines critical experiences only. It does not approve component primitives, final styling, frontend implementation or changes to `takaven/hirepass` source.

### Candidate Pass

**Purpose:** Give the candidate one controlled mobile-first place to understand their hiring status, what is required from them and what happens next.

**Opening State:** Candidate identity and role context, Pass/action state, one dominant next action, hiring-stage progress and next event or waiting message.

**Information Hierarchy:**

1. Candidate / role identity
2. Current Pass/action state
3. Dominant next required action
4. Hiring-stage progress
5. Next scheduled event or employer-side waiting state
6. Requested documents/tasks
7. Recent HR update or message
8. Secondary timeline/history/details

**Primary Actions:**

- Choose or confirm interview slot
- Upload requested document
- Complete assessment
- Reply to HR
- Review offer
- Accept, decline or request discussion
- Acknowledge waiting/no-action state

**Secondary Information:** Full timeline, older messages, document history, interview details, offer details and pass/access metadata should be progressively disclosed below the primary action surface.

**Important States:** Action required, waiting on employer, interview upcoming, documents pending, assessment pending, offer issued, completed/hired, expired, revoked.

**Existing Source Mapping:**

| Capability | Mapping | Evidence |
| ---------- | ------- | -------- |
| Token Candidate Pass route | PRESERVE | `/candidate-pass/:token`, `/api/candidate-pass/:token` |
| Candidate/pass/role context | PRESERVE | candidate/pass/passCandidate payload returned by route |
| Interview slot booking | ADAPT | existing slot booking endpoint and `candidate-portal-pass.tsx` action |
| Candidate messages | ADAPT | candidate message endpoints and schema |
| Candidate documents | ADAPT | candidate document endpoints/schema; needs later secure document hardening |
| Timeline/progress | ADAPT | candidate timeline events exist but need stronger next-action hierarchy |
| Offer response | ADAPT | offer-response endpoint exists; D3/D4 should simplify visible decision surface |
| Emotional reassurance / waiting clarity | NEW | current source has data, but not the required uncertainty-reduction model |

**Anti-Patterns:** Internal scoring, manager comments, rankings, analytics, generic tabs-first candidate portal, full application dashboard, hidden next action.

**"WOW" Interaction:** The Pass opens to one clear live state and one dominant action. After the candidate acts, the Pass visibly changes to show whether the next wait is on the employer, manager or candidate.

### Manager Pass

**Purpose:** Let a hiring manager complete required hiring decisions with minimal friction and no need to learn an ATS.

**Opening State:** Manager identity/context, the decision required now, deadline/urgency, candidate or requisition evidence needed for that decision and one primary decision action with confirmation.

**Information Hierarchy:**

1. Required decision and urgency
2. Role/requisition context
3. Candidate or JD evidence summary
4. Recommended structured decision options
5. Upcoming interview/action context
6. Supporting CV/profile/evaluation details
7. Prior activity/history

**Primary Actions:**

- Approve or request changes to hiring request/JD
- Shortlist or reject candidate
- Select interview availability
- Prepare for interview
- Submit structured evaluation
- Make final hiring decision

**Secondary Information:** CV/profile detail, prior evaluation summary, outstanding questions, interview schedule context, candidate history and access/activity metadata.

**Important States:** Decision required, waiting on candidate, interview preparation, evaluation overdue, final decision pending, no action required, expired, revoked.

**Existing Source Mapping:**

| Capability | Mapping | Evidence |
| ---------- | ------- | -------- |
| Token Manager Pass route | PRESERVE | `/manager-pass/:token`, `/api/manager-pass/:token` |
| JD approval / change request | ADAPT | manager-pass approve/request endpoints exist |
| Candidate shortlist/reject | ADAPT | manager-pass candidate action endpoints exist |
| Interview setup/availability | ADAPT | manager interview setup and slot data exist |
| Structured evaluation | ADAPT | manager evaluation endpoint and evaluation schema exist |
| Final decision | ADAPT | final-decision endpoint exists; needs clearer one-surface confirmation model |
| Decision-relevant evidence | REBUILD | existing source leans portal/dashboard; D2 requires decision-surface compression |
| Low-friction manager completion state | NEW | completion feedback should explicitly show HR no longer needs action |

**Anti-Patterns:** Multi-page ATS navigation, full candidate database, deep menus, broad analytics, account-training burden, manager dashboard clutter.

**"WOW" Interaction:** A manager receives one decision surface, completes the decision, and immediately sees a clear "HR has what it needs" state.

### HR Pass Control / Hiring Action Workspace

**Purpose:** Give HR operational control over external hiring actions so they can see, nudge and resolve work without manual chasing.

**Opening State:** Prioritised action queue showing stalled Passes, outstanding candidate actions, outstanding manager decisions, upcoming deadlines/interviews and recent meaningful activity.

**Information Hierarchy:**

1. Exceptions and stalled actions
2. Candidate actions outstanding
3. Manager decisions outstanding
4. Upcoming interviews/deadlines
5. Active Pass health/status
6. Recently completed actions
7. Expired/revoked/completed history

**Primary Actions:**

- Issue Pass
- Resend/nudge
- Pause where appropriate
- Revoke
- Expire or extend
- Inspect activity
- Resolve exception
- Open candidate or manager context

**Secondary Information:** Full activity log, pass metadata, candidate/manager history, document state, offer/onboarding handoff context and settings.

**Important States:** Action required, stalled, overdue, upcoming, active, waiting, completed, expired, revoked, exception.

**Existing Source Mapping:**

| Capability | Mapping | Evidence |
| ---------- | ------- | -------- |
| Pass creation / candidate linking | PRESERVE | passes, pass candidates and link-generation routes exist |
| Candidate and manager link issuing | ADAPT | candidate link and share link routes exist |
| Activity and pass monitoring | ADAPT | activity log and analytics routes exist but need action-queue framing |
| Nudge/resend/expiry/revocation | NEW | link activity/active/expiry fields exist; control actions need productised workflow |
| Stalled-action detection | NEW | source has underlying dates/statuses but not a focused stalled-action model |
| HR action workspace | REBUILD | current internal views are broader ATS-like pages; D2 requires external workflow control focus |

**Anti-Patterns:** Full ATS command centre, analytics-first dashboard, unrelated HRIS features, broad admin settings, manual chase notes replacing action-state tracking.

**"WOW" Interaction:** HR sees exactly who is blocking progress and can nudge or revoke/extend the relevant Pass from the same control surface.

## Cross-Experience Flow

HR issues a Candidate Pass for a shortlisted applicant. The candidate opens the Pass, sees `ACTION REQUIRED`, chooses an interview slot and receives a live `UPCOMING` state. HR sees the candidate action complete and the manager decision become the next blocker. The manager receives a Manager Pass showing the candidate evidence and one structured evaluation action. After the manager submits the evaluation, the candidate Pass changes to `WAITING` with a clear employer-side message, while HR sees the workflow advance to the next decision state.

## D2 Visual Direction Concept

HirePass should make identity and state prominent before navigation. External Passes should use controlled density, one dominant action, strong status hierarchy and selective Electric Signal Green for meaningful action/state moments. Motion should be minimal and purposeful, used only to confirm state transitions or completed actions. The Pass should be recognisable as an issued, personal, time-bound object without relying on decorative card tricks.
