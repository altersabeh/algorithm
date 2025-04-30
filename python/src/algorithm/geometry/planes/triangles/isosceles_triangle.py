from typing import final

from algorithm.geometry.planes import Triangle
from algorithm.utils import validation


@final
class IsoscelesTriangle(Triangle):
    """
    IsoscelesTriangle
    =================

    A triangle with two equal sides and two equal angles. The base angles are
    equal, and the altitude from the vertex angle bisects the base.

    Example
    -------
    ```python
    from algorithm.geometry.planes.triangles import IsoscelesTriangle

    triangle: IsoscelesTriangle = IsoscelesTriangle(5, 7)

    print(f"Triangle Base: {triangle.base}")
    print(f"Triangle Height: {triangle.height}")
    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")
    ```
    """

    def __init__(self, base: float, height: float):
        validation.validate_positive(base, "base")
        validation.validate_positive(height, "height")
        self._base = base
        self._height = height

    @property
    def base(self) -> float:
        """
        Returns the base of the isosceles triangle.
        """
        return self._base

    @property
    def height(self) -> float:
        """
        Returns the height of the isosceles triangle.
        """
        return self._height

    @property
    def side(self) -> float:
        """
        Returns the length of the equal sides of the isosceles triangle.
        """
        return pow(pow(self.base / 2, 2) + pow(self.height, 2), 0.5)

    def perimeter(self) -> float:
        """
        Returns the perimeter of the isosceles triangle.
        """
        return 2 * self.side + self.height

    def area(self) -> float:
        """
        Returns the area of the isosceles triangle.
        """
        return (self.base * self.height) / 2
