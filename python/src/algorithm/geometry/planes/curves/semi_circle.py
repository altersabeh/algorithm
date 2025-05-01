import math
from typing import final

from algorithm.geometry.planes import Curve
from algorithm.utils import validation


@final
class SemiCircle(Curve):
    """
    SemiCircle
    ==========
    A half-circle, defined by its radius. It has a curved edge and a straight edge.

    Example
    -------
    ```
    from algorithm.geometry.planes.curves import SemiCircle

    semi_circle: SemiCircle = SemiCircle(5)

    print(f"SemiCircle Perimeter: {semi_circle.perimeter()}")
    print(f"SemiCircle Area: {semi_circle.area()}")
    ```
    """

    def __init__(self, radius: float):
        validation.validate_positive(radius, "radius")
        self._radius = radius

    @property
    def radius(self) -> float:
        """
        Returns the radius of the semi-circle.
        """
        return self._radius

    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the semi-circle.
        """
        return 2 * self.radius

    def perimeter(self) -> float:
        """
        Returns the perimeter of the semi-circle.
        """
        return math.pi * self.radius + self.diameter

    def area(self) -> float:
        """
        Returns the area of the semi-circle.
        """
        return (math.pi * pow(self.radius, 2)) / 2
