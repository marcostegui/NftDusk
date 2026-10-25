# test_nftdusk.py
"""
Tests for NftDusk module.
"""

import unittest
from nftdusk import NftDusk

class TestNftDusk(unittest.TestCase):
    """Test cases for NftDusk class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftDusk()
        self.assertIsInstance(instance, NftDusk)

    def test_run_method(self):
        """Test the run method."""
        instance = NftDusk()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
