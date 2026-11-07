# PDD patterns

**Private review collection. Public release requires Will's approval.**

Small proof-driven development patterns, runnable examples, an agent skill, and standalone starter templates. Verification applies to named properties, under stated assumptions. It is not a certification of this repository or an application.

## Start with a pattern

- [Inclusive boundaries](patterns/inclusive-boundary.md): accept permitted equality cases as well as reject overspending. Lean and Z3.
- [Complete clamp](patterns/bounded-idempotent-clamp.md): prove the bound, idempotence, preservation within the cap, and saturation above it. Lean and Z3.
- [Boolean policy branches](patterns/boolean-policy.md): preserve a disabled gate and an enabled authorization input. Experimental Bend starter.

## Choose a starter

Copy a whole starter directory into a new project, follow its setup, and run `python3 check.py`.

- [Lean](templates/lean/): proofs about the actual pure Lean definitions.
- [Z3](templates/z3/): proofs about separate mathematical integer models.
- [Bend](templates/bend/): application, laws, and proofs checked with `--verdict`.

The root check copies each starter to a temporary directory outside this repository and runs it there. Each checker verifies the correct artifact and rejects a semantic mutation while preserving the specification. Missing tools, syntax errors, timeouts, and undecided results are failures, not successful negative controls.

## Run all checks

Use Python 3.11 or later. Install Z3 4.15.4 from `z3-solver==4.15.4.0` using the Z3 starter instructions. Install Lean 4.34.0 with the [official Lean setup](https://lean-lang.org/install/) and select that toolchain on PATH. Install Bun 1.4.2 using the [official Bun instructions](https://bun.com/docs/installation).

The Bend kernel requires Lean 4.34.0. Obtain its exact checked source without executing a remote installer:

```sh
curl -fL https://codeload.github.com/bendlang/bend/tar.gz/ca77ef289bf6e199a0cb95adb9804c0f58d991f0 -o /tmp/pdd-bend.tar.gz
printf '%s  %s\n' fe358d46fdc40f3f89368e3fdd80280492afcde8d1b2403995b4322cbef0feb6 /tmp/pdd-bend.tar.gz | sha256sum -c -
tar -xzf /tmp/pdd-bend.tar.gz -C /tmp
export BEND_SOURCE=/tmp/bend-ca77ef289bf6e199a0cb95adb9804c0f58d991f0
python3 scripts/verify.py
```

The pinned Lean Linux release archive is `lean-4.34.0-linux.tar.zst`, SHA-256 `caaa98356098c85dc0fcbbd28e1ec66f39eb6551829972b752ff20e1286b646b`. CI installs these same exact versions and source. Setup needs network access; verification runs locally without credentials or paid services.

## Use the agent skill

Read [skills/pdd-change/SKILL.md](skills/pdd-change/SKILL.md), or copy its directory to your agent's skill location. The skill guides a proportionate choice of proof, tests, and review, preserves the approved claim, and requires real checker receipts with meaningful negative controls. It does not grant permission to publish, deploy, or change unrelated systems.

See [the dogfood receipt](docs/verification.md). Skill guidance itself is not formally proved.

## When to use this approach

Use proofs for a stable, consequential rule that you can express precisely, when the reduction in risk justifies the initial and ongoing cost. Boundary arithmetic, protocol invariants, and security decisions can be useful candidates.

Use ordinary tests, human review, or monitoring when requirements are exploratory or changing quickly, correctness depends on subjective usability, the change is low impact and easy to reverse, or the behavior is mainly about outside systems. Formal reasoning can still help clarify such work, but proving everything is not the goal.

## Limits and maintenance

A correct proof of an incomplete specification can produce false confidence. Review the intended permitted outcomes, preconditions, and external assumptions. A separate model can drift from the application. A source-level theorem does not establish that every compiler backend, runtime, library, or deployment behaves correctly.

Lean's kernel, standard library, and reported foundational axioms are trusted. Z3's encoding and solver are trusted. Bend's parser, kernel translation, compiler, and runtime have explicit limits documented in its starter. These examples do not model persistent state, concurrent transactions, external identity, machine overflow, or a complete service.

Proofs require maintenance when requirements, code, dependencies, or checker versions change. Keep integration tests, usability review, monitoring, and incident response for behavior outside the proof. The checked properties do not establish that the product is useful.

[Requirements](PRD.md) · [Decisions](docs/decisions.md) · [Verification evidence](docs/verification.md)

Public release is still held. The proposed reuse license is MIT. Review [the release proposal](docs/release.md) before approving publication.
