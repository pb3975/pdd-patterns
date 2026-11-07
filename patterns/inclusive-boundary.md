# Accept exactly at the boundary

Use this when the requirement has both a safety condition and a useful permitted outcome. Rejecting every action can satisfy a one-way safety statement while breaking the product.

Contract: accept if and only if `amount <= limit - spent`, assuming nonnegative values and `spent <= limit`. Zero amount is allowed in these teaching examples. A real payment specification may exclude it.

Implementation: `spent + amount <= limit`.

Negative control: replace only the implementation's `<=` with `<`. Leave the contract and proof unchanged. The equality case becomes a counterexample.

- [Lean definition and theorem](../templates/lean/Patterns.lean): proves the relation for the actual Lean definition.
- [Z3 model](../templates/z3/boundary.smt2): proves the relation for a separate integer model.

Run each starter's `python3 check.py` after its setup. They verify the correct artifact and reject the semantic mutation. Neither proves an account database or concurrent payment service.
