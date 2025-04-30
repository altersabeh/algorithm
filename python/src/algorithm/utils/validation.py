"""
Utility functions for validating parameter values.
"""

from .errors import ImpossibleTriangleError, NegativeValueError, ZeroValueError


def validate_positive(value: float, name: str):
    """
    Validates that the given value is positive.

    Raises `NegativeValueError` if the value is negative and `ZeroValueError` if the
    value is zero.
    """
    match value:
        case v if v < 0.0:
            raise NegativeValueError(name, value)
        case 0.0:
            raise ZeroValueError(name, value)
        case _:
            return


def validate_triangle(side_a: float, side_b: float, side_c: float):
    """
    Validates that the given side lengths can form a triangle.

    Raises `ImpossibleTriangleError` if the triangle inequality is not satisfied.
    """
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        raise ImpossibleTriangleError(side_a, side_b, side_c)
