import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularOctagon(Polygon):
    """
    RegularOctagon
    ==============

    An eight-sided polygon with eight angles summing to 1080°. A regular octagon
    has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularOctagon

    octagon: RegularOctagon = RegularOctagon(5)

    print(f"Octagon Perimeter: {octagon.perimeter()}")
    print(f"Octagon Area: {octagon.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of a side of the octagon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the octagon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 8)))

    def perimeter(self) -> float:
        return 8 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
