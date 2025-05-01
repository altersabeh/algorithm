import math
from typing import final

from algorithm.geometry.planes import Curve
from algorithm.utils import validation


@final
class Ellipse(Curve):
    """
    Ellipse
    =======

    An elongated circle, defined by two axes: the major axis (longest diameter)
    and the minor axis (shortest diameter). It has two foci and is symmetric
    about both axes.

    Example
    -------
    ```
    from algorithm.geometry.planes.curves import Ellipse

    ellipse: Ellipse = Ellipse(5, 3)

    print(f"Ellipse Perimeter: {ellipse.perimeter()}")
    print(f"Ellipse Area: {ellipse.area()}")
    ```
    """

    def __init__(self, major_axis: float, minor_axis: float):
        validation.validate_positive(major_axis, "major_axis")
        validation.validate_positive(minor_axis, "minor_axis")
        self._major_axis = major_axis
        self._minor_axis = minor_axis

    @property
    def major_axis(self) -> float:
        """
        Returns the length of the major axis of the ellipse.
        """
        return self._major_axis

    @property
    def minor_axis(self) -> float:
        """
        Returns the length of the minor axis of the ellipse.
        """
        return self._minor_axis

    def perimeter(self) -> float:
        """
        Returns the approximate perimeter of the ellipse using Ramanujan's formula.
        """
        semi_major_axis = self.major_axis / 2
        semi_minor_axis = self.minor_axis / 2
        return math.pi * (
            3 * (semi_major_axis + semi_minor_axis)
            - math.sqrt(
                (3 * semi_major_axis + semi_minor_axis) * (semi_major_axis + 3 * semi_minor_axis)
            )
        )

    def area(self) -> float:
        """
        Returns the area of the ellipse.
        """
        return math.pi * (self.major_axis / 2) * (self.minor_axis / 2)
