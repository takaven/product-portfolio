# Design Notes

Use `../../DESIGN-SYSTEM.md` as the portfolio-level design governance source.

## Product Direction

LeaseDesk should follow its product boundary and avoid borrowing patterns that imply excluded scope.

## Frontend Gate Rule

No full frontend rollout before D1-D3 are approved.

## Current State

No final product design is created by this operating-repository setup.

## Gate 3/8 - D1 UX Principles

- Authorised issue: #15
- Endpoint: `GATE 3/8 D1 READY FOR ORCHESTRATOR/FOUNDER DESIGN DECISION`
- Design status: approved by founder decision recorded for Issue #15 / PR #16. `PORTFOLIO.yaml` records `D1_APPROVED`.

### Product Personality

LeaseDesk should feel operational, property-oriented and calmly dense. It should help a small commercial landlord see what needs attention without making the product feel like enterprise property-management software.

### Primary User

The primary user is a small commercial landlord or family-owned commercial-property operator who personally manages day-to-day commercial property administration.

This user needs quick operational clarity more than advanced configuration. They are likely moving from spreadsheets, email, WhatsApp and scattered documents, so the interface should reduce mental load rather than expose every possible property-management concept.

### Core Operating Priorities

LeaseDesk should make operational attention obvious in this order:

1. Arrears and overdue rent.
2. Current rent/payment status.
3. Expiring or expired leases.
4. Occupied and vacant units.
5. Tenant and lease record completeness.
6. Missing or important documents.
7. Expenses requiring review.
8. Other operational exceptions.

Dashboard and list surfaces should prioritise exception visibility over decorative analytics. A user should be able to answer "what needs action today?" before exploring secondary reports.

### Navigation Model

Use a simple bounded information architecture:

| Area | UX Role |
| ---- | ------- |
| Overview | Operational command view for exceptions, status totals and immediate follow-up. |
| Properties / building context | Minimal building/property identity and operating context. Do not turn this into enterprise portfolio administration. |
| Units | Store/unit registry with occupancy, tenant link, rent context and vacancy signal. |
| Tenants / leases | Tenant records, lease dates, rent terms, lease status and tenant detail. |
| Payments / arrears | Payment recording, payment history, outstanding amounts and arrears follow-up. |
| Documents | Tenant/lease document metadata and controlled access to uploaded files. |
| Expenses | Property and unit/store expense capture, history and simple categorisation. |
| Reports | Basic operational reporting only: arrears, payments, expenses and lease expiries. |
| Settings | Minimal product/business settings required to operate the account. |

Navigation should stay recognisable and shallow. Avoid nested navigation that implies a broad property suite.

### Density Principles

- Use compact operational tables for records users scan repeatedly: units, tenants, payments, expenses, documents and reports.
- Use summary cards only for high-value totals or exception counts, not as decoration.
- Use exception indicators for arrears, overdue rent, expiring leases, vacant units and missing documents.
- Use detail pages or panels when the user needs full context for a tenant, lease, payment or document.
- Use forms that are direct and work-focused; avoid onboarding-style forms unless they materially reduce setup errors.
- Preserve enough whitespace for legibility, but avoid oversized SaaS dashboard spacing that hides operational information.

### Status Language

Use consistent statuses across dashboard, lists and detail views:

| Status | Meaning |
| ------ | ------- |
| Paid | The expected amount for the relevant period has been received. |
| Partially Paid | Some payment has been recorded, but a balance remains. |
| Outstanding | An expected payment or item remains open. |
| Overdue | An outstanding item is past its due period and should be treated as an exception. |
| Current Lease | Lease is active and not near expiry. |
| Expiring | Lease ends within the governed warning window. |
| Expired | Lease end date has passed. |
| Occupied | Unit/store has an active tenant or active lease relationship. |
| Vacant | Unit/store has no active tenant or active lease relationship. |
| Archived | Record is retained for history but removed from active operational lists. |

Do not freeze detailed microcopy at D1. D2 may refine wording where screen context requires it.

### Safety Principles

- Archive should be the normal record-removal pattern for tenants, leases, units/stores and landlords. Permanent delete should be rare, explicitly guarded and usually avoided for first release.
- Payment corrections should preserve context. Avoid silent overwrites of financially meaningful records.
- Document removal should distinguish hiding/archive from permanent deletion and should respect retention expectations.
- Destructive actions must use clear confirmation and must explain the consequence in business language.
- Demo and production environments must be visually and operationally distinct enough that fictional records cannot be mistaken for customer data.
- Tenant, lease, payment and document information should be treated as sensitive operational data. Lists should reveal enough to operate, while detail views should carry more sensitive context.

### Design Boundaries

LeaseDesk UX must not imply these excluded products:

- Enterprise property-management platform.
- Maintenance ticketing system.
- Online rent-collection/payment processor.
- Advanced accounting suite.
- Tenant marketplace.
- Generic analytics or BI platform.
- Local tax/MRA/TDS workflow as a commercial product surface.

