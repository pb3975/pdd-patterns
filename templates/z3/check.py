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

def z3_check(directory, z3):
    for name in ("boundary", "clamp"):
        output = run([z3, name + ".smt2"], directory)
        assert output.strip() == "unsat", (name, output)
        print(f"PASS Z3 {name}: unsat")
    boundary = (directory / "boundary.smt2").read_text()
    mutant = boundary.replace("(<= (+ spent amount) limit)", "(< (+ spent amount) limit)")
    assert mutant != boundary
    mutant += "\n(get-value (spent amount limit))\n"
    (directory / "broken.smt2").write_text(mutant)
    output = run([z3, "broken.smt2"], directory)
    assert output.splitlines()[0] == "sat", output
    values = dict((key, int(value)) for key, value in re.findall(r"\((spent|amount|limit)\s+([0-9]+)\)", output))
    assert set(values) == {"spent", "amount", "limit"}, output
    assert 0 <= values["spent"] <= values["limit"] and values["amount"] >= 0
    assert values["spent"] + values["amount"] == values["limit"]
    print("PASS Z3 semantic boundary mutation: sat, validated equality witness", values)
    clamp = (directory / "clamp.smt2").read_text()
    for name, replacement in [("unclamped", "n"), ("constant-zero", "0")]:
        mutant = clamp.replace("(ite (<= n cap) n cap)", replacement)
        assert mutant != clamp
        (directory / "broken-clamp.smt2").write_text(mutant)
        assert run([z3, "broken-clamp.smt2"], directory).strip() == "sat"
        print(f"PASS Z3 semantic {name} clamp mutation: sat")


if __name__ == "__main__":
    binary = shutil.which("z3")
    if binary is None:
        raise SystemExit("Missing z3; follow README.md. This is not a successful proof check.")
    source = pathlib.Path(__file__).resolve().parent
    version = run([binary, "-version"], source)
    assert re.search(r"(?<![0-9.])4[.]15[.]4(?![0-9.])", version), version
    with tempfile.TemporaryDirectory(prefix="pdd-z3-check-") as temporary:
        directory = pathlib.Path(temporary)
        for artifact in source.glob("*.smt2"):
            shutil.copyfile(artifact, directory / artifact.name)
        z3_check(directory, binary)
