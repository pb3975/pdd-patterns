import Base

# Both enabled and authorized are required. No external authorization is modeled.
def allowed(enabled: Bool, authorized: Bool) -> Bool:
  match enabled:
    case True{}:
      authorized
    case False{}:
      False{}
