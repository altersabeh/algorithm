"""
triangles
=========

This module defines geometric types for three-sided polygons.

Triangles are shapes with three sides and three angles. They can vary in side
lengths and angle measures, such as equilateral, isosceles, or scalene
triangles. This module provides representations and utilities for working with
such shapes.
"""

from .equilateral_triangle import EquilateralTriangle
from .isosceles_triangle import IsoscelesTriangle
from .right_triangle import RightTriangle
from .scalene_triangle import ScaleneTriangle

__all__ = ["EquilateralTriangle", "IsoscelesTriangle", "RightTriangle", "ScaleneTriangle"]
