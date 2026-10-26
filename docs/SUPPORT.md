# Support and evidence

| Tier | Meaning |
|---|---|
| Unprofiled | Generic distribution kernel/initramfs; inventory only |
| Experimental | Profile exists; release gates or variants remain unresolved |
| Community-qualified | Exact components passed functional/recovery checks on specified versions |
| Maintained | Named maintainer, reproducible artifacts, update/recovery policy and regression coverage |

MacPro6,1 is currently experimental. One historical boot does not qualify all D300/D500/D700,
CPU upgrades, docks, SSD replacements or distributions. Other models are unprofiled.
T2 and mixed-mode EFI are distinct tracks.

Evidence levels: source/config → artifacts → boot → per-function observation →
recovery validation → repeated stability measurements. Never promote one level to another.
Physical monitor output and audible sound require observation; enumeration cannot substitute.

Defaults: distribution security/signature policy, generic recovery, configurable thermal policy.
Local maximum fan and mitigations-off settings are not universal defaults.
Unknown root topology always retains an initramfs.

No binary/firmware redistribution is assumed permissible. Review licenses separately.
Original MIT code does not relicense kernel patches or vendor drivers.
