# Preserve both branches of a Boolean policy

The Bend starter defines `allowed(enabled, authorized)`: a disabled feature rejects every authorization value; an enabled feature returns the authorization value.

Two laws state both behaviors. They cover the actual pure Bend definition, not a real identity system or permission store. A temporary semantic mutation changes the disabled branch to `True{}`. The same law and proof must reject it.

See [the Bend starter](../templates/bend/) for the exact checker, trust boundary, and run instructions. Boolean inputs are assumptions. The proof does not establish where authorization comes from or whether the surrounding application checks it.
