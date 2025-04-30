from typing import final

from algorithm.geometry.planes import Triangle
from algorithm.utils import validation


@final
class EquilateralTriangle(Triangle):
    """
    EquilateralTriangle
    ===================

    A triangle with all three sides of equal length and all three angles of
    equal measure (60 degrees). It is a regular polygon with three sides.

    Example
    -------
    ```python
    from algorithm.geometry.planes.triangles import EquilateralTriangle

    triangle: EquilateralTriangle = EquilateralTriangle(5)

    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of the side of the equilateral triangle.
        """
        return self._side

    def perimeter(self) -> float:
        return 3 * self.side

    def area(self) -> float:
        return (pow(self.side, 2) * pow(3, 0.5)) / 4
