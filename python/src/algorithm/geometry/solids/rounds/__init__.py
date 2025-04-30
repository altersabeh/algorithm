"""
curves
======

This module defines geometric types for various three-dimensional curved shapes.

Curved solid figures are three-dimensional shapes with at least one curved edge
or boundary. This module provides representations and utilities for working with
such shapes.
"""

from .cylinder import Cylinder
from .sphere import Sphere

__all__ = ["Cylinder", "Sphere"]
