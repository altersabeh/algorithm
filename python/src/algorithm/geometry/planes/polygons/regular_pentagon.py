import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularPentagon(Polygon):
    """
    RegularPentagon
    ===============

    A five-sided polygon with five angles summing to 540°. A regular pentagon
    has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularPentagon

    pentagon: RegularPentagon = RegularPentagon(5)

    print(f"Pentagon Side: {pentagon.side}")
    print(f"Pentagon Apothem: {pentagon.apothem}")
    print(f"Pentagon Perimeter: {pentagon.perimeter()}")
    print(f"Pentagon Area: {pentagon.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of the side of the pentagon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the pentagon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 5)))

    def perimeter(self) -> float:
        return 5 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
