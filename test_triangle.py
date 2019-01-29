import unittest
from math import sqrt
from HW01 import classify_triangle

class HW01Test(unittest.TestCase):
    """test HW01 functions"""
    def test_classify_triangle(self):
        """test if it's a triangle"""
        self.assertEqual(classify_triangle(1, 2, 3), "It's not a triangle.")
        """test if it's a equilateral"""
        self.assertEqual(classify_triangle(5, 5, 5), "It's an equilateral triangle.")
        """test if it's a isosceles and right"""
        self.assertEqual(classify_triangle(1, 1, sqrt(2)), "It's an isosceles and right triangle.")
        """test if it's a isosceles"""
        self.assertEqual(classify_triangle(3, 3, 5), "It's an isosceles triangle.")
        """test if it's a right and scalene"""
        self.assertEqual(classify_triangle(3, 4, 5), "It's a right and scalene triangle.")
        """test if it's a scalene"""
        self.assertEqual(classify_triangle(4, 5, 6), "It's a scalene triangle.")

if __name__ == '__main__':
    print("run the testcase:")
    unittest.main(exit=False)
