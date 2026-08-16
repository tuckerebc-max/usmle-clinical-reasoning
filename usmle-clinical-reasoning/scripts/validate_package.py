#!/usr/bin/env python3
"""Validate this standalone skill package without external dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["SKILL.md", "agents/openai.yaml", "references/competency-object.json", "references/source-crosswalk.md", "references/source-manifest.json", "references/textbook-architecture.md", "references/domain-prompt.md", "references/bounded-packet-001.md", "references/evaluator-spec.json", "references/evaluator-design.md", "references/safety-and-boundaries.md", "references/output-schema.json", "references/skill-contract.md", "tests/fixtures/representative-task.json", "scripts/evaluate_fixture.py"]

def main():
    errors = [f"missing {path}" for path in REQUIRED if not (ROOT / path).is_file()]
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\n---\n" not in skill: errors.append("frontmatter")
    frontmatter = skill.split("\n---\n", 1)[0]
    if not re.search(r"^name:\s+[a-z0-9-]+$", frontmatter, re.MULTILINE): errors.append("name")
    if not re.search(r"^description:\s+.+$", frontmatter, re.MULTILINE): errors.append("description")
    if "TODO" in skill: errors.append("TODO")
    for path in ["references/competency-object.json", "references/source-manifest.json", "references/evaluator-spec.json", "references/output-schema.json", "tests/fixtures/representative-task.json"]:
        if (ROOT / path).is_file():
            try: json.loads((ROOT / path).read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc: errors.append(f"invalid JSON {path}: {exc}")
    result = {"package": ROOT.name, "status": "PASS" if not errors else "FAIL", "errors": errors, "human_review_required": True, "credentialing": False}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
