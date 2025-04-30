"""
planes
======

This module provides types and utilities for working with two-dimensional plane
shapes.

Plane figures are flat, two-dimensional shapes that lie entirely within a single
plane. They have length and width but no thickness or depth.
"""

from .curve import Curve
from .polygon import Polygon
from .quadrilateral import Quadrilateral
from .triangle import Triangle

__all__ = ["Curve", "Polygon", "Quadrilateral", "Triangle"]
