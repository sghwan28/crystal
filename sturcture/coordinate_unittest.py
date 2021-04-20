import unittest
from coordinate import Coordinate


class TestCoordinateMethod(unittest.TestCase):

    def test_addition(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(4, 5, 6)
        a.add(Coordinate(3, 3, 3))
        self.assertEqual(a, b)

    def test_add(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(4, 5, 6)
        c = Coordinate(3, 3, 3)
        self.assertEqual(a+c, b)

    def test_dot_product(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(4, 5, 6)
        self.assertEqual(a.dot(b), 32)

    def test_get_coordinate(self):
        a = Coordinate(1, 2, 3)
        self.assertEqual(a.get_coordinate(), (1, 2, 3))


if __name__ == '__main__':
    unittest.main()
