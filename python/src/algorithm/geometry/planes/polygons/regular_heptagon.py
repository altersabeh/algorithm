import math
from typing import final

from algorithm.geometry.planes import Polygon
from algorithm.utils import validation


@final
class RegularHeptagon(Polygon):
    """
    RegularHeptagon
    ===============

    A seven-sided polygon with seven angles summing to 900°. A regular heptagon
    has equal sides and angles, while an irregular one does not.

    Example
    -------
    ```python
    from algorithm.geometry.planes.polygons import RegularHeptagon

    heptagon: RegularHeptagon = RegularHeptagon(5)

    print(f"Heptagon Perimeter: {heptagon.perimeter()}")
    print(f"Heptagon Area: {heptagon.area()}")
    ```
    """

    def __init__(self, side: float):
        validation.validate_positive(side, "side")
        self._side = side

    @property
    def side(self) -> float:
        """
        Returns the length of a side of the heptagon.
        """
        return self._side

    @property
    def apothem(self) -> float:
        """
        Returns the length of the apothem of the heptagon.
        """
        return self.side / (2 * math.tan(math.radians(180 / 7)))

    def perimeter(self) -> float:
        return 7 * self.side

    def area(self) -> float:
        return (self.perimeter() * self.apothem) / 2
