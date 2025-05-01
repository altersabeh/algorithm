"""
# values

This module contains types for handling specific error cases related to
parameter values.
"""

from .negative_parameter_error import NegativeValueError
from .zero_parameter_error import ZeroValueError

__all__ = ["NegativeValueError", "ZeroValueError"]
