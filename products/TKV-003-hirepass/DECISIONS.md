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
