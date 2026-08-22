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
- Design status: proposed D1 principles only. `PORTFOLIO.yaml` must not move to `D1_APPROVED` until explicit founder/orchestrator approval is recorded.

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
