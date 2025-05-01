"""
# values

This module contains types for handling specific error cases related to
parameter values.
"""

from .negative_parameter_error import NegativeParameterError
from .zero_parameter_error import ZeroParameterError

__all__ = ["NegativeParameterError", "ZeroParameterError"]
