#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for path in ("scripts/validate_package.py", "scripts/evaluate_fixture.py"):
    result = subprocess.run([sys.executable, str(ROOT / path)], cwd=ROOT)
    if result.returncode: raise SystemExit(result.returncode)
print("PASS standalone package tests")
