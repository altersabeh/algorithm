import math

import pytest
from fixtures import helper

from algorithm.geometry.planes.quadrilaterals import Rectangle, Square
from algorithm.utils.errors import NegativeValueError, ZeroValueError


class TestSquare:
    def test_square_new_negative_or_zero_side_returns_error(self):
        with pytest.raises(NegativeValueError):
            Square(-1.0)
        with pytest.raises(ZeroValueError):
            Square(0.0)

    def test_square_side_returns_correct_value(self):
        square = Square(3.0)
        actual = square.side
        expected = 3.0
        assert actual == expected, helper.error_message(actual, expected)

    def test_square_area_returns_correct_value(self):
        square = Square(3.0)
        expected = 3.0**2
        actual = square.area()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)

    def test_square_perimeter_returns_correct_value(self):
        square = Square(3.0)
        expected = 4 * 3.0
        actual = square.perimeter()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)


class TestRectangle:
    def test_rectangle_new_negative_or_zero_width_returns_error(self):
        with pytest.raises(NegativeValueError):
            Rectangle(-1.0, 2.0)
        with pytest.raises(ZeroValueError):
            Rectangle(0.0, 2.0)

    def test_rectangle_new_negative_or_zero_height_returns_error(self):
        with pytest.raises(NegativeValueError):
            Rectangle(3.0, -1.0)
        with pytest.raises(ZeroValueError):
            Rectangle(3.0, 0.0)

    def test_rectangle_width_and_height_returns_correct_value(self):
        rectangle = Rectangle(3.0, 4.0)
        actual_width = rectangle.width
        expected_width = 3.0
        assert actual_width == expected_width, helper.error_message(actual_width, expected_width)

        actual_height = rectangle.height
        expected_height = 4.0
        assert actual_height == expected_height, helper.error_message(
            actual_height, expected_height
        )

    def test_rectangle_area_returns_correct_value(self):
        rectangle = Rectangle(3.0, 4.0)
        expected = 3.0 * 4.0
        actual = rectangle.area()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)

    def test_rectangle_perimeter_returns_correct_value(self):
        rectangle = Rectangle(3.0, 4.0)
        expected = 2 * (3.0 + 4.0)
        actual = rectangle.perimeter()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)
