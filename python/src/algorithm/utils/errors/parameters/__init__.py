"""
# parameters

This module contains types for handling specific error cases related to
parameter.
"""

from .negative_parameter_error import NegativeParameterError
from .zero_parameter_error import ZeroParameterError

__all__ = ["NegativeParameterError", "ZeroParameterError"]
