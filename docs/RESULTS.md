# Share results — no code required

[Share your Mac's results](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues/new?template=hardware-results.yml)

Anyone with a GitHub account can fill out the form. No fork, pull request, terminal command,
custom kernel or toolkit installation is required. Stock-distribution observations, failures
and partial results all help. Choose "Not tested / unknown" when appropriate.
Do not perform extra hardware stress tests, change partitions or risk reboot just to contribute.

Report exact model and distribution, kernel if known, component upgrades if known, and what
you actually observed: boot, displays, video playback, audio, networking, peripherals and sleep.
Recovery is its own question: a normal boot does not prove the fallback works.

Optional inventory:

    PYTHONPATH=src python3 -m intel_mac_linux.cli inventory > my-mac-report.json

This writes only the file you explicitly redirect to; nothing is uploaded automatically.
Review the file before attaching it. Do not attach serials, UUIDs, MACs, credentials,
private paths, account information or raw personal logs. Screenshots should be cropped.

## How results become support evidence

1. Submission is a community observation, not automatic validation.
2. A maintainer checks model/component variants, software versions and clarity.
3. Reports are linked to relevant work packages/regressions; contradictory results remain visible.
4. Profile qualification requires its documented functional and recovery gates.
5. Only a reviewed profile PR changes a support tier.

A future dashboard may summarize reviewed submissions. It must preserve version, hardware
variant, evidence level and unknown/not-tested states rather than turn every report into a
green check. No public write access to code or unauthenticated upload service is needed.

GitHub requires an account for this route. An account-free submission service would be separate
future work with moderation, abuse prevention and explicit privacy handling; none exists today.
