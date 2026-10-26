# Outreach plan and draft

Draft only; no outreach sent. No OCLP/Dortania/CachyOS affiliation is claimed.

Potential contributors:
- Interested OCLP/OpenCore volunteers: model quirks, EFI/ACPI, mixed-mode boot and recovery.
- DRM/Mesa volunteers: Tahiti regression, decode versus scanout separation.
- t2linux volunteers: separately maintained T2 boundary, if they choose to participate.
- CachyOS/Arch packagers: kernel, offline wl and update/fallback integration.
- Model owners: sanitized inventory and bounded functional observations.

Follow each community's preferred channels/rules. Do not file recruitment spam as bugs,
mass-tag contributors or ask another project's team to take ownership. Offer a small task
with evidence, clear boundaries and an easy way to decline.

## Draft introduction

We're building an independent, experimental Intel Mac Linux hardware-tailoring toolkit,
starting with CachyOS on MacPro6,1. The aim is reusable model profiles and distro adapters,
with generic recovery preserved and initramfs-free boot only where verified.
This is not an OCLP fork or affiliated project.

The first repository contains read-only discovery/planning code and tests. The local
reference experiment has boot evidence, but graphics regressions and release qualification
remain open. We welcome volunteers for specific tasks: EFI/model review (IML-16/19),
Tahiti DRM investigation (IML-12), packaging (IML-07/08), and recovery design (IML-11).
Sanitized reports and documentation corrections are welcome.

If interested, choose one scoped task. We'd also appreciate advice on existing work we
should reuse and credit rather than duplicate. Repository URL: [add after publication].
