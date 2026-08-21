# Phase 2 Automation Candidates

Phase 2 implemented only deterministic read-only GitHub checks. Anything that mutates issues, applies labels, assigns agents or closes work automatically remains deferred.

## Candidate Controls

| Candidate | Why Consider It | Do Not Start Until |
| --------- | --------------- | ------------------ |
| GitHub issue-to-PR agent pilot | Tests whether bounded issue execution can safely reduce founder coordination load. | Phase 3 is explicitly authorised and a low-risk repository-only issue is selected. |
| Registry conflict detector | Could compare generated docs, dashboard and product folders for deeper contradictions. | Current validation checks prove stable and false-positive rate is low. |
| Source locator verification assistant | Could help keep source metadata current without modifying product repositories. | Source-resolution workflow has passed at least once manually. |
| Design gate checklist automation | Could validate D1-D4 prerequisite references before design PRs. | First product design gate has been run manually and the evidence pattern is clear. |
| PR review summariser | Could produce standardised governance review summaries. | PR template and review classifications have been accepted by independent review. |
| Automatic issue close-on-merge | Could reduce manual issue housekeeping. | PR-to-issue linkage is proven reliable and safe failure behaviour is defined. |
| Minimal label taxonomy | Could improve filtering and duplicate detection. | A small accepted label set exists and false-positive risk is low. |
| Stale issue detection | Could surface abandoned governance work. | A rule exists that distinguishes abandoned work from deliberately long product phases. |

## Deferred By Design

Do not automate:

- product discovery reopening;
- commercial ranking;
- product activation or archive decisions;
- design approval;
- production deployment;
- external service setup with spend or data exposure.
