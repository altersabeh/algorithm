from typing import final

from algorithm.geometry import PlaneFigure
from algorithm.utils import validation


@final
class Square(PlaneFigure):
    """
    Square
    ======

    A regular quadrilateral with four equal sides and four right angles (90°).
    It has four lines of symmetry and equal diagonals that bisect each other.

    Example
    -------
    ```
    from algorithm.geometry.planes.quadrilaterals import Square

    square: Square = Square(5)

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
        Returns the side length of the square.
        """
        return self._side

    @property
    def diagonal(self) -> float:
        """
        Returns the length of the diagonal of the square.
        """
        return pow(2, 0.5) * self.side

    def perimeter(self) -> float:
        return 4 * self.side

    def area(self) -> float:
        return pow(self.side, 2)
