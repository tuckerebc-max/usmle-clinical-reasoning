# `OPT-66-USMLE` source-to-construct crosswalk

**Packet:** `F2-PACKET-66-USMLE-001`  
**Status:** `SOURCE_LOCK_DRAFT`  
**Primary sources:** `F2-66-007`, `F2-66-008`

## Source-grounded construct

**SOURCE:** USMLE Step 2 CK assesses application of medical knowledge, skills, and clinical understanding essential for patient care under supervision, with attention to health promotion and disease prevention. The associated resources include a content outline and physician task / competency documents. AAMC Core EPAs frame integrated activities that may be entrusted with appropriate supervision.

## Assessment-versus-competency boundary

**SOURCE:** Step 2 CK is an examination; Core EPAs are a medical-education framework.  
**INFERENCE:** The textbook competency is supervised clinical knowledge application: represent a patient problem, generate and compare diagnostic or management possibilities, use evidence, communicate professionally, attend to safety and prevention, reassess outcomes, and learn from errors or gaps.  
**NOT CLAIMED:** Independent diagnosis, treatment, prescribing, or unsupervised practice.

## Construct decomposition

1. Orient to patient, context, purpose, and supervision boundary.
2. Build a concise problem representation from relevant findings.
3. Generate and compare hypotheses and information needs.
4. Select or interpret tests proportionally to the decision.
5. Consider management, prevention, prognosis, safety, and alternatives.
6. Communicate reasoning, uncertainty, handoffs, and escalation.
7. Reassess outcomes and identify practice-based learning needs.

## Evidence and task model

**CROSSWALK:** Case representation, evidence / cue ledger, differential or option set, test-selection rationale, management / non-action threshold, safety check, communication / handoff, reassessment, and learning note.  
**EVALUATOR DESIGN:** Evaluate evidence fidelity, differential breadth, priority reasoning, uncertainty, safety / supervision, and reassessment. Do not supply a clinical answer for a real patient.

## Textbook spine

`Orient → Represent → Hypothesize → Test → Manage / prevent → Communicate and escalate → Reassess and learn`

## Failure modes and constraints

- treating a vignette answer as a real-patient order;
- premature closure;
- test ordering without purpose;
- missing safety or supervision boundary;
- false precision or outdated practice;
- privacy leakage;
- agent hallucination treated as medical expertise.

## Next source requests

- harvest the current USMLE physician-task document and technical notes;
- choose educational, de-identified cases only;
- add explicit current-practice verification and professional-review protocol;
- test a refusal / escalation path before any clinical scenario is released.
