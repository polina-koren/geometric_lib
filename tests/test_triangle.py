import unittest
from triangle import area, perimeter


class TestAreaTriangle(unittest.TestCase):

    def test_area_general_triangle(self):
        sides = (5, 7, 9)
        expected_area = (sides[0] + sides[1] + sides[2]) / 2
        result = area(*sides)
        self.assertAlmostEqual(result, expected_area)

    def test_area_right_triangle(self):
        sides = (3, 4, 5)
        expected_area = (sides[0] + sides[1] + sides[2]) / 2
        result = area(*sides)
        self.assertAlmostEqual(result, expected_area)

    def test_area_equilateral_triangle(self):
        sides = (5, 5, 5)
        expected_area = (sides[0] + sides[1] + sides[2]) / 2
        result = area(*sides)
        self.assertAlmostEqual(result, expected_area)

    def test_area_zero_sides_triangle(self):
        sides = (0, 0, 0)
        with self.assertRaises(ValueError):
            area(*sides)

    def test_area_one_sides_triangle(self):
        sides = [(0, 1, 2), (1, 0, 2), (1, 2, 0)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    area(a, b, c)

    def test_area_two_sides_triangle(self):
        sides = [(0, 0, 7), (0, 7, 0), (7, 0, 0)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    area(a, b, c)

    def test_area_negative_sides_triangle(self):
        sides = [(-1, -2, -7), (-1, 2, 3), (1, -1, 2), (1, 2, -3), (-1, -2, 5), (-1, 5, -2), (5, -1, -2)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    area(a, b, c)

    def test_area_non_existent_triangle(self):
        sides = [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    area(a, b, c)


class TestPerimeterTriangle(unittest.TestCase):

    def test_perimeter_general_triangle(self):
        sides = (5, 7, 9)
        expected_perimeter = sides[0] + sides[1] + sides[2]
        result = perimeter(*sides)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_perimeter_right_triangle(self):
        sides = (3, 4, 5)
        expected_perimeter = sides[0] + sides[1] + sides[2]
        result = perimeter(*sides)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_perimeter_equilateral_triangle(self):
        sides = (6, 6, 6)
        expected_perimeter = sides[0] + sides[1] + sides[2]
        result = perimeter(*sides)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_perimeter_zero_sides_triangle(self):
        sides = (0, 0, 0)
        with self.assertRaises(ValueError):
            perimeter(*sides)

    def test_perimeter_one_sides_triangle(self):
        sides = [(0, 1, 2), (1, 0, 2), (1, 2, 0)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    perimeter(a, b, c)

    def test_perimeter_two_sides_triangle(self):
        sides = [(0, 0, 7), (0, 7, 0), (7, 0, 0)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    perimeter(a, b, c)

    def test_perimeter_negative_sides_triangle(self):
        sides = [(-1, -2, -7), (-1, 2, 3), (1, -1, 2), (1, 2, -3), (-1, -2, 5), (-1, 5, -2), (5, -1, -2)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    perimeter(a, b, c)

    def test_perimeter_non_existent_triangle(self):
        sides = [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

        for a, b, c in sides:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    perimeter(a, b, c)


if __name__ == '__main__':
    unittest.main()
