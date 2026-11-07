#!/usr/bin/env python3
"""Check the pure Bend policy and a same-law semantic mutation."""
import os
import pathlib
import shutil
import subprocess
import tempfile

source = pathlib.Path(__file__).resolve().parent
bend = pathlib.Path(os.environ["BEND_SOURCE"]).resolve() / "bend2" / "main.ts"
assert bend.is_file(), "BEND_SOURCE must point to the pinned Bend checkout"
command = ["bun", "--no-env-file", "--no-config", str(bend)]
version = subprocess.run(command + ["version"], text=True, capture_output=True, check=True).stdout.strip()
assert version == "bend 2.0.40", version
assert subprocess.run(["bun", "--version"], text=True, capture_output=True, check=True).stdout.strip() == "1.4.2"
with tempfile.TemporaryDirectory(prefix="pdd-bend-check-") as temporary:
    directory = pathlib.Path(temporary)
    for artifact in source.glob("*.bend"):
        shutil.copyfile(artifact, directory / artifact.name)
    result = subprocess.run(command + ["PROOF.bend", "--verdict"], cwd=directory, text=True, capture_output=True, timeout=120)
    assert result.returncode == 0 and "ALL PROOFS CHECK" in result.stdout, result.stdout + result.stderr
    print("PASS Bend Boolean policy: both laws checked with --verdict")
    app = directory / "App.bend"
    original = app.read_text()
    mutant = original.replace("\n      False{}\n", "\n      True{}\n")
    assert mutant != original
    app.write_text(mutant)
    result = subprocess.run(command + ["PROOF.bend", "--verdict"], cwd=directory, text=True, capture_output=True, timeout=120)
    output = result.stdout + result.stderr
    assert result.returncode != 0, "Bend accepted the disabled-allows mutation"
    assert "infrastructure" not in output and "parse error" not in output.lower(), output
    assert any(text in output.lower() for text in ("mismatch", "type error", "expected", "proofs fail")), output
    print("PASS Bend semantic policy mutation: unchanged law rejected")
