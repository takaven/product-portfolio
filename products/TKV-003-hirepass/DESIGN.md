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

## D3 Pass Component System Proposal

This D3 proposal defines interaction/component primitives only. It does not approve final visual styling, D4 implementation, portfolio-wide visual harmonisation or changes to `takaven/hirepass` source.

### 1. Pass Shell

- **Purpose:** Provide the recognisable external Pass frame for Candidate and Manager experiences.
- **Required content:** recipient identity, role/requisition context, Pass/action state, hiring stage, dominant next action, expiry/access state, secondary details and recent meaningful activity.
- **States/variants:** candidate, manager, active, waiting, action required, expired, revoked, completed.
- **Primary behaviour:** open directly to status plus the next action; keep access/security context visible without dominating the page.
- **Applicability:** Candidate and Manager primary; HR uses related metadata but not the external shell as its main workspace.
- **Mobile behaviour:** single-column hierarchy; identity/state/action above the fold; secondary details collapsible.
- **Source mapping:** ADAPT existing `candidate-portal-pass.tsx`, `manager-recruitment-pass.tsx`, token routes and pass payloads.
- **Anti-patterns:** identical candidate/manager pages with swapped text, full ATS dashboard, decorative card with no workflow value.

### 2. Action Card

- **Purpose:** Centre the one action that matters now.
- **Required content:** action title, why it matters, deadline/urgency, required context, primary action, optional justified secondary action, completion/error feedback.
- **States/variants:** action required, waiting, upcoming, completed, unavailable, expired.
- **Primary behaviour:** one dominant action per card; successful action visibly changes Pass state.
- **Applicability:** Candidate, Manager and HR exception/action rows.
- **Mobile behaviour:** primary action reachable without scrolling where practical; sticky action only when the page is long and action remains current.
- **Source mapping:** ADAPT existing interview booking, document upload, message, offer response, JD approval, shortlist/reject and evaluation actions.
- **Anti-patterns:** multiple competing primary buttons, dashboard action grids, silent completion.

### 3. Pass State System

- **Purpose:** Separate access/action state from hiring-stage status.
- **Required content:** Pass/action state plus hiring stage shown together but visually distinct.
- **States/variants:** `ACTION REQUIRED`, `WAITING`, `UPCOMING`, `COMPLETED`, `EXPIRED`, `REVOKED`; hiring stages Application, Screening, Interview, Assessment, Decision, Offer, Handoff.
- **Primary behaviour:** Pass/action state drives urgency and primary action; hiring stage provides process context.
- **Applicability:** Candidate, Manager and HR.
- **Mobile behaviour:** compact state block near top; avoid multi-colour overload.
- **Source mapping:** ADAPT existing pass/candidate statuses, token expiry/active flags and stage data.
- **Anti-patterns:** status proliferation, using green for every positive state, confusing stage with action need.

### 4. Journey / Progress

- **Purpose:** Show where the candidate/requisition is without exposing internal detail.
- **Required content:** completed stages, current stage, likely next stage and waiting/action ownership.
- **States/variants:** not started, current, completed, skipped/not applicable, blocked.
- **Primary behaviour:** answer “where am I in the process?” quickly.
- **Applicability:** Candidate primary; HR and Manager secondary.
- **Mobile behaviour:** horizontal compact stepper or stacked short list; long history hidden behind details.
- **Source mapping:** ADAPT existing candidate timeline, passCandidate status and hiring-stage data.
- **Anti-patterns:** enterprise workflow map, internal scoring/rank detail, dense timeline as first screen.

### 5. Decision Card

- **Purpose:** Let managers make one structured hiring decision without navigating elsewhere.
- **Required content:** required decision, relevant evidence, urgency/deadline, structured options, confirmation and post-submit state.
- **States/variants:** approve/request changes, shortlist/reject, evaluation rating, final hire/no-hire, pending confirmation, completed.
- **Primary behaviour:** decision surface plus confirmation; update Manager Pass and HR queue after completion.
- **Applicability:** Manager primary; HR sees resulting decision state.
- **Mobile behaviour:** evidence summary first, decision controls next, confirmation in sheet/dialog where useful.
- **Source mapping:** ADAPT manager JD, shortlist/reject, evaluation and final decision endpoints; REBUILD evidence compression.
- **Anti-patterns:** full candidate profile before action, multi-page decision flow, free-text-only decisions.

