# Decisions

Append only material decisions for LeaseDesk.

## 2026-08-20 - Initial Portfolio Record

- Status: `REVIVAL_IN_PROGRESS`
- Priority: `P0`
- Current execution gate: Commercial-product completion after validation/demo readiness.
- Evidence confidence: `VERIFIED`

## 2026-08-22 - Gate 2/8 Completion Gap Audit And Scope Lock

- Authorised issue: #13
- Source inspected: `isudally/leasedesk-demo` at `224a49196167ed77d0f0882f7e438f39ad7a0f5f`.
- Scope decision: preserve the existing LeaseDesk implementation as the production foundation where it already supports the governed commercial workflow. Do not rebuild functioning areas for architectural preference.
- Product boundary remains unchanged: small commercial landlord operations for units/stores, tenants, leases, payments, arrears, documents, expenses and basic reporting/settings.
- Gate 2 endpoint: `GATE 2/8 COMPLETE - READY FOR ORCHESTRATOR REVIEW`.

### Governed Area Assessment

| Area | Classification | Evidence / Decision |
| ---- | -------------- | ------------------- |
| Properties / buildings | `PARTIAL` | Building identity exists through settings and demo defaults, but there is no production-ready building/property configuration flow. Keep single-building simplicity for release; do not expand into enterprise multi-property management. |
| Units / stores | `COMPLETE / materially usable` | Store schema, API routes, list/detail UI, add/edit forms and bulk upload support exist. Add only low-cost occupancy clarity if needed during implementation. |
| Tenants | `COMPLETE / materially usable` | Tenant schema, API routes, add/edit workflow, tenant detail page and landlord/store links exist. Preserve the workflow. |
| Leases | `PARTIAL` | Lease dates, rent, contract fields, renewal UI and generated lease/receipt assets exist, but document generation still contains demo/local wording and needs production hardening. |
| Payments / rent status | `PARTIAL` | Payment recording, monthly history, receipts and dashboard totals exist, but the implementation is demo-storage backed and contains legacy TDS/tax calculation paths that must not define V1. |
| Arrears | `COMPLETE / materially usable` | Tenant-level and portfolio arrears calculations and displays exist. Add regression tests before release because arrears is commercially central. |
| Documents | `PARTIAL` | Document metadata routes and UI exist, but real upload/download/storage, file permissions and retention are not production-ready. |
| Expenses | `COMPLETE / materially usable` | Expense schema, API routes, add/edit workflow, filters and dashboard totals exist. Preserve the workflow. |
| Basic reporting / settings | `PARTIAL` | Dashboard, payments, expenses and setting retrieval exist. Production settings remain minimal and should stay bounded. |

### Production Foundation Findings

| Area | Classification | Release Decision |
| ---- | -------------- | ---------------- |
| Authentication / account model | `MISSING` | Must be implemented before any external commercial release. A simple owner/admin account model is enough for first release; do not create enterprise roles unless separately authorised. |
| User / role requirements | `PARTIAL` | A users table and demo user exist, but no production authorisation model is implemented. First release only needs founder/customer admin access and record ownership protection. |
| Database / storage architecture | `MISSING` | The source uses in-memory `DemoStorage`; Drizzle/Neon schema exists but is not the active persistence path. Production persistence is the largest technical blocker. |
| Live/demo storage separation | `PARTIAL` | The demo is intentionally isolated, but production must explicitly separate demo seeds from customer data and must not rely on in-memory storage. |
| Environment variables / secrets | `PARTIAL` | `DATABASE_URL` handling exists in database config, but runtime validation and documented production/demo environment modes are required. No secret values were copied into this repository. |
| Document / file handling | `MISSING` | Current documents are metadata/demo placeholders or local UI-only uploads. Production needs controlled file storage, download permissions and deletion/retention rules. |
| Destructive actions | `PARTIAL` | Server deletes are disabled for the demo, while frontend delete/archive flows still exist. Production needs a deliberate archive/correction model and guarded destructive actions. |
| Validation / error handling | `PARTIAL` | Zod schemas and basic API errors exist, but critical workflows need stronger validation and user-facing error states. |
| Logging / auditability | `MISSING` | Payment, document and record-change activity should have basic audit trails before release. This should remain lightweight. |
| Deployment dependencies | `PARTIAL` | Build/start scripts exist, but deployable production configuration, health checks and environment setup are not locked. |
| Tests / CI | `MISSING` | No source-level test suite was found in the pinned source. Add focused workflow checks rather than broad test theatre. |
| Privacy / security | `PARTIAL` | Demo data is fictional and no copied source data was identified in the control repo. Commercial release still requires auth, storage permissions, and removal or hard disabling of demo-only paths. |

