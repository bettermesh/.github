"""Validate public brand assets without third-party dependencies."""

from pathlib import Path
import struct
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "profile/assets"
NS = "{http://www.w3.org/2000/svg}"


class BrandingTests(unittest.TestCase):
    def test_self_contained_accessible_vectors(self):
        for name in ("bettermesh-icon.svg", "bettermesh-logo.svg", "bettermesh-logo-dark.svg"):
            with self.subTest(asset=name):
                svg = ET.parse(ASSETS / name).getroot()
                self.assertEqual(svg.tag, NS + "svg")
                self.assertEqual(svg.get("role"), "img")
                self.assertEqual(svg.get("aria-labelledby"), "title")
                self.assertEqual(svg.find(NS + "title").text, "BetterMesh")
                self.assertEqual(len(svg.findall(".//" + NS + "circle")), 5)
                for element in svg.iter():
                    self.assertIn(element.tag, {NS + tag for tag in ("svg", "title", "g", "rect", "path", "circle")})
                    for attribute, value in element.attrib.items():
                        self.assertNotIn("href", attribute)
                        self.assertNotIn("url(", value)
                        self.assertNotIn("font", attribute)

    def test_theme_variants(self):
        light = (ASSETS / "bettermesh-logo.svg").read_text()
        dark = (ASSETS / "bettermesh-logo-dark.svg").read_text()
        self.assertIn('<path fill="#101E2D"', light)
        self.assertEqual(dark, light.replace("#101E2D", "#F5F8FC"))

    def test_square_avatar(self):
        png = (ASSETS / "bettermesh-icon.png").read_bytes()
        self.assertEqual(png[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(png[12:16], b"IHDR")
        self.assertEqual(struct.unpack(">II", png[16:24]), (1024, 1024))
        self.assertEqual(png[37:41], b"sRGB")
        svg = ET.parse(ASSETS / "bettermesh-icon.svg").getroot()
        self.assertEqual(svg.get("viewBox"), "0 0 1024 1024")

    def test_profile_uses_public_theme_assets(self):
        readme = (ROOT / "profile/README.md").read_text()
        self.assertIn('media="(prefers-color-scheme: dark)"', readme)
        self.assertIn('alt="BetterMesh logo"', readme)
        for name in ("bettermesh-logo.svg", "bettermesh-logo-dark.svg"):
            self.assertIn(
                "https://raw.githubusercontent.com/bettermesh/.github/main/profile/assets/" + name,
                readme,
            )
            self.assertTrue((ASSETS / name).is_file())
        self.assertNotIn("githubusercontent.com/bettermesh/app/", readme)


if __name__ == "__main__":
    unittest.main()
