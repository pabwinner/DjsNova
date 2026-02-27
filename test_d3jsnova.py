# test_d3jsnova.py
"""
Tests for D3jsNova module.
"""

import unittest
from d3jsnova import D3jsNova

class TestD3jsNova(unittest.TestCase):
    """Test cases for D3jsNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = D3jsNova()
        self.assertIsInstance(instance, D3jsNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = D3jsNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
