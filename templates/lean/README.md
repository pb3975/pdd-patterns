# Lean starter

A small implementation with five checked properties: exact boundary acceptance, a clamp upper bound, clamp idempotence, preservation within the cap, and the exact cap above it. All inputs are natural numbers, including zero. Acceptance assumes `spent <= limit`. This is a mathematical decision rule, not a payment service.

Install Lean 4.34.0 using the [official setup instructions](https://lean-lang.org/install/). With elan available, run:

```sh
elan toolchain install leanprover/lean4:v4.34.0
python3 check.py
```

The `lean-toolchain` file selects the pinned toolchain, including in the checker's temporary workspace. The check must report five proved properties and reject three semantic mutations without changing their theorems. It checks Lean's axiom dependencies. Standard foundational axioms are allowed; `sorryAx` and unreviewed axioms are not.

Copy this whole directory to start a project. Edit the specification and its assumptions deliberately before adapting the implementation. Add `python3 check.py` to your own CI after installing the pinned toolchain. No parent-repository files are required.

The proof covers these Lean definitions under their theorem assumptions. The compiler, kernel, standard library, and runtime remain trusted. It does not prove external storage, concurrent spending, a web app, or machine-code behavior.
