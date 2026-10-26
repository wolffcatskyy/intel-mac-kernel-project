# Developer quickstart

The current preview implements read-only model/CPU/PCI discovery, experimental profile matching,
conservative planning and resolved kernel-config auditing. It does not build or install kernels.
No support tier or performance benefit is inferred from a successful configuration check.

From the repository directory:

    PYTHONPATH=src python3 -m intel_mac_linux.cli inventory
    PYTHONPATH=src python3 -m intel_mac_linux.cli plan
    PYTHONPATH=src python3 -m intel_mac_linux.cli audit-config /path/to/resolved.config
    PYTHONPATH=src python3 -m unittest discover -s tests -v

No root access or network is required. Reports print to stdout; review before sharing.
A plan never approves initramfs-free boot in this preview: storage/firmware gates are future work.
To install the CLI into a disposable virtual environment, use pip install . and run iml.

The wheel bundles the experimental model profile. Five synthetic tests and a local wheel build
passed during scaffolding; public CI and physical qualification are separate evidence.
See ROADMAP.md for build, boot/recovery and graphics blockers.

Discovery → component inventory → model profile → compatibility resolution →
reviewable plan → distro build adapter → artifact checks → explicit installation →
user-controlled boot → functional validation.

Only discovery, initial planning and config assertions are implemented here.