If a future screen pattern would naturally pull the product toward one of these categories, it should be deferred or rejected unless the product boundary is formally changed.

### Existing Interaction Patterns To Preserve

Preserve these existing patterns unless D2 evidence shows they materially fail:

- Overview-first operating dashboard focused on tenants, arrears, lease dates, payments and expenses.
- Tenant detail as the main place to understand lease, payment, arrears and document context.
- Direct add/edit flows for landlords, units/stores, tenants, payments and expenses.
- Payment history and arrears views that show month-by-month status.
- Dashboard cards that link into operational lists rather than decorative charts.
- Bulk import as a practical operational utility, provided it remains safe and bounded.
- Generated receipt/contract ideas as workflow aids, after demo wording and document handling are production-hardened.

### D1 Non-Decisions

- D1 does not approve critical screen layouts.
- D1 does not define component primitives.
- D1 does not authorise frontend rollout.
- D1 does not choose database, authentication, deployment or storage architecture.
- D1 does not authorise changes in `isudally/leasedesk-demo`.
- D1 does not start Gate 4/8.

## Gate 4/8 - D2 Critical Screens

- Authorised issue: #17
- Endpoint: `GATE 4/8 D2 READY FOR ORCHESTRATOR/FOUNDER DESIGN DECISION`
- Design status: proposed D2 critical screens only. `PORTFOLIO.yaml` must not move to `D2_APPROVED` until explicit founder/orchestrator approval is recorded.

### D2 Design Decisions

- Primary navigation should be shallow and operational: Overview, Units, Tenants/Leases, Payments/Arrears, Documents, Expenses, Reports and Settings.
- Overview uses summary cards only for priority totals; operational tables/lists carry the work.
- Tenant / Lease Detail remains a full detail page rather than a lightweight CRM profile.
- Payments & Arrears should operate as a dense financial worklist with drill-down to tenant detail.
- Exceptions should be visible through status labels, counts, overdue indicators and prioritised worklists rather than decorative charts.
- Primary actions should sit close to the record or exception they affect.

### Screen 1/3 - Operational Overview

#### User Objective

The landlord should understand within seconds what needs action today: arrears, overdue/partial payments, expiring leases, vacancies, missing documents and relevant expense exceptions.

#### Layout Structure

```text
Header: Building / account context + primary action

Priority strip:
  Arrears total | Overdue/partial payments | Leases expiring | Vacant units

Main work area:
  Left: Action required list
  Right: Portfolio/unit occupancy summary

Secondary work area:
  Recent payments | Recent expenses | Document/record exceptions

Footer/utility:
  Reports links | Settings link | Demo/production environment marker
```

#### Key Components / Regions

- Building/context header with clear environment marker where relevant.
- Compact priority cards for arrears, payment exceptions, expiring leases and vacancy.
- Action-required table combining the highest priority exceptions.
- Occupancy snapshot showing occupied/vacant units and direct link to Units.
- Recent activity blocks for payments and expenses.
- Document/record exception list for missing or stale tenant/lease documents.

#### Information Hierarchy

1. Exceptions needing action.
2. Financial exposure: arrears and partial/overdue payments.
3. Lease and occupancy risk.
4. Recent operating activity.
5. Secondary reports/settings navigation.

#### Key Actions

- Record payment.
- Open tenant/lease detail.
- Review arrears.
- Review expiring leases.
- Add tenant or unit where appropriate.
- Open payment, expense or document record from exception rows.

#### Statuses / Exceptions Shown

- Paid, Partially Paid, Outstanding, Overdue.
- Current Lease, Expiring, Expired.
- Occupied, Vacant.
- Missing document, stale document, record incomplete.

#### Responsive Behaviour

- Desktop: priority strip plus two-column work area.
- Tablet: priority strip wraps; action list remains first.
- Mobile: single-column stack with action-required list before summary cards.

#### Preserve From Existing Implementation

- Overview-first workflow.
- Dashboard cards linked to operational records.
- Arrears, lease expiry, tenant and expense visibility.
- Direct action patterns for payment and tenant workflows.

#### Material Changes From Existing Implementation

- Reduce demo-dashboard language and fictional context.
- Make the action-required list the main work surface rather than treating all dashboard blocks equally.
- Add clearer occupancy/vacancy and document exception treatment.
- Avoid oversized cards if they push exception lists below the fold.

#### Explicit Exclusions

- No generic analytics dashboard.
- No maintenance-ticket widgets.
- No online rent collection prompts.
- No enterprise multi-property command centre.

### Screen 2/3 - Tenant / Lease Detail

#### User Objective

The landlord should see one tenant's commercial operating record in one place: identity, unit, lease, rent, arrears, payment history, documents, notes and safe corrective actions.

#### Layout Structure

```text
Header:
  Tenant/business identity | Lease status | Payment status | quick actions

Primary detail:
  Left: Tenant + unit + lease terms
  Right: Current rent/payment state + arrears summary

Operational tabs/sections:
  Payment history | Documents | Notes / activity | generated documents

Safety area:
  Archive/correction controls with explicit confirmations
```

