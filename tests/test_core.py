import json
import tempfile
import unittest
from pathlib import Path
from intel_mac_linux.cli import inventory, plan, profiles, audit_config

class CoreTests(unittest.TestCase):
    def test_inventory_omits_identity_and_intersects_cpu_features(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = {"sys/class/dmi/id/product_name": "MacPro6,1",
                     "sys/class/dmi/id/sys_vendor": "Apple Inc.",
                     "sys/class/dmi/id/product_serial": "SECRET_SERIAL",
                     "proc/cpuinfo": "flags : lm avx avx2 fma\nflags : lm avx\n",
                     "etc/os-release": 'ID=cachyos\n'}
            for name, value in files.items():
                p = root / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(value)
            data = inventory(root)
            self.assertNotIn("SECRET_SERIAL", json.dumps(data))
            self.assertEqual(data["cpu_features"], ["avx", "lm"])
            self.assertEqual(plan(data)["profile"], "macpro61")
            self.assertFalse(plan(data)["initramfs_free_approved"])

    def test_unknown_vendor_never_matches_apple_model_string(self):
        data = {"schema_version": 1, "model": "MacPro6,1", "apple_vendor": False,
                "cpu_features": ["lm"], "pci": []}
        self.assertIsNone(plan(data)["profile"])

    def test_malformed_input_fails_closed(self):
        for data in [None, {}, {"schema_version": 1, "model": [], "apple_vendor": True}]:
            with self.assertRaises(ValueError):
                plan(data)

    def test_config_rejects_dependency_reenabled_driver(self):
        profile = profiles()[0]
        text = "\n".join("CONFIG_"+key+"=y" for key in profile["required_builtin"])
        self.assertTrue(audit_config(profile, text)["pass"])
        result = audit_config(profile, text+"\nCONFIG_IEEE802154=y\n")
        self.assertFalse(result["pass"])
        self.assertIn("IEEE802154", result["forbidden_enabled"])

    def test_module_does_not_satisfy_builtin_requirement(self):
        profile = profiles()[0]
        self.assertFalse(audit_config(profile, "CONFIG_SATA_AHCI=m\n")["pass"])

if __name__ == "__main__":
    unittest.main()
