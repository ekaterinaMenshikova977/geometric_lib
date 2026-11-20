import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2)
        self.assertAlmostEqual(res, 4 * math.pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 6 * math.pi)


if __name__ == '__main__':
    unittest.main()
