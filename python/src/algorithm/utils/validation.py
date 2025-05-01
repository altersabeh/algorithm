"""
Utility functions for validating parameter values.
"""

from .errors.angles import AcuteAngleError
from .errors.parameters import NegativeParameterError, ZeroParameterError
from .errors.shapes import InvalidTrapezoidError, InvalidTriangleError


def validate_acute_angle(value: float, name: str):
    """
    Validates that the given angle is acute (between 0 and 90 degrees).

    Raises `AcuteAngleError` if the angle is not acute.
    """
    match value:
        case v if v <= 0.0 or v >= 90.0:
            raise AcuteAngleError(name, value)
        case _:
            return


def validate_positive(value: float, name: str):
    """
    Validates that the given value is positive.

    Raises `NegativeValueError` if the value is negative and `ZeroValueError` if the
    value is zero.
    """
    match value:
        case v if v < 0.0:
            raise NegativeParameterError(name, value)
        case 0.0:
            raise ZeroParameterError(name, value)
        case _:
            return


def validate_triangle(side_a: float, side_b: float, side_c: float):
    """
    Validates that the given side lengths can form a triangle.

    Raises `ImpossibleTriangleError` if the triangle inequality is not satisfied.
    """
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        raise InvalidTriangleError(side_a, side_b, side_c)


def validate_trapezoid(base_a: float, base_b: float):
    """
    Validates that the given bases can form a trapezoid.

    Raises `InvalidTrapezoidError` if the trapezoid inequality is not satisfied.
    """
    if base_a == base_b:
        raise InvalidTrapezoidError(base_a, base_b)
