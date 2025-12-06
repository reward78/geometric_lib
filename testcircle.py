import unittest
import math

import circle


class TestCircle(unittest.TestCase):
    def _check_circle(self, r):
        expected_area = math.pi * r * r
        expected_perimeter = 2 * math.pi * r

        self.assertAlmostEqual(circle.area(r), expected_area, places=7)
        self.assertAlmostEqual(circle.perimeter(r), expected_perimeter, places=7)


_circle_radii = [
    0.0,
    0.1,
    0.5,
    1.0,
    1.5,
    2.0,
    3.0,
    4.2,
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


def _make_circle_test(r):
    def test(self):
        self._check_circle(r)
    return test


for i, r in enumerate(_circle_radii, start=1):
    test_name = f"test_circle_case_{i}"
    setattr(TestCircle, test_name, _make_circle_test(r))


if __name__ == "__main__":
    unittest.main()