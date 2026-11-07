#!/usr/bin/env python3
import pathlib
import re
import shutil
import subprocess
import tempfile


def run(command, cwd, expected=0):
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=90)
    output = result.stdout + result.stderr
    if result.returncode != expected:
        raise AssertionError(f"{command[0]} exited {result.returncode}, expected {expected}:\n{output}")
    return output

def lean_check(directory, lean):
    source = (directory / "Patterns.lean").read_text()
    assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b", source), "Unreviewed proof escape"
    output = run([lean, "Patterns.lean"], directory)
    assert "sorryAx" not in output, output
    allowed_axioms = {"propext", "Classical.choice", "Quot.sound"}
    reports = re.findall(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", output)
    assert {name for name, _ in reports} == {"allow_exactly", "clamp_bounded", "clamp_idempotent", "clamp_preserves", "clamp_caps"}, output
    for _, report in reports:
        assert (set(report.split(", ")) if report else set()) <= allowed_axioms, output
    print("PASS Lean definitions: exact acceptance, clamp bound/idempotence, preserve-inside and cap-outside")
    for name, old, new in [
        ("boundary", "decide (spent + amount ≤ limit)", "decide (spent + amount < limit)"),
        ("clamp", "min limit value", "value"),
        ("constant-zero clamp", "min limit value", "0"),
    ]:
        mutant = source.replace(old, new)
        assert mutant != source
        (directory / "Broken.lean").write_text(mutant)
        result = subprocess.run([lean, "Broken.lean"], cwd=directory, text=True, capture_output=True, timeout=90)
        output = result.stdout + result.stderr
        assert result.returncode != 0, f"Lean accepted {name} mutation"
        assert "unexpected token" not in output and "unknown module" not in output, output
        assert "error:" in output and any(text in output for text in ("omega could not prove", "Type mismatch", "type mismatch", "unsolved goals")), output
        print(f"PASS Lean semantic {name} mutation: unchanged theorem rejected")


if __name__ == "__main__":
    binary = shutil.which("lean")
    if binary is None:
        raise SystemExit("Missing lean; follow README.md. This is not a successful proof check.")
    source = pathlib.Path(__file__).resolve().parent
    version = run([binary, "--version"], source)
    assert re.search(r"(?<![0-9.])4[.]34[.]0(?![0-9.])", version), version
    with tempfile.TemporaryDirectory(prefix="pdd-lean-check-") as temporary:
        directory = pathlib.Path(temporary)
        shutil.copyfile(source / "lean-toolchain", directory / "lean-toolchain")
        for artifact in source.glob("*.lean"):
            shutil.copyfile(artifact, directory / artifact.name)
        lean_check(directory, binary)
