import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularTetragon(Polygon):
    """
    RegularTetragon
    ===============

    A four-sided polygon with four angles summing to 360°. A regular tetragon
    (square) has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularTetragon

    square: RegularTetragon = RegularTetragon(5)

    print(f"Square Side: {square.side}")
    print(f"Square Apothem: {square.apothem}")
    print(f"Square Perimeter: {square.perimeter()}")
    print(f"Square Area: {square.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of a side of the tetragon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the tetragon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 4)))

    def perimeter(self) -> float:
        return 4 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
