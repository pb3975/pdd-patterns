#!/usr/bin/env python3
"""Run each starter after copying it outside the repository."""
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
for tool in ("lean", "z3", "bend"):
    with tempfile.TemporaryDirectory(prefix=f"pdd-{tool}-standalone-") as temporary:
        target = pathlib.Path(temporary) / "starter"
        shutil.copytree(ROOT / "templates" / tool, target)
        subprocess.run([sys.executable, "check.py"], cwd=target, check=True, timeout=120)
        print(f"PASS {tool} standalone starter copied outside repository", flush=True)
