#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for the max integer module.
    """
    def test_empty_list(self):
        """
        This function checks for the return of empty list.
        """
        self.assertIsNone(max_integer())
        
    def test_result_in_list(self):
        """
        this function checks if the return value is in the list.
        """
        my_list = [1, 2, 5, 78, 56, 88]
        self.assertIn(max_integer(my_list), my_list)
    
    def test_negative_numbers(self):
        """
        this function tests for negative values
        """
        my_list = [-1, -100, -200, -8]
        self.assertEqual(max_integer(my_list), -1)

    def test_one_number(self):
        """
        This function tests for only one number.
        """
        self.assertEqual(max_integer([1]), 1)
    
    def test_is_return_value(self):
        """
        This function tests for return value type.
        """
        self.assertIsInstance(max_integer([6, 7, 4]), int)
    
    def test_positive_negative(self):
        """
        This function tests for mixed values.
        """
        self.assertEqual(max_integer([6, 5, 100, -100]), 100)

    def test_positive_numbers(self):
        """
        This function tests positive numbers.
        """
        self.assertEqual(max_integer([100, 2, 99, 200]), 200)

    def test_float_numbers(self):
        """
        This function tests for floating point numbers
        """
        self.assertEqual(max_integer([1, 2, 5, 5.5, 5.51]), 5.51)

    def test_duplicate_numbers(self):
        """
        This function tests for for duplicate numbers. 
        """
        self.assertEqual(max_integer([6, 7, 7,]), 7)


if __name__ == "__main__":
    unittest.main()
