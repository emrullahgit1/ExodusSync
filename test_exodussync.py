# test_exodussync.py
"""
Tests for ExodusSync module.
"""

import unittest
from exodussync import ExodusSync

class TestExodusSync(unittest.TestCase):
    """Test cases for ExodusSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ExodusSync()
        self.assertIsInstance(instance, ExodusSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ExodusSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
