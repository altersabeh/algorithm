import math
from typing import final

from algorithm.geometry.solids import Round
from algorithm.utils import validation


@final
class Cylinder(Round):
    """
    Cylinder
    ========

    A tube-shaped solid with two parallel circular bases and one curved lateral
    surface. Examples include soda cans and pipes.

    Example
    -------
    ```
    cylinder = Cylinder(radius=5, height=10)
    print(cylinder.volume())
    ```
    """

    def __init__(self, radius: float, height: float):
        validation.validate_positive(radius, "radius")
        validation.validate_positive(height, "height")
        self._radius = radius
        self._height = height

    @property
    def radius(self) -> float:
        """
        Returns the radius of the cylinder.
        """
        return self._radius

    @property
    def height(self) -> float:
        """
        Returns the height of the cylinder.
        """
        return self._height

    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the cylinder.
        """
        return self._radius * 2

    def surface_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self) -> float:
        return math.pi * pow(self.radius, 2) * self.height
