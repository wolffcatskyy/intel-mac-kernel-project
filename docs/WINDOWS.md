# Optional Windows research track

Future companion integration, not a current product or custom Windows kernel.
Normal deployment uses Microsoft's kernel and separate signed drivers. DISM can stage
driver packages into Windows/WinPE images; it does not statically link them into NT.

Reusable: model/component schema, compatibility evidence, driver provenance, recovery plans.
Windows-specific: read-only PowerShell collector, official Boot Camp/driver acquisition
and license review, signature checks, recovery media and optional offline DISM deployment.
No Windows binaries, activation material, signing bypasses or modified proprietary kernel.

Apple documents Boot Camp installation of Windows 10. Check Windows 11 CPU, UEFI/Secure Boot
and TPM requirements individually. A bypassed installation is not official vendor support.

Sources:
- https://support.apple.com/en-ie/102622
- https://www.microsoft.com/en-us/windows/windows-11-specifications
- https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/add-and-remove-drivers-to-an-offline-windows-image?view=windows-11

IML-23 starts with research/discovery. No Windows image builder is implemented.
