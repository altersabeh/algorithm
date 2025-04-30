"""
polygon
=======

This module defines geometric types for multi-sided polygons.

Polygons are closed, two-dimensional shapes formed by straight line segments.
They can have three or more sides and may be regular (equal sides and angles)
or irregular. This module provides representations and utilities for working
with such shapes.
"""

from .regular_decagon import RegularDecagon
from .regular_heptagon import RegularHeptagon
from .regular_hexagon import RegularHexagon
from .regular_nonagon import RegularNonagon
from .regular_octagon import RegularOctagon
from .regular_pentagon import RegularPentagon
from .regular_tetragon import RegularTetragon
from .regular_trigon import RegularTrigon

__all__ = [
    "RegularDecagon",
    "RegularHeptagon",
    "RegularHexagon",
    "RegularNonagon",
    "RegularOctagon",
    "RegularPentagon",
    "RegularTetragon",
    "RegularTrigon",
]
