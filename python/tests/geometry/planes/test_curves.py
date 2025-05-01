import math

import pytest
from fixtures import helper

from algorithm.geometry.planes.curves import Circle
from algorithm.utils.errors.parameters import NegativeValueError, ZeroValueError


class TestCircle:
    def test_circle_new_negative_or_zero_radius_returns_error(self):
        with pytest.raises(NegativeValueError):
            Circle(-1.0)
        with pytest.raises(ZeroValueError):
            Circle(0.0)

    def test_circle_radius_returns_correct_value(self):
        circle = Circle(3.0)
        actual = circle.radius
        expected = 3.0
        assert actual == expected, helper.error_message(actual, expected)

    def test_circle_area_returns_correct_value(self):
        circle = Circle(3.0)
        expected = math.pi * 3.0**2
        actual = circle.area()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)

    def test_circle_perimeter_returns_correct_value(self):
        circle = Circle(3.0)
        expected = 2 * math.pi * 3.0
        actual = circle.perimeter()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)
