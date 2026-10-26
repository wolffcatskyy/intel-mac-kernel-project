# Roadmap

Milestones are acceptance gates, not promised dates. All Intel Macs are a long-term scope,
not a current compatibility claim.

| Milestone | Deliverable | Exit gate | Current state |
|---|---|---|---|
| 0.1 Discover and plan | Privacy-aware inventory, profiles, config audit, contribution workflow | Tests pass; unknown models fail closed; reports omit identifiers; schema documented | Initial prototype present; review needed |
| 0.2 Reference Mac Pro build | Reproducible CachyOS adapter, 7.2.7-1 and 7.3 compatibility, signed firmware manifest, matched wl | Clean build, full resolved config assertions, package hashes/licenses, actual boot and recovery evidence | Not implemented here |
| 0.3 Boot and recovery | Root-topology checks, optional initramfs-free path, atomic boot-entry handling | Unknown/LUKS/LVM/complex roots retain initramfs; fallback independently verified | Planned |
| 0.4 Mac Pro qualification | Graphics, audio, Wi-Fi, Ethernet, fan failure handling, Thunderbolt and storage | Per-function observations on actual variants; no unresolved release-blocking regressions | GPU issue remains blocker |
| 0.5 More Intel Mac families | Community-owned MacPro5,1, selected iMac/Mac mini/MacBook profiles | Separate component/CPU/EFI variant evidence; qualification owner | No supported profiles yet |
| 0.6 More distributions | Arch reuse, then Debian/Ubuntu and Fedora package/boot adapters | Each adapter preserves native updates, signing and recovery; CI and real boot evidence | Planned |
| Research tracks | Mixed 32-bit EFI, T2, Windows deployment | Dedicated expertise, hardware and maintainers; no inherited Linux support claim | Research only |

## Release gates

- No claim of improved speed, memory consumption or stability without a reproducible baseline.
- No universal kernel: actual replacement GPUs, adapters and storage layouts matter.
- No trimming based only on installer-loaded modules; collect components and declared peripherals.
- No automatic firmware updates, signature bypasses, mitigation removal or fixed maximum fan policy.
- Hardware changes and unsupported layouts select the generic recovery path.
- Distribution and kernel versions remain explicit in evidence records.
- An artifact check is not proof of boot, monitor output, audio or Messages.

## Active reference priorities

1. Preserve the running system and finish separately managed Tahoe work; no host reboot from this project.
2. Port the compatible reference package to exact CachyOS 7.2.7-1, checking resolved options and patches.
3. Investigate video-player Mesa aborts and framebuffer ENOMEM; distinguish separate browser/flicker symptoms.
4. Resolve package provenance, firmware updates and offline precompiled wl packaging.
5. Qualify recovery before a public installation release.

Tahoe/Reims is a separate optional integration, not evidence of kernel quality.
No Apple sign-in credentials, private VM assets or guaranteed Messages activation are supplied.
