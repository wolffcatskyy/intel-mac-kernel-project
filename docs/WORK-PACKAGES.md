# Contributor work packages

IML IDs identify work packages. All 24 packages now have linked GitHub issues and are unassigned.
Contributors may claim one scoped task by issue comment or PR.
Acceptance gates must be independently reviewable. Size is relative, not a delivery estimate.

| ID | Component / deliverable | Useful expertise | Size | Depends on | Acceptance evidence |
|---|---|---|---|---|---|
| [IML-01](https://github.com/wolffcatskyy/intel-mac-linux/issues/1) | Versioned inventory/profile schemas | Python, JSON Schema | Small | — | Valid/invalid fixtures; unknown-fields policy; no private identifiers |
| [IML-02](https://github.com/wolffcatskyy/intel-mac-linux/issues/2) | PCI/USB and replacement-component matching | Linux sysfs | Medium | 01 | Fixtures distinguish swapped GPUs, storage adapters and unknown IDs |
| [IML-03](https://github.com/wolffcatskyy/intel-mac-linux/issues/3) | CPU capability and userspace ISA guard | x86 toolchains | Medium | 01 | Per-core intersection; missing flags/32-bit CPU cases; no AVX2 on Ivy Bridge |
| [IML-04](https://github.com/wolffcatskyy/intel-mac-linux/issues/4) | Root topology and initramfs eligibility | storage, initramfs | Large | 01 | LUKS/LVM/MD/overlay/multi-device fixtures fail closed; direct-root case |
| [IML-05](https://github.com/wolffcatskyy/intel-mac-linux/issues/5) | Firmware manifest/signature pipeline | firmware, crypto | Medium | 01 | Early files/signatures identified; hashes/update path; no bundled blobs |
| [IML-06](https://github.com/wolffcatskyy/intel-mac-linux/issues/6) | Resolved Kconfig dependency audit | Kconfig | Medium | 01 | Catch re-enabled drivers and required=y becoming=m; version-specific symbols |
| [IML-07](https://github.com/wolffcatskyy/intel-mac-linux/issues/7) | CachyOS 7.2.7-1 build adapter | Arch packaging, LLVM | Large | 03,05,06 | Verified source/signature; strict patches; clean packages and exact release |
| [IML-08](https://github.com/wolffcatskyy/intel-mac-linux/issues/8) | Offline matched wl module package | modules, packaging | Medium | 07 | Exact vermagic/dependency; no first-boot DKMS; proper license files |
| [IML-09](https://github.com/wolffcatskyy/intel-mac-linux/issues/9) | Reproducible build/cache management | build systems | Medium | 07 | RAM tree reconstructs after reboot; persistent caches; bounded resources |
| [IML-10](https://github.com/wolffcatskyy/intel-mac-linux/issues/10) | Artifact verification/provenance | Python, ELF, packaging | Medium | 05,07,08 | Image/module hashes, firmware bytes, final config, compiler/source commit |
| [IML-11](https://github.com/wolffcatskyy/intel-mac-linux/issues/11) | Transaction-safe boot installation | Limine/GRUB/systemd-boot | Large | 04,10 | Disposable-fixture rollback; default/fallback preserved; no automatic reboot |
| [IML-12](https://github.com/wolffcatskyy/intel-mac-linux/issues/12) | MacPro6,1 AMDGPU/Mesa regression | DRM, Mesa, Tahiti | Large | — | Correlated logs; same-userspace kernel comparison; decode/render/scanout separated |
| [IML-13](https://github.com/wolffcatskyy/intel-mac-linux/issues/13) | SMC fan control and failure handling | hwmon, systemd | Large | 02 | Configurable policy; measured RPM/limits; sensor failure and cleanup tests |
| [IML-14](https://github.com/wolffcatskyy/intel-mac-linux/issues/14) | Cirrus/HDMI/USB audio qualification | ALSA/PipeWire | Medium | 02 | Actual codec/SSID; upstream quirks checked; each output observed |
| [IML-15](https://github.com/wolffcatskyy/intel-mac-linux/issues/15) | Thunderbolt/PCIe hotplug | PCIe/EFI | Large | 02 | Model/topology evidence; attach/detach results; no blanket resource flags |
| [IML-16](https://github.com/wolffcatskyy/intel-mac-linux/issues/16) | MacPro5,1 profile research | classic Mac Pro owners | Medium | 01,02 | CPU/GPU/EFI/storage variants; unknown replacements retain generic kernel |
| [IML-17](https://github.com/wolffcatskyy/intel-mac-linux/issues/17) | iMac/Mac mini pilot profiles | model owners | Medium | 01,02 | One exact model/variant per PR; sanitized fixtures and limits |
| [IML-18](https://github.com/wolffcatskyy/intel-mac-linux/issues/18) | Laptop power/input/suspend | Apple laptops, input | Large | 02,13 | Keyboard/trackpad/battery/sleep evidence; no copied desktop policy |
| [IML-19](https://github.com/wolffcatskyy/intel-mac-linux/issues/19) | 32-bit EFI discovery/recovery | EFI/OpenCore | Large | 03,11 | Firmware/CPU bitness separated; actual hardware recovery evidence |
| [IML-20](https://github.com/wolffcatskyy/intel-mac-linux/issues/20) | T2 integration boundary | t2linux, Apple BCE | Large | 02,11 | Reviewed external dependencies/boot policy; no generic T2 claim |
| [IML-21](https://github.com/wolffcatskyy/intel-mac-linux/issues/21) | Debian/Ubuntu adapter | deb/kernel packaging | Large | 10,11 | Native update/signing/recovery semantics; prototype fixtures |
| [IML-22](https://github.com/wolffcatskyy/intel-mac-linux/issues/22) | Fedora adapter | rpm, dracut, Secure Boot | Large | 10,11 | Native update/signing/recovery semantics; prototype fixtures |
| [IML-23](https://github.com/wolffcatskyy/intel-mac-linux/issues/23) | Read-only Windows/deployment research | PowerShell, DISM, Boot Camp | Medium | 01 | Common PCI schema; signed driver sources; no custom NT kernel claim |
| [IML-24](https://github.com/wolffcatskyy/intel-mac-linux/issues/24) | Documentation and report review | writers, model owners | Small | — | Runnable quickstart; sanitized example; evidence levels explained |

## Good first contributions

- IML-24: run the quickstart and correct one concrete documentation gap.
- IML-01: add a malformed-inventory fixture and expected refusal.
- IML-02: submit one sanitized PCI/USB fixture; omit serials/MACs/UUIDs.
- IML-06: add a required-built-in-becomes-module fixture and verify rejection.
- IML-17: document one model's variants; this does not automatically grant support.

## Release-blocking roles

Need owners for packaging, DRM regression, recovery/boot safety, thermal policy and
model qualification. Maintainers review claims/provenance before tier promotion.
No unsolicited messages, mass tagging or assumed commitments from other volunteers.
