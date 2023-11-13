#!/usr/bin/python3
"""
This program handles the test cases for rectangle module
"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """
    This class handles the test cases for rectangle module
    """
    def test_with_id(self):
        """
        This function tests the module with id.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)

    def test_without_argument(self):
        """
        This function tests the module without arguments.
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_area(self):
        """
        This function tests the area method in rectagle module.
        """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r1 = Rectangle(3, 10, 0, 0, 10)
        self.assertEqual(r1.area(), 30)

    def test_not_int(self):
        """
        This function tests the module by passing a non int value.
        """
        with self.assertRaises(TypeError):
            Rectangle(2, "8")
            Rectangle("8", 2)
            Rectangle(2, 3, "7")
            Rectangle(5, 4, 3, "2")

    def test_negative_int(self):
        """
        This function tests the module by passing a negative value.
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2,)
            Rectangle(2, -1)
            Rectangle(5, 2, -1)
            Rectangle(5, 4, 3, -2)

    def test_create(self):
        """
        this function tests the create method with dictionary.
        """
        r = Rectangle(4, 2, 2, 1, 77)
        rdict = r.to_dictionary()
        r1 = Rectangle.create(**rdict)
        self.assertNotEqual(r, r1)

    def test_type(self):
        """
        this function tests the return type.
        """
        r = Rectangle(12, 12, 12, 6, 56)
        rdict = r.to_dictionary()
        self.assertIsInstance(rdict, dict)

    def test_update(self):
        """
        This function tests the method update in rectangle module with kwargs.
        """
        r = Rectangle(1, 1, 1, 1)
        r.update(width=2)
        self.assertEqual(r.width, 2)
        r.update(height=2)
        self.assertEqual(r.height, 2)
        r.update(x=2, y=2, id=2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 2)

    def test_with_dict(self):
        """
        This function tests the kwarg of upadte method with dictionary.
        """
        r = Rectangle(10, 10, 10, 10, 47)
        rdict = r.to_dictionary()
        r1 = Rectangle(20, 20, 20, 20, 49)
        r1.update(**rdict)
        self.assertEqual(r1.id, 47)
        self.assertNotEqual(r, r1)

    def test_update(self):
        """
        This function tests the method update in rectangle module.
        """
        r = Rectangle(4, 5, 8, 5, 77)
        self.assertEqual(r.id, 77)
        r.update(15)
        self.assertEqual(r.id, 15)
        r.update(15, 6)
        self.assertEqual(r.width, 6)
        r.update(15, 6, 2)
        self.assertEqual(r.height, 2)
        r.update(15, 6, 2, 2)
        self.assertEqual(r.x, 2)
        r.update(15, 6, 2, 2, 1)
        self.assertEqual(r.y, 1)


if __name__ == "__main__":
    unittest.main()
