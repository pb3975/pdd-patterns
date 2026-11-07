---
name: pdd-change
description: Add or change a specified behavior with a machine-checked proof and a meaningful negative control. Use for proof-driven development work; do not describe tests or unchecked claims as formal proofs.
---

# Make a specified change

Read the owning requirements and the existing implementation. Identify one behavior whose failure matters and a proof tool that can express it. Keep the work within the user's requested scope.

Before coding, write the claim in plain language and in the tool's specification. Include useful behavior as well as rejection of invalid behavior. Name preconditions, arithmetic rules, external dependencies, and what the proof leaves unverified. Preserve the approved claim when repairing the implementation. If the claim must change, make that change explicit for review.

Implement the behavior and check the proof with the actual pinned tool. Record the command, version, exit status, proved properties, assumptions, and remaining test coverage. A proof about a separate model does not prove an application implementation.

Make a temporary, syntactically valid semantic mutation that violates the claim while keeping the specification and proof unchanged. Confirm that verification rejects it for the expected reason. Restore the implementation and run the checks again. A missing compiler, parser error, timeout, or absent dependency is not a successful negative control.

Keep proofs in CI. For Lean, reject `sorry` or unreviewed extra axioms. For solver models, require a decisive result and fail on `unknown`. For Bend, state whether the default checker or `--verdict` checked the law and disclose the toolchain boundary. Keep empirical tests for behavior outside the proof.

If a proof is not practical, report the exact gap and label the example as a draft or as tested only. Do not add a proof badge to a skill, a template's scaffolding, or a whole application because one example passes.

## Choose a proportionate method

Use formal proofs when a stable, consequential rule can be expressed precisely and the expected benefit justifies proof and maintenance effort. Exploratory requirements, subjective usability, low-impact reversible changes, and integration behavior often need ordinary tests, human review, or monitoring instead. Say which method fits this change. Do not force a formal proof for every change.

A correct proof of an incomplete specification can still give false confidence. Review missing outcomes, assumptions, and interfaces. State the effort to maintain the proof when requirements or toolchains change. Keep tests and monitoring for the outside world.
