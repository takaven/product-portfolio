# Takaven Design Governance

Takaven products should clearly belong to the same company without becoming reskinned copies of each other.

This is governance, not a finished UI kit.

## Version

Current governed design-system version: `takaven-design-system-v1`

Product records in `PORTFOLIO.yaml` must reference this version in their `design_governance` block. Changing this version is a governance change, not an implementation convenience.

## Colour Tokens

Written HEX values are authoritative. Do not sample colours from images.

| Token | HEX |
| ----- | --- |
| Electric Signal Green | `#01FF22` |
| Soft Graphite | `#42494D` |
| Titanium Grey | `#68707D` |
| Deep Support Charcoal | `#20242B` |
| Soft Mist | `#F4F6F8` |
| White | `#FFFFFF` |

## Shared Rules

- Use accessible contrast for text, controls and data states.
- Keep typography calm and legible; avoid decorative type for operational tools.
- Use consistent spacing, state handling, form behaviour and responsive layout.
- Use high-quality icons consistently; avoid improvised icon styles.
- Tables, forms, cards, navigation, modals and drawers should share interaction patterns across products.
- Products may have distinct visual personalities within these constraints.

## Product Personalities

- HirePass: pass-centric, identity/status-driven, sharper, more progressive.
- LeaseDesk: operational, property-oriented, controlled information density.
- PayrollFlowEngine: precise, analytical, audit/control-oriented.

TeamFrame may have its own design direction in its separate repository. This file must not be treated as TeamFrame governance.

## Portfolio-Wide Visual Harmonisation

Final visual harmonisation is intentionally deferred until the selected Takaven products are complete. Do not reopen a completed product, including LeaseDesk, merely for cosmetic visual refinement before that portfolio-wide phase unless a material usability defect appears.

The later visual phase should align typography, spacing, component styling, forms, tables, navigation, status patterns, responsive behaviour, Takaven brand use, iconography and visual polish across the portfolio while preserving each product's personality.

## Frontend Gates

No full frontend rollout before visual foundation and critical screens are approved.

- D1 - UX principles: navigation, density, roles and workflows.
- D2 - Critical screens: approximately three highest-value screens.
- D3 - Component primitives: tables, forms, cards, navigation, states, modals and drawers.
- D4 - Full frontend implementation.

D2 requires approved D1 evidence. D3 requires approved D1 and D2 evidence. D4 requires approved D1, D2 and D3 evidence.

For HirePass, likely critical surfaces are HR / Pass management view, Candidate Pass and Manager Pass. Do not design them until the relevant gate is opened.

## Product Design Stages

`PORTFOLIO.yaml` tracks product design stage using:

- `NOT_STARTED`
- `D1_APPROVED`
- `D2_APPROVED`
- `D3_APPROVED`
- `D4_AUTHORISED`
- `NOT_APPLICABLE`

`NOT_APPLICABLE` is reserved for retained component records such as TeamFrame-destined modules. Independent product records must not use it.
