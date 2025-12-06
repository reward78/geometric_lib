import unittest
import math

import square
class TestSquare(unittest.TestCase):
    def _check_square(self, a):
        expected_area = a * a
        expected_perimeter = 4 * a

        self.assertAlmostEqual(square.area(a), expected_area, places=7)
        self.assertAlmostEqual(square.perimeter(a), expected_perimeter, places=7)


_square_sides = [
    0.0,
    0.1,
    0.5,
    1.0,
    1.5,
    2.0,
    3.0,
    4.0,
    5.0,
    10.0,
    12.3,
    15.7,
    20.0,
    25.5,
    30.0,
    33.3,
    40.0,
    50.0,
    75.5,
    100.0,
    123.456,
    256.0,
    512.0,
    999.99,
    1000.0,
]


def _make_square_test(a):
    def test(self):
        self._check_square(a)
    return test


for i, a in enumerate(_square_sides, start=1):
    test_name = f"test_square_case_{i}"
    setattr(TestSquare, test_name, _make_square_test(a))


if __name__ == "__main__":
    unittest.main()