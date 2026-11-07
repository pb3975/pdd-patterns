import Base
import ./App.bend as App

law disabled_rejects:
  for authorized: Bool
  {App.allowed(False{}, authorized) == False{} : Bool}

law enabled_preserves_authorization:
  for authorized: Bool
  {App.allowed(True{}, authorized) == authorized : Bool}
