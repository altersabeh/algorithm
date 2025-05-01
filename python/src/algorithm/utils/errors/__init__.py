"""
# errors

This module contains types for handling specific error cases.
"""

from .acute_angle_error import AcuteAngleError
from .impossible_triangle_error import ImpossibleTriangleError
from .negative_value_error import NegativeValueError
from .zero_value_error import ZeroValueError

__all__ = [
    "AcuteAngleError",
    "ImpossibleTriangleError",
    "NegativeValueError",
    "ZeroValueError",
]
