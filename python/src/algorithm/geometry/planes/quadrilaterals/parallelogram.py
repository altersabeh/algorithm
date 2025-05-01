import math
from typing import final

from algorithm.geometry import PlaneFigure
from algorithm.utils import validation


@final
class Parallelogram(PlaneFigure):
    """
    Parallelogram
    =============

    A quadrilateral with opposite sides parallel and equal in length. The
    opposite angles are also equal, and the adjacent angles are supplementary.
    The diagonals bisect each other but are not necessarily equal in length.

    Example
    -------
    ```python
    from algorithm.geometry.planes.quadrilaterals import Parallelogram

    parallelogram: Parallelogram = Parallelogram(3, 4, 60)

    print(f"Parallelogram Perimeter: {parallelogram.perimeter()}")
    print(f"Parallelogram Area: {parallelogram.area()}")
    ```
    """

    def __init__(self, base: float, height: float, angle: float):
        validation.validate_positive(base, "base")
        validation.validate_positive(height, "height")
        validation.validate_acute_angle(angle, "angle")
        self._base = base
        self._height = height
        self._angle = angle

    @property
    def base(self) -> float:
        """
        Returns the base length of the parallelogram.
        """
        return self._base

    @property
    def height(self) -> float:
        """
        Returns the height of the parallelogram.
        """
        return self._height

    @property
    def angle(self) -> float:
        """
        Returns the angle of the parallelogram.
        """
        return self._angle

    @property
    def side(self) -> float:
        """
        Returns the length of the side of the parallelogram.
        """
        return self.height / math.sin(math.radians(self.angle))

    def perimeter(self) -> float:
        """
        Returns the perimeter of the parallelogram.
        """
        return 2 * (self.base + self.side)

    def area(self) -> float:
        """
        Returns the area of the parallelogram.
        """
        return self.base * self.height
