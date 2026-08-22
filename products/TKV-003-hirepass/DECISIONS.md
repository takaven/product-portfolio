# Decisions

Append only material decisions for HirePass.

## 2026-08-20 - Initial Portfolio Record

- Status: `SHORTLIST_BUILD`
- Priority: `P1`
- Current execution gate: Phase 1 - sanitisation and foundation extraction.
- Evidence confidence: `VERIFIED`

## 2026-08-22 - Sanitised Source Foundation Preserved

- Founder authorised creation of `takaven/hirepass` from the sanitised Talent-Flow working tree.
- Repository visibility is `PUBLIC` temporarily by founder instruction for live review; it should become private after execution.
- `takaven/hirepass` on `main` at `50b7704b732e3309ad5ce3a361b69eb83b2a5777` is the current authoritative HirePass implementation source.
- The original local/Replit-export `Talent-Flow` source remains historical/reference only. Its contaminated Git history must not be reused for Builder access or future repository history.
- Sanitisation removed historical company/candidate material and preserved functional Candidate Pass, Manager Pass, hiring request, candidate, interview, evaluation, offer, onboarding, message, document, schema, route and storage code.
- Known baseline execution debt: `npm run check` fails in `client/src/pages/manager-form.tsx`, and no automated `test` script exists.
- These baseline defects are not sanitisation defects, but they must be addressed in the first bounded foundation-hardening gate before substantial HirePass feature work.

## 2026-08-22 - Foundation Hardening Closed

- `takaven/hirepass` PR #2 merged foundation hardening at `09ded87dbba0cff8c53a3a764608f96e03f9141b`.
- The baseline manager-form typecheck defect was corrected.
- A minimal automated regression baseline now protects current Candidate Pass and Manager Pass token access behaviour.
- Foundation validation now runs typecheck, tests and build in GitHub Actions.
- No Candidate Pass redesign, Manager Pass redesign, D1 screen design or component-source import was performed.

## 2026-08-22 - D1 Product / UX Definition Proposed

- HirePass should be governed by a Pass-first product model.
- Candidate Pass and Manager Pass are the primary external interaction surfaces.
- HR uses an internal control workspace to issue, monitor, nudge, expire and revoke Passes.
- Pass/action state must remain distinct from hiring-stage status.
- External Passes should be next-action-first, controlled-access, mobile-first and progressively disclosed.
- This proposal does not approve D2 screens, D3 components, D4 implementation, frontend redesign, deployment or product-boundary expansion.

## 2026-08-22 - D1 Approved / D2 Critical Experiences Proposed

- Founder approval prompt approved the D1 principles from Issue #31 / PR #32.
- Canonical design stage moved to `D1_APPROVED`.
- D2 proposes three critical experiences: Candidate Pass, Manager Pass and HR Pass Control / Hiring Action Workspace.
- D2 records source reuse direction only; no HirePass source code or frontend was modified.
- D2 remains pending orchestrator/founder approval and does not authorise D3 components or Pass implementation.

## 2026-08-22 - D2 Approved / D3 Pass Component System Proposed

- Founder approval prompt approved the D2 critical experiences from Issue #33 / PR #34.
- Canonical design stage moved to `D2_APPROVED`.
- D3 proposes the reusable Pass interaction/component primitive system required for Candidate Pass, Manager Pass and HR Pass Control.
- D3 records primitive behaviour and source reuse direction only; no HirePass source code or frontend was modified.
- D3 remains pending orchestrator/founder approval and does not authorise D4 implementation.
