# Decisions

## 2026-11-07: Private review collection

Will requested patterns, examples, agent skills, and starter templates, with public publication only after approval. The collection is separate from the existing public website source. Website hosting remains offline pending Vercel credentials.

## 2026-11-07: Small checked examples

Use two arithmetic patterns and a small Bend Boolean policy, each with direct specifications and semantic mutations. Z3 checks separate unbounded integer models. Lean checks the definitions in its own language. These checks do not establish JavaScript, machine-code, database, network, or concurrent-system correctness. Pin proof tools and keep runtime dependencies out of website content.

## 2026-11-07: Shared pinned Lean version

Use Lean 4.34.0 for both the Lean starters and Bend's kernel build. The pinned Bend 2.0.40 source rejects Lean 4.35.0 for its `--verdict` infrastructure. CI and the local receipts use Lean 4.34.0, Z3 4.15.4, Bun 1.4.2, and Bend commit `ca77ef289bf6e199a0cb95adb9804c0f58d991f0`. Lean and Bend source archives are checksum-verified before use.

## 2026-11-07: Complete clamp contract

Review found that bound plus idempotence also permits constant zero. Preserve both properties and add preservation at or below the cap and the exact cap above it. Both Lean and Z3 reject input-value and constant-zero mutations against the strengthened contract. This is a concrete example of a valid proof of an incomplete specification giving false confidence.

## 2026-11-11: Inbox: proof-driven-development/public-release

Will approved public release under the MIT license: "Publish under MIT." The reviewed candidate is commit 2a6e482bf53d82d8a6910c99da7be160f56bf1ab, merged to `main` as dac6cd7. Its CI was rerun and passed on November 11, 2026. The proposed license text moves to `LICENSE` unchanged. A scan of the full history found no credentials. The website links this repository. Will asked to keep the website's source repository private, so this repository does not link to it.
