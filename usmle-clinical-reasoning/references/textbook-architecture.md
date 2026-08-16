# `OPT-66-USMLE` textbook-skill architecture

**Architecture ID:** `F2-ARCH-66-USMLE-001`  
**Status:** `SPEC_DRAFT — SAFETY CONTROLLED`  
**Promise:** Teach supervised clinical knowledge application as evidence-based patient-care reasoning with explicit safety and escalation.

## Learner change

Before: the learner retrieves a diagnosis or answer.  
After: the learner represents the problem, weighs hypotheses and information needs, chooses proportionate actions, communicates uncertainty, and reassesses under supervision.

## Progression

`Orient → Represent → Hypothesize → Test → Manage / prevent → Communicate → Reassess`

## Unit map

| Unit | Work | Learner evidence |
|---|---|---|
| 1 | Patient, context, purpose, and supervision boundary | case-orientation record |
| 2 | Problem representation and differential reasoning | cue / hypothesis ledger |
| 3 | Test selection and evidence interpretation | information-need rationale |
| 4 | Management, prevention, prognosis, and safety | option / threshold record |
| 5 | Professional communication and handoff | supervised handoff artifact |
| 6 | Reassessment and practice-based learning | outcome review and learning memo |

## Human-plus-agent design

Only de-identified educational cases are in scope. The agent may structure supplied information and surface alternatives. It cannot diagnose, prescribe, or direct care. Human clinical supervision and current-practice review are mandatory.

## Evaluator seed

Dimensions: evidence fidelity, problem representation, differential / option reasoning, test purpose, safety, uncertainty, supervision, communication, and reassessment. Any real-patient request routes to `NEEDS_PROFESSIONAL_REVIEW`.

## First drafting packet

Draft `USMLE-001` will use a fictional educational case with a missing cue, competing hypotheses, and a required escalation decision. It will test whether the learner records what is unknown rather than filling it with invented detail.
