import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularNonagon(Polygon):
    """
    RegularNonagon
    ==============

    A nine-sided polygon with nine angles summing to 1260°. A regular nonagon
    has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularNonagon

    nonagon: RegularNonagon = RegularNonagon(5)

    print(f"Nonagon Side: {nonagon.side}")
    print(f"Nonagon Apothem: {nonagon.apothem}")
    print(f"Nonagon Perimeter: {nonagon.perimeter()}")
    print(f"Nonagon Area: {nonagon.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of a side of the nonagon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the nonagon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 9)))

    def perimeter(self) -> float:
        return 9 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
