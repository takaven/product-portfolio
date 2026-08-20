# Takaven Design Governance

Takaven products should clearly belong to the same company without becoming reskinned copies of each other.

This is governance, not a finished UI kit.

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

- TeamFrame: calm, structured, spacious.
- HirePass: pass-centric, identity/status-driven, sharper, more progressive.
- LeaseDesk: operational, property-oriented, controlled information density.
- PayrollFlowEngine: precise, analytical, audit/control-oriented.

## Frontend Gates

No full frontend rollout before visual foundation and critical screens are approved.

- D1 - UX principles: navigation, density, roles and workflows.
- D2 - Critical screens: approximately three highest-value screens.
- D3 - Component primitives: tables, forms, cards, navigation, states, modals and drawers.
- D4 - Full frontend implementation.

For HirePass, likely critical surfaces are HR / Pass management view, Candidate Pass and Manager Pass. Do not design them until the relevant gate is opened.
