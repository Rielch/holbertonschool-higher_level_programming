#!/usr/bin/python3
"""Unittest for 6-max_integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    """Test suit for max_integer function"""

    def testEmpty(self):
        """Test emply list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())
        self.assertRaises(TypeError, max_integer, None)

    def testTrue(self):
        """test possible cases"""
        self.assertEqual(max_integer([1, 3, 2, 1]), 3)
        self.assertEqual(max_integer([-200, 14.5, 20]), 20)
        self.assertEqual(max_integer([-200, -300]), -200)
        self.assertEqual(max_integer("hello world"), "w")
        self.assertEqual(max_integer([3]), 3)

    def testFalse(self):
        """test imposible cases"""
        self.assertRaises(TypeError, max_integer, [1, 40, 5 + 6j])
        self.assertRaises(TypeError, max_integer, [2, 40, "Hello"])


if __name__ == "__main__":
    unittest.main()
