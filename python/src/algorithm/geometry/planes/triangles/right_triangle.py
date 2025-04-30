from typing import final

from algorithm.geometry.planes import Triangle
from algorithm.utils import validation


@final
class RightTriangle(Triangle):
    """
    Right Triangle
    ==============

    A triangle with one angle measuring 90 degrees. The side opposite the right
    angle is called the hypotenuse, and the other two sides are called the legs.
    It follows the Pythagorean theorem.

    Example:
    --------
    ```python
    from algorithm.geometry.planes.triangles import RightTriangle

    right_triangle: RightTriangle = RightTriangle(3, 4)

    print(f"Right Triangle Base: {right_triangle.base}")
    print(f"Right Triangle Height: {right_triangle.height}")
    print(f"Right Triangle Hypotenuse: {right_triangle.hypotenuse}")
    print(f"Right Triangle Perimeter: {right_triangle.perimeter()}")
    print(f"Right Triangle Area: {right_triangle.area()}")
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
        Returns the base of the right triangle.
        """
        return self._base

    @property
    def height(self) -> float:
        """
        Returns the height of the right triangle.
        """
        return self._height

    @property
    def hypotenuse(self) -> float:
        """
        Returns the hypotenuse of the right triangle.
        """
        return pow(pow(self.base, 2) + pow(self.height, 2), 0.5)

    def perimeter(self) -> float:
        return self.base + self.height + self.hypotenuse

    def area(self) -> float:
        return (self.base * self.height) / 2
