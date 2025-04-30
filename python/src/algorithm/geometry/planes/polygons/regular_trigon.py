import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularTrigon(Polygon):
    """
    RegularTrigon
    =============

    A three-sided polygon with three angles summing to 180°. A regular trigon
    (equilateral triangle) has equal sides and angles, while an irregular one
    does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularTrigon

    triangle: RegularTrigon = RegularTrigon(5)

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
        Returns the length of the side of the trigon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the trigon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 3)))

    def perimeter(self) -> float:
        """
        Returns the perimeter of the trigon.
        """
        return 3 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
