# Z3 starter

Two separate mathematical models: inclusive boundary acceptance, and complete clamping. The clamp must stay bounded, be idempotent, preserve values within the cap, and return the cap above it. Variables are nonnegative, unbounded integers, including zero. The boundary model assumes `spent <= limit`.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python check.py
```

On Debian/Ubuntu, install your distribution's `python3-venv` package if the venv command reports that ensurepip is unavailable. Z3 must be exactly 4.15.4, supplied by `z3-solver==4.15.4.0`.

The correct models must return `unsat`: no violating input exists under the encoded assumptions. The temporary strict-boundary, unclamped, and constant-zero mutations must return `sat`. The boundary witness is read and checked to confirm it is a legal equality input. `unknown`, a missing tool, or a parse error fails verification.

Copy this whole directory to start a project. Adapt the contract deliberately and preserve it when repairing the implementation. Add `python check.py` to your CI after installing requirements. No parent-repository files are required.

These results prove properties of the SMT-LIB models. They do not prove an application's source code, database state, concurrency behavior, machine overflow behavior, or user requirements. The encoding and solver are trusted.
