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

Do not rebuild from zero. Use the sanitised takaven/hirepass baseline as the authoritative source, consolidate controlled modules later, and remove full ATS/broad HR scope. Repository is public temporarily by founder instruction for live review and should be made private after execution. Known baseline execution debt: manager-form typecheck failure and no automated test script.

## Product Principles

### Pass concept

- Status: `REQUIRED`
- Description: HirePass must preserve distinct controlled external passes such as Candidate Pass and Manager Pass.
- Governance rule: Do not dilute the Pass concept into generic portal terminology or freeze detailed terminology without the relevant design/product gate.
- Provisional terms: Issue Pass, Open Pass, Revoke Pass, Pass Status, Pass Activity

