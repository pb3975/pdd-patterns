# Bound a value without changing it twice

Use this for an explicit upper-bound operation on nonnegative values. Define `clamp(cap, value) = min(cap, value)`.

Properties:

- The result is at most `cap`.
- Applying the same clamp twice gives the same result as applying it once.
- Values at or below the cap stay unchanged.
- Values above the cap return the cap.

Negative controls: replace only the implementation with the input value, then with constant zero. The input-value mutation violates the bound. Constant zero satisfies both the bound and idempotence but violates the permitted result for positive values. Preserve the complete specification in both checks.

This is why bound and idempotence alone do not establish correct clamping. Useful permitted outcomes belong in the contract too.

- [Lean definition and theorems](../templates/lean/Patterns.lean).
- [Z3 model](../templates/z3/clamp.smt2).

Run each starter's `python3 check.py` after setup. These statements cover mathematical values. They do not establish that clamping money is the right business rule, nor do they model overflow, concurrent updates, or persistence.