### Demo-Derived Items To Replace Or Harden

- In-memory seeded data in `server/storage.ts`.
- Demo user/password and validation-demo notes.
- `Riverton Market Plaza` and related fictional defaults embedded in UI/storage/import examples.
- Footer/banner wording that says validation demo or fictional data.
- Placeholder document URLs and metadata-only document flows.
- Demo-disabled delete/archive responses.
- Lease and receipt generators containing validation-demo footers.
- Legacy local tax/TDS paths that are not part of the governed product boundary.

### Commercial Release Scope

#### MUST COMPLETE BEFORE RELEASE

1. Replace demo in-memory storage with production persistence while preserving the existing schema/workflow intent.
2. Implement a minimal authenticated owner/admin access model with record-level protection appropriate for first release.
3. Create explicit demo/production data separation so fictional demo records cannot become production defaults.
4. Implement production document storage for tenant/lease files, including access control and safe removal/retention behaviour.
5. Replace demo delete-disable behaviour with a bounded archive/correction model for tenants, stores, landlords, documents, expenses and payment corrections.
6. Remove or hard-disable demo-only labels, fictional defaults, validation footers and legacy tax/TDS routes from the production path.
7. Add focused workflow validation and regression checks for tenants, units, leases, payments, arrears, documents and expenses.
8. Define deployable runtime configuration, environment validation and a basic health/check path.

#### SHOULD COMPLETE IF LOW COST

- Clean mixed English/French UI labels in the commercial workflow.
- Add clearer occupancy/vacancy signals on the units/stores surface.
- Add a minimal settings screen for building/business display details.
- Add lightweight activity history for payment and document changes if it can be done without creating a broad audit product.

#### POST-LAUNCH / DEFER

- Multi-property portfolio architecture beyond the first bounded commercial release.
- Advanced reporting beyond dashboard, arrears, payments and expenses.
- Accounting exports/integrations.
- Granular role hierarchy beyond first-release owner/admin access.

#### OUT OF SCOPE

- Enterprise property management.
- Online rent collection.
- Maintenance ticketing.
- Advanced accounting.
- Tenant marketplace.
- Mauritius-specific MRA/TDS workflows as a product surface.

### Proposed Gate 6/8 Implementation Slices

| Slice | Objective | Affected Product Areas | Acceptance Endpoint | Dependencies | Independent Review |
| ----- | --------- | ---------------------- | ------------------- | ------------ | ------------------ |
| Slice 1/5 | Replace demo storage with production persistence and explicit demo/production modes. | Database/storage, settings, landlords, stores, tenants, payments, expenses, documents metadata. | Core records persist across restart; demo seeds are opt-in only. | Gate 3/8 and Gate 4/8 constrain UX/design only; technical path remains a Gate 6 implementation decision. | No standalone review; combine with Slice 2. |
| Slice 2/5 | Add minimal authenticated owner/admin access and record protection. | Authentication, authorisation, routes, frontend session states. | Unauthenticated users cannot access operational data; authorised admin can use the core workflow. | Slice 1 persistence decisions. | Required: Independent Foundation/Security Review covering Slices 1+2. |
| Slice 3/5 | Harden core operating workflows without redesign. | Units/stores, tenants, leases, payments, arrears, expenses, dashboard. | Main commercial demo and first-customer workflow operates on production data with consistent totals and errors. | Slices 1-2. | No automatic independent review if tests/CI pass and no BLOCKING/MATERIAL evidence appears. |
| Slice 4/5 | Implement production document handling and safe record lifecycle. | Documents, files, archive/correction flows, generated receipts/contracts. | Documents can be uploaded, viewed/downloaded by authorised users, and safely retained/removed according to policy. | Slices 1-2; includes relevant privacy/security review of Slice 3 effects where needed. | Required: Independent Privacy/Security Review covering relevant work from Slices 3+4. |
| Slice 5/5 | Release readiness hardening. | Tests/CI, deployment config, environment validation, demo cleanup, basic activity history where included. | Product passes focused workflow checks and is ready for release review, not automatic launch. | Slices 1-4. | No duplicate Gate 6 review; Gate 7/8 is the final independent release-readiness review. |

### Explicit Non-Decisions

- Gate 2 does not authorise implementation.
- Gate 2 does not start D1 or visual design.
- Gate 2 does not change the LeaseDesk product boundary.
- Gate 2 does not authorise source-code changes in `isudally/leasedesk-demo`.

## Gate 8/8 - Release Verification Closeout

Date: 2026-08-22

### Decision

LeaseDesk completed the governed Gate 6/8 implementation programme, Gate 7/8 production-readiness review, and Gate 8/8 release verification. The code is ready for a founder production-release decision, but LeaseDesk is not deployed, released, or commercially live from this decision alone.

