"""No root writes, installation, network access or sensitive identifier collection."""
import argparse
import importlib.resources
import json
import re
import subprocess
from pathlib import Path

FEATURES = {"lm", "sse4_2", "avx", "avx2", "fma", "f16c", "rdrand"}
HEX_ID = re.compile(r"0x[0-9a-fA-F]{4,8}\Z")

def read(path):
    try:
        return path.read_text().strip()
    except (OSError, UnicodeError):
        return ""

def inventory(root=Path("/")):
    root = Path(root)
    model = read(root / "sys/class/dmi/id/product_name")
    vendor = read(root / "sys/class/dmi/id/sys_vendor")
    cpuinfo = read(root / "proc/cpuinfo")
    cpu_sets = [set(line.split(":", 1)[1].split()) for line in cpuinfo.splitlines()
                if line.startswith("flags") and ":" in line]
    common = set.intersection(*cpu_sets) if cpu_sets else set()
    devices = []
    for dev in sorted((root / "sys/bus/pci/devices").glob("*")):
        fields = {key: read(dev / key) for key in ("vendor", "device", "class")}
        if not all(HEX_ID.fullmatch(v) for v in fields.values()):
            continue
        driver = ""
        try:
            if (dev / "driver").is_symlink():
                driver = (dev / "driver").readlink().name
        except OSError:
            pass
        # No PCI address, MAC, serial, UUID, hostname or network information.
        devices.append({**fields, "driver": driver})
    os_id = "unknown"
    for line in read(root / "etc/os-release").splitlines():
        if line.startswith("ID="):
            value = line.split("=", 1)[1].strip('"')
            if re.fullmatch(r"[a-zA-Z0-9._-]+", value):
                os_id = value
    root_fs = "unknown"
    if root == Path("/"):
        try:
            result = subprocess.run(["findmnt", "-n", "-o", "FSTYPE", "/"],
                                    capture_output=True, text=True, timeout=3, check=False)
            if result.returncode == 0 and re.fullmatch(r"[a-z0-9_]+\n?", result.stdout):
                root_fs = result.stdout.strip()
        except (OSError, subprocess.TimeoutExpired):
            pass
    return {"schema_version": 1, "model": model if re.fullmatch(r"[A-Za-z]+[0-9]+,[0-9]+", model) else "unknown",
            "apple_vendor": vendor in {"Apple Inc.", "Apple Computer, Inc."},
            "distro": os_id, "cpu_features": sorted(common & FEATURES),
            "cpu_features_known": bool(cpu_sets), "pci": devices,
            "root": {"filesystem": root_fs, "topology_verified": False},
            "privacy": "No identifiers collected; still review reports before sharing."}

def profiles():
    directory = importlib.resources.files("intel_mac_linux").joinpath("profiles")
    return [json.loads(p.read_text()) for p in directory.iterdir() if p.name.endswith(".json")]

def validate_inventory(data):
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Unsupported inventory")
    if not isinstance(data.get("model"), str) or not isinstance(data.get("apple_vendor"), bool):
        raise ValueError("Invalid model/vendor")
    for key in ("cpu_features", "pci"):
        if not isinstance(data.get(key), list):
            raise ValueError("Invalid inventory list")
    return data

def plan(data):
    validate_inventory(data)
    matches = [p for p in profiles() if data["apple_vendor"] and data["model"] in p["models"]]
    profile = matches[0] if matches else None
    return {"schema_version": 1, "profile": profile["id"] if profile else None,
            "tier": profile["tier"] if profile else "unverified",
            "adapter": "cachyos (planned)" if data.get("distro") == "cachyos" else "not implemented",
            "cpu_target": "x86-64-v1" if "lm" in data["cpu_features"] else "requires architecture review",
            "initramfs_free_approved": False,
            "reasons": ["Read-only planner; no builder or installer shipped.",
                        "Root topology, firmware and hardware variants require independent validation."],
            "blockers": profile["known_blockers"] if profile else ["No validated model profile."],
            "fallback": "Retain generic distribution kernel and initramfs.",
            "next": "Review model, actual components and evidence before any build."}

def audit_config(profile, text):
    values = {}
    for line in text.splitlines():
        if line.startswith("CONFIG_") and "=" in line:
            key, value = line.split("=", 1)
            values[key[7:]] = value
        elif line.startswith("# CONFIG_") and line.endswith(" is not set"):
            values[line.split()[1][7:]] = "n"
    failures = {key: values.get(key, "absent") for key in profile["required_builtin"]
                if values.get(key) != "y"}
    forbidden = {key: values[key] for key in profile["required_disabled"]
                 if values.get(key) in ("y", "m")}
    return {"profile": profile["id"], "required_failures": failures,
            "forbidden_enabled": forbidden, "pass": not failures and not forbidden,
            "limit": "Configuration assertions only; no package, firmware or boot proof."}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("inventory")
    p = commands.add_parser("plan")
    p.add_argument("--inventory", type=Path)
    p = commands.add_parser("audit-config")
    p.add_argument("config", type=Path)
    p.add_argument("--profile", default="macpro61")
    args = parser.parse_args()
    try:
        if args.command == "inventory":
            result = inventory()
        elif args.command == "plan":
            result = plan(json.loads(args.inventory.read_text()) if args.inventory else inventory())
        else:
            match = next((p for p in profiles() if p["id"] == args.profile), None)
            if match is None:
                raise ValueError("Unknown profile")
            result = audit_config(match, args.config.read_text())
    except (OSError, ValueError, TypeError, KeyError):
        parser.exit(2, "Input could not be validated; no changes made.\n")
    print(json.dumps(result, indent=2))
    return 1 if args.command == "audit-config" and not result["pass"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
