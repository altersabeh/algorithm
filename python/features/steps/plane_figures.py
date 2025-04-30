from typing import TypeVar

from behave import given, then, when

from algorithm.geometry.planes.curves import Circle
from algorithm.geometry.planes.quadrilaterals import Rectangle, Square

T = TypeVar("T")


# region CIRCLE STEPS
@given("a circle radius of {radius:f}")
def step_given_circle_radius(test_plane, radius):
    test_plane.circle_radius = radius


@when("the circle is created")
def step_when_circle_created(test_plane):
    test_plane.circle = Circle(test_plane.circle_radius)


@then("the circle's radius should be {expected:f}")
def step_then_circle_radius(test_plane, expected):
    actual = test_plane.circle.radius
    assert actual == expected, _generate_error_report(actual, expected)


# endregion


# region RECTANGLE STEPS
@given("a rectangle width of {width:f}")
def step_given_rectangle_width(test_plane, width):
    test_plane.rectangle_width = width


@given("a rectangle height of {height:f}")
def step_given_rectangle_height(test_plane, height):
    test_plane.rectangle_height = height


@when("the rectangle is created")
def step_when_rectangle_created(test_plane):
    test_plane.rectangle = Rectangle(test_plane.rectangle_width, test_plane.rectangle_height)


@then("the rectangle's width should be {expected:f}")
def step_then_rectangle_width(test_plane, expected):
    actual = test_plane.rectangle.width
    assert actual == expected, _generate_error_report(actual, expected)


@then("the rectangle's height should be {expected:f}")
def step_then_rectangle_height(test_plane, expected):
    actual = test_plane.rectangle.height
    assert actual == expected, _generate_error_report(actual, expected)


# endregion


# region SQUARE STEPS
@given("a square side length of {side:f}")
def step_given_square_side(test_plane, side):
    test_plane.square_side = side


@when("the square is created")
def step_when_square_created(test_plane):
    test_plane.square = Square(test_plane.square_side)


@then("the square's side length should be {expected:f}")
def step_then_square_side(test_plane, expected):
    actual = test_plane.square.side
    assert actual == expected, _generate_error_report(actual, expected)


# endregion


def _generate_error_report(actual: T, expected: T) -> str:
    return f"Actual: {actual}\nExpected: {expected}"