#### Key Components / Regions

- Tenant identity and business summary.
- Unit/store link and occupancy context.
- Lease dates, rent terms and lease status block.
- Current payment status and arrears summary.
- Payment history by period.
- Document list with required/available/missing status.
- Notes/activity area for operational context.
- Safe archive/correction controls.

#### Information Hierarchy

1. Tenant, unit and status summary.
2. Lease dates and rent terms.
3. Payment and arrears position.
4. Documents and record completeness.
5. Notes/activity and generated document aids.
6. Archive/correction actions.

#### Key Actions

- Record payment for this tenant.
- Correct payment record with visible context.
- Add or view document.
- Generate receipt or lease document where supported.
- Archive tenant/lease relationship.
- Navigate to unit, payment history or arrears worklist.

#### Statuses / Exceptions Shown

- Current Lease, Expiring, Expired.
- Paid, Partially Paid, Outstanding, Overdue.
- Missing document, document present, document requires review.
- Archived state if record is inactive.

#### Responsive Behaviour

- Desktop: two-column summary with sections below.
- Tablet: summary cards stack into a readable single page.
- Mobile: status summary and primary actions first; long history/document lists collapse into sections.

#### Preserve From Existing Implementation

- Tenant detail as the centre of lease/payment/document context.
- Month-by-month payment and arrears history.
- Links between tenant, landlord and store/unit.
- Receipt/contract generation as workflow aids after hardening.

#### Material Changes From Existing Implementation

- Remove broad CRM feel and keep operational property context primary.
- Standardise mixed status language.
- Move destructive actions into a controlled safety area.
- Treat documents as controlled records rather than demo metadata.

#### Explicit Exclusions

- No broad CRM profile.
- No employee-style people record.
- No advanced legal case-management workflow.
- No tenant portal design.

### Screen 3/3 - Payments & Arrears

#### User Objective

The landlord should scan payment status across tenants, identify overdue or partially paid accounts, record/review payments and move quickly into the relevant tenant record.

#### Layout Structure

```text
Header:
  Period selector | payment action | arrears total

Filters:
  All | Overdue | Partially paid | Outstanding | Paid | Expiring lease context

Primary table:
  Tenant | Unit | Period | Due | Paid | Balance | Status | Last action | Next action

Detail side panel / row expansion:
  Payment history | corrections | notes | tenant link

Footer:
  Basic totals and export/report link if authorised later
```

#### Key Components / Regions

- Period/month selector.
- Status filters.
- Dense payments/arrears table.
- Balance and overdue indicators.
- Row-level action menu for record payment, review history, open tenant.
- Detail expansion or side panel for history and correction context.
- Basic totals for due, paid and outstanding.

#### Information Hierarchy

1. Overdue and partially paid accounts.
2. Outstanding balances for the selected period.
3. Paid/current accounts.
4. Historical context and correction actions.
5. Basic totals/reports.

#### Key Actions

- Record payment.
- Review month/period history.
- Correct a payment without silent overwrite.
- Open tenant/lease detail.
- Filter by status or period.
- Review arrears summary.

#### Statuses / Exceptions Shown

- Paid, Partially Paid, Outstanding, Overdue.
- Balance amount and overdue age where available.
- Current/expiring lease context where it affects urgency.

#### Responsive Behaviour

- Desktop: dense table with optional detail side panel.
- Tablet: table remains primary, with fewer visible columns and row expansion.
- Mobile: priority worklist by exception, with full payment history behind detail rows.

#### Preserve From Existing Implementation

- Payment history and arrears calculations.
- Record payment workflow.
- Tenant drill-down.
- Month-by-month view of obligations and payments.

#### Material Changes From Existing Implementation

- Make Payments & Arrears a single financial worklist rather than scattering status across dashboard and detail only.
- Make corrections explicit and contextual.
- Remove legacy tax/TDS emphasis from the commercial payment screen.
- Prioritise overdue and partial accounts before paid records.

#### Explicit Exclusions

- No online rent collection.
- No accounting ledger replacement.
- No tax/MRA/TDS workflow as a product surface.
- No complex reconciliation engine.

### D2 Coherence Rules

- All three screens must use the same status vocabulary from D1.
- Overview drives users into Tenant / Lease Detail and Payments & Arrears; it should not duplicate every detailed workflow.
- Tenant / Lease Detail is the record of truth for one tenant; Payments & Arrears is the cross-tenant financial worklist.
- Documents appear in Overview only as exceptions, in Tenant / Lease Detail as record context, and in future document surfaces as their own controlled file list.
- Expenses appear in Overview as recent/exception activity and remain a bounded operating area, not accounting software.

### D2 Non-Decisions

- D2 does not approve component primitives.
- D2 does not authorise frontend implementation.
- D2 does not select or change database, authentication, storage, deployment or frontend architecture.
- D2 does not authorise changes in `isudally/leasedesk-demo`.
- D2 does not approve Gate 5/8.
