# Intel Mac Kernel Project

**Keeping Intel Macs useful with Linux built for their hardware.**

## Apple is moving on from Intel Macs. We’re building what comes next.

Millions of Intel Macs still have useful life ahead of them. As their macOS upgrade paths
close, Linux gives owners another way forward. We’re building the tools to make that
transition easier—and to help Linux work better on the hardware people already own.

The goal is simple: **keep good Macs useful, with less guesswork and fewer workarounds.**

[Share your Mac’s results](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues/new?template=hardware-results.yml) ·
[Find a contributor task](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues) ·
[See the roadmap](docs/ROADMAP.md)

## Your Mac still has life in it. Getting Linux right shouldn’t be a research project.

Installing Linux is only the beginning. Depending on the Mac model and its upgrades, the
next challenge can be getting Wi-Fi online, making the internal speakers work, keeping an
external display connected, or finding a cooling setup you can trust.

The fixes exist in scattered patches, distribution packages and years of forum posts.
Too often, every owner has to assemble—and troubleshoot—the same puzzle again.

**We’re building a shared, model-aware foundation to do that work once and make it reusable.**

## The Mac-specific problems we’re tackling

- **Wi-Fi that needs a driver before you can get online.** Match Broadcom hardware to the
  right driver, handle conflicting drivers, and package a matching precompiled driver
  where needed so installation doesn’t depend on first-boot compilation.
- **Speakers, headphone jacks and display audio that behave differently.** Bring together
  model-specific codec quirks and tested audio configurations.
- **Black screens, flicker and unreliable external displays.** Track GPU generations,
  driver selection, firmware, connector behavior and kernel regressions by actual hardware.
  The dual-GPU Mac Pro needs its own treatment.
- **Cooling and sensors that need Apple-specific support.** Include the right SMC support
  and develop supervised fan policies suited to each model.
- **Thunderbolt, replacement SSDs and Apple boot firmware.** Account for controller
  dependencies, hotplug, AHCI-to-NVMe upgrades and model-specific EFI requirements.
- **Advice that stops working after an update.** Record which fixes apply to which hardware
  and kernel versions, then check that the required settings survive configuration changes.

These are the project’s work areas; the [roadmap](docs/ROADMAP.md) and
[support matrix](docs/SUPPORT.md) show their current maturity.

## A kernel built for the Mac you actually own

Start with a database of tested model profiles. Augment it with live hardware detection
and, where available, a history of drivers used on that machine. Account for upgrades
rather than assuming every Mac with the same model name is identical.

From those inputs, the toolkit will resolve the drivers, firmware and dependencies needed
for a tailored kernel, trimming unrelated hardware support while keeping a working
recovery option. Compatible layouts can boot without an initramfs; encrypted-root and
other complex setups can retain a minimal one.

**The goal is working hardware, easier installation and updates that preserve the fixes—not
just a smaller kernel file.**

## Start with CachyOS. Build for the wider Linux community.

CachyOS and the Mac Pro 6,1 are our starting point. The longer-term goal is a shared
foundation for more Intel Mac families and more Linux distributions, with each combination
earning support through testing and community experience.

An independent, community-led project in early development.

## Your results can help—even if you don’t write code

Have Linux running on an Intel Mac? Tell us what works, what fails and what you haven’t
tested. Stock installations, upgraded machines and unsuccessful attempts are all useful.

**[Share your Mac’s results →](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues/new?template=hardware-results.yml)**

No fork or custom kernel is required. A GitHub account is needed to submit the form.
[How community reports are reviewed](docs/RESULTS.md).

## Help build it

We welcome developers, packagers, hardware owners, testers and writers. There are specific
tasks for kernel and graphics work, EFI and recovery, thermal control, distro integration,
hardware profiles and documentation.

- [Open contributor tasks](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues)
- [Component work packages](docs/WORK-PACKAGES.md)
- [Roadmap](docs/ROADMAP.md)
- [Contribution guide](CONTRIBUTING.md)
- [Developer quickstart](docs/DEVELOPMENT.md)
- [Support and evidence policy](docs/SUPPORT.md)

## License

Original toolkit code is MIT licensed. Third-party components retain their own licenses.
