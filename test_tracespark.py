# test_tracespark.py
"""
Tests for TraceSpark module.
"""

import unittest
from tracespark import TraceSpark

class TestTraceSpark(unittest.TestCase):
    """Test cases for TraceSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TraceSpark()
        self.assertIsInstance(instance, TraceSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TraceSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
