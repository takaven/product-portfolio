# Product Definition

Canonical state lives in `../../PORTFOLIO.yaml`.

## Promise

A secure hiring pass workflow that lets HR, managers and candidates complete hiring steps through controlled external links.

## Buyer

HR lead or founder at a 20-150 employee company hiring regularly.

## Problem

Hiring decisions, candidate documents, interviews and manager feedback are scattered across email, WhatsApp and manual follow-up.

## Product Boundary

- hiring requests and positions
- candidate records
- Candidate Pass
- Manager Pass
- interview workflow
- structured evaluations
- candidate documents
- candidate journey and status
- offer-related workflow where materially implemented
- onboarding handoff

## Explicit Exclusions

- full enterprise ATS
- job-board marketplace
- recruitment agency CRM
- payroll
- employee lifecycle management
- broad HRIS
- TeamFrame functionality after employment begins

## Relationship To TeamFrame

complementary; possible later integration at hire-to-employee handoff

## Remarks

HirePass product/code programme is complete through Gate 8/8 and the final governed source baseline is takaven/hirepass main at 75b6df109a67542ee1bd7126b34c4cb758df059f. Signature Pass experience is achieved through the recurring Pass State contract (Now, Your Action, Waiting On, Next, Expected Movement), visible Pass Handoff across Candidate, Hiring Manager and HR workflow transitions, final release-quality cleanup and browser-rendered visual signature acceptance. Candidate Pass and Manager Pass are commercially strong; HR Pass Control is commercially usable. Product thesis: HirePass is the hiring process that tells everyone when it is their turn. Candidate promise: No more recruitment silence. Product remains a secure external hiring workflow centred on Candidate Pass, Manager Pass and HR Pass Control; do not describe or expand it as a generic ATS. Production release and deployment are NOT STARTED and require founder approval plus production PostgreSQL/schema, strong session secret, admin username/password hash, persistent upload storage, HTTPS/domain/runtime configuration, backups and final production smoke verification. TeamFrame integration remains a future separate decision. Final portfolio-wide UI harmonisation remains deferred. Repository is public temporarily by founder instruction for live review and should be made private after execution.

## Product Principles

### Pass concept

- Status: `REQUIRED`
- Description: HirePass must preserve distinct controlled external passes such as Candidate Pass and Manager Pass.
- Governance rule: Do not dilute the Pass concept into generic portal terminology or freeze detailed terminology without the relevant design/product gate.
- Provisional terms: Issue Pass, Open Pass, Revoke Pass, Pass Status, Pass Activity

### Pass-first product model

- Status: `REQUIRED`
- Description: External participants should primarily experience HirePass through controlled role-specific Passes, while HR uses an internal operational workspace.
- Governance rule: Do not turn Candidate Pass or Manager Pass into generic dashboards, ATS portals or ordinary CRUD workspaces.
- Provisional terms: Candidate Pass, Manager Pass, HR Pass Control

### Next action first

- Status: `REQUIRED`
- Description: Every Pass opening state should immediately show current status, what needs attention, what can be done now and what happens next.
- Governance rule: Do not require candidates or managers to interpret an administrative dashboard before taking the next useful action.
- Provisional terms: Action Required, Waiting, Completed, Expired, Revoked

### Controlled access

- Status: `REQUIRED`
- Description: A Pass is a controlled-access object with expiry, revocation, role-specific visibility, least-necessary information, traceability and secure document handling.
- Governance rule: Do not treat Pass links as merely shareable URLs or expose cross-candidate/internal recruitment information through external Passes.
- Provisional terms: Issue Pass, Expire Pass, Revoke Pass, Pass Activity

