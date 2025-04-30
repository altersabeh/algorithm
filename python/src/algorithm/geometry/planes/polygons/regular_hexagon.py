import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularHexagon(Polygon):
    """
    RegularHexagon
    ==============

    A six-sided polygon with six angles summing to 720°. A regular hexagon
    has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularHexagon

    hexagon: RegularHexagon = RegularHexagon(5)

    print(f"Hexagon Side: {hexagon.side}")
    print(f"Hexagon Apothem: {hexagon.apothem}")
    print(f"Hexagon Perimeter: {hexagon.perimeter()}")
    print(f"Hexagon Area: {hexagon.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of the side of the hexagon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the hexagon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 6)))

    def perimeter(self) -> float:
        return 6 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
