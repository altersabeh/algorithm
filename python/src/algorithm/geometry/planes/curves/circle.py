import math
from typing import final

from algorithm.geometry.planes import Curve
from algorithm.utils import validation


@final
class Circle(Curve):
    """
    Circle
    ======

    A perfectly round shape with all points equidistant from the center. It has
    no edges or vertices and infinite lines of symmetry.

    Example
    -------
    ```
    from algorithm.geometry.planes.curves import Circle

    circle: Circle = Circle(5)

    print(f"Circle Radius: {circle.radius}")
    print(f"Circle Diameter: {circle.diameter}")
    print(f"Circle Perimeter: {circle.perimeter()}")
    print(f"Circle Area: {circle.area()}")
    ```
    """

    def __init__(self, radius: float):
        validation.validate_positive(radius, "radius")
        self._radius = radius

    @property
    def radius(self) -> float:
        """
        Returns the radius of the circle.
        """
        return self._radius

    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the circle.
        """
        return 2 * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * pow(self.radius, 2)
