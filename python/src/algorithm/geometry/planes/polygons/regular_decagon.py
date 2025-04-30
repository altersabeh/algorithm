import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularDecagon(Polygon):
    """
    RegularDecagon
    ==============

    A ten-sided polygon with ten angles summing to 1440°. A regular decagon
    has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularDecagon

    decagon: RegularDecagon = RegularDecagon(5)

    print(f"Decagon Side: {decagon.side}")
    print(f"Decagon Apothem: {decagon.apothem}")
    print(f"Decagon Perimeter: {decagon.perimeter()}")
    print(f"Decagon Area: {decagon.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of a side of the decagon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the decagon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 10)))

    def perimeter(self) -> float:
        return 10 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