### 6. Evidence Summary

- **Purpose:** Show only the evidence needed for the current manager decision.
- **Required content:** candidate summary, role fit evidence, CV/profile highlights, interview/evaluation summary, decision-relevant documents.
- **States/variants:** compact, expanded, missing evidence, confidential/internal-only.
- **Primary behaviour:** progressive disclosure from summary to detail.
- **Applicability:** Manager primary; HR secondary; Candidate must not see internal-only evidence.
- **Mobile behaviour:** summary chips/cards with expandable details.
- **Source mapping:** ADAPT candidate profile, documents, interviews, evaluations and offers; REBUILD filtering/visibility rules.
- **Anti-patterns:** dumping entire ATS record, leaking manager notes to candidate, analytics-first evidence.

### 7. Interview Primitives

- **Purpose:** Handle interview scheduling and status clearly for each role.
- **Required content:** available slots, selected slot, confirmed interview, upcoming interview, completed interview, cancellation/reschedule state where justified.
- **States/variants:** choose slot, confirm attendance, scheduled, completed, unavailable, reschedule requested.
- **Primary behaviour:** Candidate books/confirm slots; Manager provides availability/preparation; HR monitors completion.
- **Applicability:** Candidate, Manager and HR.
- **Mobile behaviour:** slot cards, clear date/time hierarchy, one-tap selection plus confirmation.
- **Source mapping:** ADAPT existing interviewSlots, booking endpoint, interview setup and interview records.
- **Anti-patterns:** calendar-heavy desktop-only UI, hidden time zone/context, no confirmation state.

### 8. Document Primitives

- **Purpose:** Make requested documents feel controlled and purposeful, not like a generic file manager.
- **Required content:** request, required/optional label, upload state, received state, rejected/replacement requested state, secure access/download state.
- **States/variants:** requested, uploading, received, approved, rejected, replacement needed, unavailable.
- **Primary behaviour:** show why the document is needed, current status and next action.
- **Applicability:** Candidate primary; HR reviews/requests; Manager may see decision-relevant documents only.
- **Mobile behaviour:** one document per card; upload progress and error recovery visible.
- **Source mapping:** ADAPT candidateDocuments and document upload endpoints; later security hardening required before broad release.
- **Anti-patterns:** generic folder UI, unclear required status, exposing documents across candidates/roles.

### 9. Message / Update Primitive

- **Purpose:** Communicate process updates without becoming a chat product.
- **Required content:** update type, sender/context, timestamp, action link if relevant and read/acknowledged state.
- **States/variants:** action-triggering update, informational update, recent status change, read/unread.
- **Primary behaviour:** updates either explain state change or direct the user to an action.
- **Applicability:** Candidate and HR primary; Manager secondary.
- **Mobile behaviour:** compact recent update near top; older updates in collapsible history.
- **Source mapping:** ADAPT candidateMessages, notifications and timeline events.
- **Anti-patterns:** full chat platform, noisy message feed, status changes buried in free text.

### 10. Access / Security Primitives

- **Purpose:** Make the Pass feel issued, personal, time-bound, controlled and traceable.
- **Required content:** Pass identity, recipient identity, role/requisition, expiry indicator, revoked/expired state, access problem state, secure-document warning where appropriate.
- **States/variants:** valid, expiring soon, expired, revoked, invalid token, secure document access.
- **Primary behaviour:** external users understand access status without seeing technical errors.
- **Applicability:** Candidate, Manager and HR.
- **Mobile behaviour:** compact security/access strip; expired/revoked states replace normal actions.
- **Source mapping:** PRESERVE active/expiry token mechanics; ADAPT token error pages and access metadata; NEW clearer user-facing states.
- **Anti-patterns:** raw 404/500 errors, treating token as ordinary URL, overexposing internal security detail.

### 11. HR Control Primitives

