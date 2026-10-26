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

## What your Mac needs. Without what it doesn’t.

A general-purpose Linux kernel must support an enormous range of computers. Your Mac
has a particular set of components. It doesn’t need every other computer’s drivers,
but it does need the right support for its own hardware.

**The Intel Mac Kernel Project aims to make both sides deliberate: include the support
your Mac needs, and leave out unrelated hardware support.**

### What goes in

- **Drivers for the actual hardware:** graphics, storage, networking, audio, input
  devices and the buses that connect them.
- **Mac-specific support:** applicable Apple platform drivers, model-specific quirks
  and reviewed fixes that may otherwise require manual configuration or patches.
- **Required firmware and dependencies:** identify what each driver needs, including
  firmware needed before the root filesystem becomes available.
- **Support for the way you use the machine:** encryption, virtualization, filesystems,
  peripherals and upgraded components belong in the configuration when required.
- **Versioned configuration rules:** preserve those requirements when kernel options
  and dependencies change.

### What stays out

- **Drivers for unrelated hardware**, once the profile and hardware checks establish
  that they are unnecessary.
- **Unused platform and subsystem support**, where removing it does not break a required
  feature, dependency or selected peripheral.
- **One-size-fits-all workarounds:** a fix for one Mac family should not become an
  unexplained setting on every Intel Mac.

Much of the necessary support already exists in Linux. The job is to select it correctly,
bring applicable fixes together and avoid carrying unrelated support simply because a
generic kernel must accommodate other machines.

Built-in drivers can remove the need to load modules during boot. Compatible storage
layouts can also boot without an initramfs. Neither is an absolute rule: encrypted-root
setups can keep a minimal initramfs, and drivers that require separate packaging remain
explicit exceptions.

### Why size matters

A Mac should not need a collection of drivers for thousands of devices it will never
contain. Removing that unrelated support can make the installed kernel and driver
collection substantially smaller.

That means **less disk space, smaller kernel downloads and updates, and less code to
compile and package**. For older machines with limited storage, those savings are
practical—not cosmetic.

Size also needs an honest comparison. Moving drivers and firmware into the kernel can
make the kernel file itself larger while making the complete boot and driver package
smaller. We measure the whole result, including modules, firmware and any initramfs.
Smaller files alone do not prove lower RAM use or faster execution; those benefits
need their own measurements.

**Keep the hardware support. Lose the unnecessary bulk.**

These are design goals. The [support matrix](docs/SUPPORT.md) records current coverage;
the [roadmap](docs/ROADMAP.md) tracks what remains to build.

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
