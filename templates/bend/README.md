# Bend starter

A pure Boolean policy with separate application code, laws, and proofs. A disabled feature rejects all authorization values. An enabled feature preserves its authorization input. This is not a real authorization service.

Use Bend source commit `ca77ef289bf6e199a0cb95adb9804c0f58d991f0`, reporting version 2.0.40, Bun 1.4.2, and Lean 4.34.0. The pinned setup below includes the source archive and hashes. Do not substitute a floating Bend release and assume this receipt still applies.

```sh
export BEND_SOURCE=/path/to/bend-ca77ef289bf6e199a0cb95adb9804c0f58d991f0
python3 check.py
```

Copy this whole directory to start a project. Set `BEND_SOURCE` to the pinned source directory. The checker invokes Bun with `--no-env-file --no-config`, checks the two laws using `--verdict`, then changes only the disabled branch to return true. The unchanged law must reject that syntactically valid semantic mutation. No parent-repository files are required.

`--verdict` rechecks translated terms with Bend's kernel formalized in Lean. Bend's parser, translation into that kernel, compiler backends, and runtime are outside that formalization. The language is young. Treat this as an experimental educational starter and inspect its trust boundary before production use. The default checker is not silently accepted if `--verdict` cannot run.

## Pinned setup on Linux x86_64

Requirements: Python 3.11+, Node/npm, curl, tar, sha256sum, and zstd. These commands install into a temporary directory, not a global toolchain.

```sh
mkdir -p /tmp/pdd-bend-tools
npm install --prefix /tmp/pdd-bend-tools/bun bun@1.4.2
export PATH=/tmp/pdd-bend-tools/bun/node_modules/.bin:$PATH
curl -fL https://github.com/leanprover/lean4/releases/download/v4.34.0/lean-4.34.0-linux.tar.zst -o /tmp/pdd-bend-tools/lean.tar.zst
printf '%s  %s\n' caaa98356098c85dc0fcbbd28e1ec66f39eb6551829972b752ff20e1286b646b /tmp/pdd-bend-tools/lean.tar.zst | sha256sum -c -
tar --zstd -xf /tmp/pdd-bend-tools/lean.tar.zst -C /tmp/pdd-bend-tools
export PATH=/tmp/pdd-bend-tools/lean-4.34.0-linux/bin:$PATH
curl -fL https://codeload.github.com/bendlang/bend/tar.gz/ca77ef289bf6e199a0cb95adb9804c0f58d991f0 -o /tmp/pdd-bend-tools/bend.tar.gz
printf '%s  %s\n' fe358d46fdc40f3f89368e3fdd80280492afcde8d1b2403995b4322cbef0feb6 /tmp/pdd-bend-tools/bend.tar.gz | sha256sum -c -
tar -xzf /tmp/pdd-bend-tools/bend.tar.gz -C /tmp/pdd-bend-tools
export BEND_SOURCE=/tmp/pdd-bend-tools/bend-ca77ef289bf6e199a0cb95adb9804c0f58d991f0
python3 check.py
```

Both checks must print `PASS`. A missing kernel or a version mismatch fails the command. This setup was checked on Linux x86_64. Other platforms require the corresponding official Lean and Bun distributions and a new verification run.
