from typing import final

from algorithm.geometry import PlaneFigure
from algorithm.utils import validation


@final
class Rectangle(PlaneFigure):
    """
    Rectangle
    ========

    A quadrilateral with four right angles and opposite sides equal and
    parallel. Unlike a square, its adjacent sides are not necessarily equal.

    Example:
    -------
    ```python
    from algorithm.geometry.planes.quadrilaterals import Rectangle

    rectangle: Rectangle = Rectangle(3, 4)

    print(f"Rectangle Perimeter: {rectangle.perimeter()}")
    print(f"Rectangle Area: {rectangle.area()}")
    ```
    """

    def __init__(self, width: float, height: float):
        validation.validate_positive(width, "width")
        validation.validate_positive(height, "height")
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        """
        Returns the width of the rectangle.
        """
        return self._width

    @property
    def height(self) -> float:
        """
        Returns the height of the rectangle.
        """
        return self._height

    @property
    def diagonal(self) -> float:
        """
        Returns the length of the diagonal of the rectangle.
        """
        return pow(pow(self.width, 2) + pow(self.height, 2), 0.5)

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def area(self) -> float:
        return self.width * self.height
