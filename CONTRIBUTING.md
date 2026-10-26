# Contributing

No code needed: [share your Mac's results](https://github.com/wolffcatskyy/intel-mac-linux/issues/new?template=hardware-results.yml).
See [reporting and review](docs/RESULTS.md).


Pick one ID in docs/WORK-PACKAGES.md. State exact model, component variant, distribution,
kernel and evidence level. Keep PRs focused; describe what was and was not tested.
Do not claim support from a profile match alone.

Run: PYTHONPATH=src python3 -m unittest discover -s tests -v

No root/hardware is needed for fixtures or documentation. Add meaningful failure-path tests:
missing data, unknown devices, dependency re-enablement and fallback selection.

Do not submit serials, UUIDs, MACs, private logs, account data, VM images, credentials,
Apple keys, proprietary objects or firmware blobs. Review reports before sharing.

Discovery/planning must not reboot, replace boot defaults, partition, remove mitigations,
flash firmware or change fan policy. Privileged actions need a separate reviewed plan/rollback.

Preserve upstream licenses/authors. Check exact kernel revisions and resolved configuration.
Cite primary technical sources; forum reports are observations, not universal proof.

Disclose generated code in PRs and verify it. AI-generated claims are not evidence.
