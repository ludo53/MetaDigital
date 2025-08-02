# test_metadigital.py
"""
Tests for MetaDigital module.
"""

import unittest
from metadigital import MetaDigital

class TestMetaDigital(unittest.TestCase):
    """Test cases for MetaDigital class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaDigital()
        self.assertIsInstance(instance, MetaDigital)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaDigital()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
