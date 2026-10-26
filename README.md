# Intel Mac Linux

A community toolkit for evidence-based Linux hardware tailoring on Intel Macs.
CachyOS is the first integration target; the core is designed for additional distributions.

**Status: experimental developer preview.** This repository does not install kernels,
modify firmware, partition disks or guarantee support for every Intel Mac. Apple silicon
is outside scope. No affiliation with Apple, CachyOS, Dortania or OCLP is implied.

## What works here today

- Read-only model, CPU-feature and PCI inventory, omitting hardware serials and account data.
- Exact model/vendor matching against an experimental MacPro6,1 profile.
- Conservative planning that retains the generic kernel and initramfs.
- Resolved kernel-config assertions that catch unwanted drivers re-enabled by dependencies.
- Synthetic tests; no hardware qualification or performance claims.

The existing local Mac Pro experiment is evidence to port, **not a release of this toolkit**.
A 7.3 slim boot was demonstrated on one system. The later 7.3 final rebuild passed artifact
checks but remains uninstalled; the requested CachyOS 7.2.7-1 port remains unbuilt.
Graphics crashes and framebuffer failures remain open blockers.

## Try it without installation or root

From the repository directory:

    PYTHONPATH=src python3 -m intel_mac_linux.cli inventory
    PYTHONPATH=src python3 -m intel_mac_linux.cli plan
    PYTHONPATH=src python3 -m intel_mac_linux.cli audit-config /path/to/resolved.config
    PYTHONPATH=src python3 -m unittest discover -s tests -v

Or install into a disposable virtual environment with pip install ., then use iml.
Inventory prints to stdout and makes no network requests. Review any report before sharing.
A plan never approves initramfs-free boot in this preview: storage-topology and firmware
gates are intentionally not implemented yet.

## Contribute

Start with [component work packages](docs/WORK-PACKAGES.md),
[roadmap](docs/ROADMAP.md), [contribution guide](CONTRIBUTING.md) and
[support policy](docs/SUPPORT.md).
We need kernel/DRM, EFI, packaging, thermal-control, testing and documentation contributors.
Model owners can contribute reviewed, sanitized observations without writing kernel code.

## Architecture

Discovery → component inventory → model profile → compatibility resolution →
reviewable plan → distro build adapter → artifact checks → explicit installation →
user-controlled boot → reported functional validation.

Only the first planning/audit pieces exist today. Future installation must preserve
a working kernel, initramfs and boot entries, and must fail closed on unknown storage.

## Boundaries

No proprietary driver/firmware blobs, Apple keys, account data, VM identities or disk
images belong here. Do not turn a user's local mitigations=off, maximum fan setting or
experimental boot flag into a distribution default. Static wl linking is research only;
the supported design target is an exact-kernel precompiled module without first-boot DKMS.

Original toolkit code is MIT licensed. Any future kernel patches retain their applicable
upstream licenses and attribution. No third-party patches or firmware are bundled yet.
