import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from copay import CAP_NOTE, packs_per_year, per_pack_difference, yearly_difference  # noqa: E402


class HandComputedCases(unittest.TestCase):
    """Expected values are the spec's hand-computed cases (AC6, AC7)."""

    def test_sortis_vs_nobel_per_pack(self):
        self.assertEqual(per_pack_difference(86.60, 40, 60.60), 28.58)

    def test_packs_per_year(self):
        self.assertEqual(packs_per_year(1, 100), 4)
        self.assertEqual(packs_per_year(0.5, 30), 7)

    def test_yearly(self):
        self.assertEqual(yearly_difference(86.60, 40, 60.60, 1, 100), 114.32)

    def test_cap_note_wording(self):
        self.assertIn("only 25 points count", CAP_NOTE)
        self.assertIn("remaining 15 points are uncapped", CAP_NOTE)


if __name__ == "__main__":
    unittest.main()
