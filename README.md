# Intel Mac Kernel Project

**A future for Intel Macs. Linux built for their hardware.**

## Apple is moving on. These Macs still have work to do.

MacBooks, iMacs, Mac minis and Mac Pros remain capable computers. As their macOS
upgrade paths close, Linux offers a way to keep them useful. The transition should
be easier than searching years of forum posts for the right combination of drivers,
kernel settings and model-specific workarounds.

**The Intel Mac Kernel Project aims to turn that scattered knowledge into reusable,
tested hardware profiles and tools that Linux distributions and Mac owners can use.**

[Share your Mac’s results](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues/new?template=hardware-results.yml) ·
[Find a contributor task](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues) ·
[See the roadmap](docs/ROADMAP.md)

## The hardware still works. The missing piece is a shared support effort.

Linux gives Intel Macs a future beyond their last supported macOS release. But being
able to boot Linux and having a Mac that works well every day are different things.

Apple designed these computers as complete systems. Graphics, firmware, audio, input
devices and power management vary across generations, and some need support that a
generic installation cannot supply on its own. Owners can end up piecing together
drivers, patches and boot settings before the machine feels complete.

The community has already done much of that work. The problem is making it travel:
a fix discovered for one model should become something the next owner can use, a
distribution can package and a maintainer can check against the next kernel.

**That is what the Intel Mac Kernel Project is being built to do.**

We’re bringing model-specific knowledge into a shared configuration database, then
combining it with hardware detection to build for the Mac actually in front of us.
That means accounting for the differences between a MacBook and an iMac, between
hardware generations, and between an original machine and one its owner has upgraded.

The work spans connectivity, graphics, sound, keyboards and trackpads, battery and
cooling behavior, storage and boot compatibility. Each tested improvement can become
a reusable part of a model profile instead of another workaround buried in a thread.

**The ambition: make choosing Linux the beginning of a Mac’s next chapter, rather
than the beginning of another troubleshooting project.**

See the [roadmap](docs/ROADMAP.md) for development work and the
[support matrix](docs/SUPPORT.md) for current coverage.

## Known configurations, verified against the actual hardware

The starting point is a database of reviewed model profiles: required kernel options,
drivers, firmware, quirks and known limitations, tied to the versions they were tested on.

Hardware detection augments that baseline with the components and storage layout
actually present. Optional driver-use history can capture peripherals and features
that are not active during installation. Kernel dependency checks then turn those
inputs into a buildable configuration.

The intended result is a smaller, hardware-appropriate kernel with the support the
machine needs. Compatible installations can boot without an initramfs; encryption
and other setups that need early userspace retain a minimal one. A working recovery
option remains part of the design.

## Shared across models and distributions

The goal is a common foundation for Intel Mac support across Linux distributions.
Distribution adapters handle packaging, installation and updates; model profiles
capture hardware knowledge that can be reused across them.

CachyOS is the initial integration target. The architecture welcomes other
distributions and contributions from owners of any Intel Mac family.

This is an independent community project in early development.

## Every Mac owner can contribute

You do not need to write code, build a kernel or install this toolkit to help.
Reports from ordinary Linux installations are useful: what works, what fails,
which components were upgraded and which features remain untested.

**[Share your Mac’s results →](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues/new?template=hardware-results.yml)**

A GitHub account is needed to submit the form. Reports are reviewed before becoming
reusable configuration guidance. [How community reports are reviewed](docs/RESULTS.md).

## Help build it

We welcome kernel developers, distribution maintainers, hardware owners, testers
and documentation contributors. Help expand model coverage, turn known fixes into
maintainable profiles, improve installation or validate updates and recovery.

- [Open contributor tasks](https://github.com/wolffcatskyy/intel-mac-kernel-project/issues)
- [Component work packages](docs/WORK-PACKAGES.md)
- [Roadmap](docs/ROADMAP.md)
- [Contribution guide](CONTRIBUTING.md)
- [Developer quickstart](docs/DEVELOPMENT.md)
- [Support and evidence policy](docs/SUPPORT.md)

## License

Original toolkit code is MIT licensed. Third-party components retain their own licenses.
