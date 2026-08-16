#!/usr/bin/env python3
"""Run the package structural, non-credentialing fixture evaluator."""
import argparse
import json
from pathlib import Path

REQUIRED = ["fixture_id", "track_id", "competency_id", "source_ids", "construct_boundary", "task_contract", "stimulus", "learner_deliverables", "evidence_envelope", "machine_checks", "human_review", "stop_conditions", "evaluator", "qa"]

def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=root / "tests" / "fixtures" / "representative-task.json")
    args = parser.parse_args()
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    errors = [field for field in REQUIRED if field not in fixture]
    if not fixture.get("source_ids"): errors.append("source_ids")
    if not fixture.get("human_review"): errors.append("human_review")
    if not fixture.get("stop_conditions"): errors.append("stop_conditions")
    if fixture.get("evaluator", {}).get("no_credentialing") is not True: errors.append("evaluator.no_credentialing")
    qa = fixture.get("qa", {})
    if qa.get("original_fixture") is not True: errors.append("qa.original_fixture")
    if qa.get("secure_content_reproduced") is not False: errors.append("qa.secure_content_reproduced")
    if qa.get("confidential_data") is not False: errors.append("qa.confidential_data")
    result = {"fixture_id": fixture.get("fixture_id"), "machine_status": "PASS" if not errors else "FAIL", "decision": "NEEDS_HUMAN_REVIEW" if not errors else "BLOCKED_STRUCTURAL_ERROR", "human_dry_run": "PENDING", "credentialing": False, "errors": errors}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
