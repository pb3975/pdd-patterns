import Std

-- Preconditions are part of the theorem. Nat subtraction truncates at zero.
def allow (spent amount limit : Nat) : Bool :=
  decide (spent + amount ≤ limit)

theorem allow_exactly (spent amount limit : Nat) (h : spent ≤ limit) :
    allow spent amount limit = true ↔ amount ≤ limit - spent := by
  simp [allow]
  omega

-- Clamp is an idempotent upper bound, not a concurrency-safe budget store.
def clamp (limit value : Nat) : Nat := min limit value

theorem clamp_bounded (limit value : Nat) : clamp limit value ≤ limit := by
  exact Nat.min_le_left limit value

theorem clamp_idempotent (limit value : Nat) :
    clamp limit (clamp limit value) = clamp limit value := by
  simp [clamp]

theorem clamp_preserves (limit value : Nat) (h : value ≤ limit) :
    clamp limit value = value := by
  exact Nat.min_eq_right h

theorem clamp_caps (limit value : Nat) (h : limit ≤ value) :
    clamp limit value = limit := by
  exact Nat.min_eq_left h

#print axioms clamp_preserves
#print axioms clamp_caps
#print axioms allow_exactly
#print axioms clamp_bounded
#print axioms clamp_idempotent
