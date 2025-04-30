"""
# errors

This module contains types for handling specific error cases.
"""

from .impossible_triangle_error import ImpossibleTriangleError
from .negative_value_error import NegativeValueError
from .zero_value_error import ZeroValueError

__all__ = [
    "ImpossibleTriangleError",
    "NegativeValueError",
    "ZeroValueError",
]
