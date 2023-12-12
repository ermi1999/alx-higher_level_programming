#!/usr/bin/python3
"""
This program handles the test cases for Base module.
"""
import unittest
from models.base import Base


class IdInitialization(unittest.TestCase):
    """
    This class handles the test cases for Base module.
    """
    def test_without_id(self):
        """
        This function test the result without id.
        """
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_with_id(self):
        """
        This function test the result with id provided.
        """
        b = Base(25)
        self.assertEqual(b.id, 25)
        b1 = Base(10)
        self.assertEqual(b1.id, 10)


if __name__ == "__main__":
    unittest.main()
