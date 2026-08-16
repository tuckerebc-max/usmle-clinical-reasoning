---
name: usmle-clinical-reasoning
description: "Structure supervised clinical reasoning in educational cases: problem representation, differential hypotheses, information needs, safety, handoff, and reassessment. Not patient care."
---

# USMLE clinical knowledge application and physician-task reasoning

## Purpose

Use this skill to operationalize competency F2-COMP-66-USMLE-001 as a bounded,
source-grounded reasoning, evidence, feedback, and improvement workflow.
The assessment, credential, degree, or program exemplar informing the skill
is evidence about the competency, not the competency itself.

## Use

Use it for educational clinical-reasoning scaffold when the user supplies a domain task, case, passage,
study, policy record, model, or design record. Do not use it as a
independent clinician, diagnostic service, prescribing system, or substitute for current clinical guidance.

## Workflow

1. State task, purpose, audience, constraints, supplied materials, intended use, accessibility, and decision rights.
2. Read supplied materials first; separate source claims, observations, inferences, project judgments, and missing evidence.
3. Build the domain-specific evidence record and connect claims, reasons, methods, facts, or requirements to locators.
4. Test alternatives, uncertainty, limitations, and the most consequential failure mode for this domain.
5. Produce a qualified learner or reviewer artifact and preserve unresolved questions.
6. Stop and route substantive judgment to the accountable human reviewer named in the safety reference.

## Competency spine

- case orientation and problem representation
- hypothesis and differential reasoning
- test and information selection
- management, prevention, and safety
- communication, reassessment, and learning

## Evidence requirements

- case and cue ledger
- hypothesis or option record
- information-need rationale
- supervised handoff and safety check
- reassessment and learning record

## Output contract

Return a structured record containing:

- task_contract and orientation
- source_ids, locators, provenance, and rights status
- competency evidence and evaluator dimensions
- alternatives, uncertainty, limitations, and unresolved_items
- learner_task or reviewer_feedback
- review_status and explicit boundary statement

Use status values such as READY_FOR_HUMAN_REVIEW, NEEDS_INPUT,
BLOCKED_PENDING_REVIEW, and FORMATIVE_ONLY. Never issue a credential,
licensure decision, professional sign-off, or high-impact decision.

## Guardrails

- Use educational cases only; no real patient data, diagnosis, prescription, or independent clinical action.
- Do not invent sources, citations, facts, results, authorities, clinical findings, validation, or stakeholder positions.
- Keep SOURCE, CROSSWALK, INFERENCE, and PROJECT_EVALUATOR layers distinct.
- Use original, synthetic, public-domain, or permission-cleared challenge materials only.
- Preserve learner authorship; scaffold and audit rather than ghostwrite assessed work.

- Stop if the supplied record is missing or unverifiable.
- Stop if the task crosses the declared professional or consequential boundary.
- Stop if source, rights, privacy, or jurisdiction conditions cannot be established.
- Stop if the output would be presented as a credential, license, sign-off, or official decision.

## Handoffs

Clinician or medical educator owns clinical interpretation, safety, privacy, and consequential decisions.

Read references/source-crosswalk.md, references/competency-object.json,
references/evaluator-spec.json, references/textbook-architecture.md,
references/bounded-packet-001.md, and references/safety-and-boundaries.md
before making a domain-specific claim.
