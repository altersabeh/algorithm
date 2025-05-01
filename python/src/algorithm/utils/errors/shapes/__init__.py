"""
# angles

This module contains types for handling specific error cases related to
geometric shapes.
"""

from .invalid_trapezoid_error import InvalidTrapezoidError
from .invalid_triangle_error import InvalidTriangleError

__all__ = ["InvalidTriangleError", "InvalidTrapezoidError"]