### Source State

- Authoritative source repository: `isudally/leasedesk-demo`
- Branch: `main`
- Final merged source SHA: `d2ce8e988f2d8726fde3dc7e3529e84e0d27db78`
- Gate 6/8 implementation slices: 5/5 COMPLETE
- Gate 7/8 production-readiness review: PASS after one bounded correction
- Gate 8/8 release verification: PASS

### Verified In Code

- Production PostgreSQL mode with explicit production configuration.
- Minimal authenticated owner/admin access with session regeneration on login and logout invalidation.
- Demo/production data separation.
- Required production `LEASEDESK_UPLOAD_DIR` with no production fallback to demo upload storage.
- Authenticated document upload/download with file type signature validation for supported document types.
- Safe archive/payment correction model for key operational records.
- Basic audit events for payment correction, document upload/archive, tenant archive, store archive and expense archive.
- `/health` and `/ready` operational endpoints.
- Focused source validation covering core workflows, auth/session, demo/production configuration and production-like Postgres persistence.

### Deployment Prerequisites

- Select hosting/runtime provider and confirm Node/runtime compatibility.
- Provision production PostgreSQL and apply schema initialisation/migration safely.
- Provide production `DATABASE_URL`, `SESSION_SECRET`, admin bootstrap credential/hash and other required secrets through secret management.
- Provide durable persistent document storage for `LEASEDESK_UPLOAD_DIR`.
- Define document and database backup/restore procedures.
- Configure HTTPS/TLS and confirm secure-cookie behaviour behind the selected proxy/runtime.
- Confirm runtime host/port binding works with the selected platform because source release verification did not choose a hosting provider.
- Establish operational access to `/health` and `/ready`.
- Run final smoke test with fictional data in the selected production-like runtime.

### Residual Non-Blocking Dependency Items

- `jspdf` and transitive `dompurify` advisories remain a post-launch maintenance item for client-side receipt/contract generation.
- `drizzle-orm` advisory remains classified non-blocking for this release because current usage relies on static schema/table/column references.
- Express/transitive HTTP-stack advisories remain a normal internet-exposed-app maintenance item.
- Unused or not-reachable dependency chains, including `@google-cloud/storage`, Uppy-related packages and `ws`, should be removed or upgraded before any future use.
- Build/tooling advisories remain outside the reviewed runtime path.

### Explicit Non-Decisions

- This closeout does not deploy LeaseDesk.
- This closeout does not provision production infrastructure, DNS, databases, storage, secrets, backups or paid services.
- This closeout does not announce a commercial release.
- This closeout does not change the LeaseDesk product boundary, priority or portfolio status.

### UI / Visual Harmonisation Decision

LeaseDesk product/code completion is complete. Final UI and visual harmonisation is intentionally deferred to a later portfolio-wide visual alignment programme after the selected Takaven products are complete.

Do not reopen LeaseDesk implementation for cosmetic UI polish before that phase unless a material usability defect appears. The later portfolio-wide visual phase should make LeaseDesk feel related to the Takaven family while preserving its operational, property-oriented and controlled-density personality.

## 2026-08-22 - Deferred Tenant Pass / Residential Extension Hypothesis

Founder identified Tenant Pass as a potentially material future LeaseDesk differentiator. The concept is a controlled live lease, rent status, payment history/receipts, document, notice/action and key-date experience for tenants, not a decorative digital card or generic portal.

Tenant Pass may be reviewed for commercial tenants, residential tenants, or both. Residential applicability is a hypothesis only and is not current approved scope.

LeaseDesk's current completed 8/8 commercial programme remains closed. The current small-commercial-landlord buyer, product boundary and exclusions remain unchanged, including the exclusion for maintenance ticketing.

No Tenant Pass, residential expansion, shared HirePass architecture, or implementation work is authorised before a later explicit product-extension review. Final portfolio UI/visual harmonisation remains deferred as already documented.

## 2026-08-22 - Product Repository Separation

`isudally/leasedesk-demo` remains the authoritative LeaseDesk application source repository on `main` at `d2ce8e988f2d8726fde3dc7e3529e84e0d27db78`.

`takaven/product-portfolio` contains LeaseDesk governance and documentation records only. The files under `products/TKV-002-leasedesk/` are not another LeaseDesk implementation, so there is no duplicate-source ambiguity between the control repo and the application source repo.

No LeaseDesk repository migration, rename, source copy, or new `takaven/leasedesk` repository is currently authorised. Future Takaven-organisation repository normalisation is deferred until there is a material operational reason and an explicit founder/product architecture decision.
