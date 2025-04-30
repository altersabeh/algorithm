"""
quadrilaterals
==============

This module defines geometric types for various four-sided polygons.

Quadrilaterals are shapes with four sides and four angles. They may have
properties such as parallel sides, equal angles, or equal side lengths. This
module provides representations and utilities for working with such shapes.
"""

from .rectangle import Rectangle
from .square import Square

__all__ = ["Rectangle", "Square"]
