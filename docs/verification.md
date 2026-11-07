# Verification receipt

Executed on Linux x86_64 on November 7, 2026. These are bounded evidence claims for the listed artifacts, not a certification of the whole repository.

## Exact tools

- Lean 4.34.0, official Linux release archive, SHA-256 `caaa98356098c85dc0fcbbd28e1ec66f39eb6551829972b752ff20e1286b646b`.
- Z3 4.15.4 from the official `z3-solver==4.15.4.0` Python wheel. This host lacks Python ensurepip, so local verification used the wheel's extracted `z3` executable. CI installs the same pinned package normally.
- Bend 2.0.40, source commit `ca77ef289bf6e199a0cb95adb9804c0f58d991f0`, source archive SHA-256 `fe358d46fdc40f3f89368e3fdd80280492afcde8d1b2403995b4322cbef0feb6`.
- Bun 1.4.2. Bend was invoked with `--no-env-file --no-config` and `--verdict`.

## Executed command

With the above tools on PATH and `BEND_SOURCE` pointing to the pinned extracted Bend source:

```sh
python3 scripts/verify.py
```

Result: exit 0. The runner copied every whole starter into a fresh temporary directory outside the repository and executed its own `check.py` there.

- Lean proved exact boundary acceptance, clamp boundedness, clamp idempotence, preservation within the cap, and the exact cap above it. It rejected three syntactically valid implementation changes: strict boundary, return input, and constant zero. The theorem statements and proofs stayed unchanged.
- Lean reported only `propext`, `Classical.choice`, and `Quot.sound` where used. The cap theorem needed no axioms. No `sorry`, `admit`, `sorryAx`, unreviewed extra axiom, or unsafe definition was admitted in the checked source.
- Z3 returned `unsat` for the correct boundary and complete clamp models. Strict boundary, return input, and constant-zero mutations returned `sat`. The boundary witness was `spent=0, amount=0, limit=0`; the checker independently verified its legal equality conditions. These examples explicitly permit zero amount.
- Bend's actual `--verdict` command checked both Boolean policy laws. Changing the disabled branch to return `True{}` caused the unchanged law and proof to be rejected. No fallback to the default checker was accepted.

Each starter is runnable without parent-repository files after its documented dependencies are installed. This checks independence of repository location. It does not retest every supported operating system or every future dependency release.

## Dogfooding the agent skill

The authoring pass used [pdd-change](../skills/pdd-change/SKILL.md) on the inclusive-boundary example: state permitted and rejected outcomes, keep the claim fixed, implement the rule, run the real checkers, then mutate only the implementation and observe rejection. The same workflow exposed a specification problem in the clamp example during review: constant zero satisfied the original bound and idempotence claims. The claim was strengthened explicitly before repeating the actual checks. The skill now directs agents to use proportionate tests or review when a formal proof is unsuitable.

The official Skill Creator `quick_validate.py skills/pdd-change` returned `Skill is valid!`. This validates skill structure. It does not formally prove the skill's prose or show that every future agent follows it.

An independent Astra review used the skill in a fresh temporary workspace with Lean 4.35.0. It implemented a cap helper, proved bound, idempotence, preservation, and saturation, and observed a return-input mutation fail against unchanged theorems. The restored helper passed. The review also demonstrated the original specification gap by replacing the Z3 clamp with zero and observing `unsat`. That prompted the explicit contract strengthening and constant-zero negative controls now checked in this collection. This is one behavioral trial, not a guarantee about future agents. The collection's reproducible suite uses the pinned Lean 4.34.0 required by Bend.

## Trust and exclusions

Lean's kernel, standard library, foundational axioms, compiler, and runtime are trusted. The Z3 encoding and solver are trusted. Bend's `--verdict` checks translated terms with its Lean-formalized kernel; parsing, translation into that kernel, backend compilation, and runtime behavior remain outside that formalization. No result here proves a production identity service, database, network, JavaScript application, machine overflow behavior, concurrency protocol, or a complete product. Proof maintenance and ordinary integration tests remain necessary.