- **Purpose:** Give HR an operational view of external action health.
- **Required content:** Pass queue/table, stalled-action indicator, candidate-awaiting-action, manager-awaiting-action, issue Pass, resend/nudge, revoke, extend expiry, activity summary and exception state.
- **States/variants:** active, stalled, overdue, waiting, completed, expired, revoked, exception.
- **Primary behaviour:** sort/filter by who must act next and let HR control the Pass lifecycle.
- **Applicability:** HR primary.
- **Mobile behaviour:** desktop-primary, responsive support; tables acceptable internally.
- **Source mapping:** ADAPT existing pass lists, link creation, activity log and analytics; NEW nudge/revoke/extend/stalled detection workflow.
- **Anti-patterns:** forcing external Pass-card metaphor into HR table workflows, full ATS analytics console.

### 12. Feedback / Transition States

- **Purpose:** Make completed actions and state changes visible and confidence-building.
- **Required content:** action submitted, decision completed, interview booked, document received, moved to waiting, new action assigned, Pass completed, expired/revoked.
- **States/variants:** success, waiting transition, next action assigned, no further action, error/retry.
- **Primary behaviour:** confirm what changed and who owns the next step.
- **Applicability:** Candidate, Manager and HR.
- **Mobile behaviour:** inline confirmation or lightweight sheet; no decorative motion unless it clarifies state transition.
- **Source mapping:** NEW/ADAPT from existing mutation success states and status payloads.
- **Anti-patterns:** animation without meaning, toast-only confirmation for material decisions, unclear next owner.

### 13. Empty / Loading / Error States

- **Purpose:** Prevent external users from encountering raw technical or confusing states.
- **Required content:** loading Pass, invalid token, expired Pass, revoked Pass, no action required, no upcoming event, failed upload, failed decision submission, stale/outdated state.
- **States/variants:** loading, empty, invalid, expired, revoked, retryable failure, non-retryable access failure.
- **Primary behaviour:** explain state in human terms and provide the safest next step.
- **Applicability:** Candidate, Manager and HR.
- **Mobile behaviour:** full-width focused state with one safe action where possible.
- **Source mapping:** ADAPT existing route error handling and loading states; NEW consistent external error language.
- **Anti-patterns:** stack traces, raw API messages, dead-end expired/revoked pages without context.

### 14. Mobile Action Behaviour

- **Purpose:** Keep external Pass participation usable one-handed on mobile where practical.
- **Required content:** dominant action placement, sticky action rules, collapsible detail sections, modal/sheet usage, long-document handling, timeline/history behaviour and confirmation flows.
- **States/variants:** short action, long form, document upload, decision confirmation, read-only waiting state.
- **Primary behaviour:** primary action remains easy to find; secondary detail does not compete with it.
- **Applicability:** Candidate and Manager primary; HR responsive support only.
- **Mobile behaviour:** top identity/state/action hierarchy; bottom sticky action only for persistent current action; sheets for confirmation/detail.
- **Source mapping:** REBUILD external Pass layout patterns while preserving existing data/actions.
- **Anti-patterns:** desktop sidebar dependence, tiny table controls, multi-tab navigation before action.

## D3 Brand / Visual Use

Use only the governed Takaven palette. Electric Signal Green should mark meaningful active/primary/high-signal action or state, not generic success everywhere. Soft Graphite, Titanium Grey, Deep Support Charcoal, Soft Mist and White should provide controlled premium structure, readable contrast and restrained density. Decorative effects must remain subordinate to identity, status, progress, urgency, transition and action confirmation.

## D3 Source Reuse Summary

- **PRESERVE:** token-based Candidate/Manager access, pass/candidate/manager data models, pass creation/link generation, core routes and source baseline.
- **ADAPT:** existing Candidate Pass page, Manager Pass page, interview slots, evaluations, documents, messages, offers, timeline, activity log and status payloads.
- **REBUILD:** external Pass layout hierarchy, manager evidence compression, HR action queue/workspace, mobile action placement and consistent state/error language.
- **NEW:** nudge/revoke/extend control workflow, stalled-action detection, state-transition feedback model, controlled access presentation and one-dominant-action composition.
