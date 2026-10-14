# Decisions

Append only material decisions for TeamFrame.

## 2026-09-06 - Active Commercial Product Record

- TeamFrame is recorded as `TKV-001`, its original Takaven product identity.
- TeamFrame is an active Takaven commercial product, not a discovery item.
- `takaven/teamframe` on `main` at `45e63bfd85c05d65b4fd935dd4ba61081b6799af` is the authoritative TeamFrame application source.
- `takaven/teamframe-site` on `main` at `34192eb663bdef5186032234e39f7d8d76969414` is the authoritative TeamFrame commercial website source.
- TeamFrame application source, commercial-site source and final branding are locked for commercial launch preparation.
- Customer deployment remains controlled per customer and requires founder/customer-delivery approval.
- The TeamFrame walkthrough destination remains a launch configuration item; no URL is invented in the portfolio record.
- Any integration with LeaseDesk, HirePass or PayrollFlowEngine remains a separate future decision.

## 2026-09-06 - Commercial Model Preserved

- TeamFrame software remains recorded as `US$1,950` one-off.
- TeamFrame + Setup remains recorded as from `US$3,450` one-off.
- Customer infrastructure is customer-paid/customer-controlled where applicable.
- Post-handover support and future change requests are optional and quoted separately.
- No monthly software subscription, mandatory maintenance or annual software licence is approved.
- TeamFrame product scope, application source and commercial-site source are unchanged by this commercial packaging source lock.

## 2026-09-06 - Independent Launch Review Response

- The independent adversarial launch review found TeamFrame is product-level GO, with no product launch blocker.
- Accepted pre-outreach corrections are operational/commercial readiness items only; product development remains closed.
- The independent concern that TeamFrame may be underpriced is classified as monitor after first sales. Approved pricing remains unchanged.
- External proof and testimonials are classified as an early commercial objective, not as a product launch blocker.
- TeamFrame remains focused on ongoing people operations after an organisation needs structured employee and HR administration. HirePass remains the pre-employment hiring handoff product; any integration remains a future separate decision.

## 2026-10-13 - Canonical Marketing Website Source Reconciled (Issue #49)

- Founder instructed review of the predecessor commercial website and consolidation into `takaven/takaven-web`, keeping `takaven/teamframe` as the separate protected HR product application source.
- `takaven/takaven-web`, `main` at `f42496f1f6ff243bca729c3b434b03bd0b8b907f` is the verified website source baseline for `teamframe/`; its Vercel-generated URL was reported Ready/checked, but the `www.takaven.com` domain verification and DNS cutover were pending at the dated checkpoint. Online form endpoint remains inactive; `admin@takaven.com` is the direct contact fallback.
- `takaven/teamframe-site` is a predecessor only. Preserve until documentation, current deployments and Git references are reconciled, then obtain separate explicit deletion approval. Historical September source locks are provenance, not current source precedence.
- Existing one-off commercial model is unchanged; previously approved price figures remain internal references and are not republished on the current website by this source correction. Current product/optional-support scope remains governed by the later TeamFrame application commercial scope and decisions.
- The TeamFrame application at `app.takaven.com` and its pending real-customer-data gates are unaffected.

## 2026-10-14 - Live Website and Audit-Ready Source State (Issue #51)

- `takaven/takaven-web` is the live canonical TeamFrame marketing source. `www.takaven.com` is Vercel-verified, the root redirects to `/teamframe/`, and the published privacy/HR Setup Check journeys are active.
- The predecessor `takaven/teamframe-site` repository was deleted after source reconciliation; historical September references remain provenance only.
- TeamFrame's six-finding bounded correction workstream closed through PR #30 and PR #31. Final behaviour-changing application baseline is `3865ec2ea9ee37bfdefbb95d45214e48038ce784`; current application `main` at this reconciliation is `e53d9ecee1fd53ccbcfa0e24ea8a6871c2a761cc` after documentation-only follow-up.
- The current marketing `main` source checkpoint is `2835dafe1abe97578dd7b2733cba47d1c061ad83`; documentation-only website commits do not change the accepted behavioural baseline or product scope.
- The website form endpoint remains unset with `admin@takaven.com` as fallback. Real-customer application data remains separately gated. No price, product-boundary or customer-data authorisation changed.
