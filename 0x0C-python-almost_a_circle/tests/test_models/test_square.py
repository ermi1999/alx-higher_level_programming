#!/usr/bin/python3
"""
Test for square module.
"""
import unittest
from models.square import Square


class TestSquareModule(unittest.TestCase):
    """
    This class handles the test square module.
    """
    def test_getter_setter(self):
        """
        This function tests the square module getters and setters.
        """
        s = Square(3, 3, 4, 50)
        self.assertEqual(s.size, 3)
        s.size = 8
        self.assertEqual(s.size, 8)
    def test_without_argument(self):
        """
        This function tests the module without argument.
        """
        with self.assertRaises(TypeError):
            Square()

    def test_wrong_type(self):
        """
        This function tests the module by giving the wrong type.
        """
        with self.assertRaises(TypeError):
            s = Square(3, 3, 4, 46)
            s.size = "3"

    def test_type(self):
        """
        This function tests the return type.
        """
        s = Square(12, 12, 6, 57)
        sdict = s.to_dictionary()
        self.assertIsInstance(sdict, dict)

    def test_update_args(self):
        """
        Test for update args.
        """
        s = Square(4, 5, 8, 41)
        s.update(7)
        self.assertEqual(s.id, 7)
        s.update(7, 2, 3, 4)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """
        This class handles the taste case for square update.
        """
        s = Square(6, 7, 8, 42)
        s.update(id=43)
        self.assertEqual(s.id, 43)
        s.update(x=2, y=2, size=3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.size, 3)

    def test_with_dict(self):
        """
        This function tests the kwargs of update with dict.
        """
        s = Square(9, 6, 5, 95)
        s1 = Square(10, 11, 12, 96)
        sdict = s.to_dictionary()
        s1.update(**sdict)
        self.assertEqual(s.id, 95)


if __name__ == "__main__":
    unittest.main()
