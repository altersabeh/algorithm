import math

from algorithm.geometry import SolidFigure
from algorithm.utils import validation


class Sphere(SolidFigure):
    """
    Sphere
    ======

    A perfectly round 3D shape where every point on the surface is equidistant
    from the center (e.g., a basketball). It has no edges or vertices.

    Example
    -------
    ```
    from algorithm.geometry.solids.rounds import Sphere

    sphere: Sphere = Sphere(5)

    print(f"Sphere Surface Area: {sphere.surface_area()}")
    print(f"Sphere Volume: {sphere.volume()}")
    ```
    """

    def __init__(self, radius: float):
        validation.validate_positive(radius, "radius")
        self._radius = radius

    @property
    def radius(self) -> float:
        """
        Returns the radius of the sphere.
        """
        return self._radius

    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the sphere.
        """
        return self._radius * 2

    def surface_area(self) -> float:
        return 4 * math.pi * pow(self._radius, 2)

    def volume(self) -> float:
        return (4 / 3) * math.pi * pow(self._radius, 3)
