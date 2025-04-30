from typing import final

from algorithm.geometry.planes import Triangle
from algorithm.utils import validation


@final
class ScaleneTriangle(Triangle):
    """
    ScaleneTriangle
    ===============

    A triangle with all sides of different lengths and all angles of different
    measures. It has no lines of symmetry and no equal sides or angles.

    Example
    -------
    ```python
    from algorithm.geometry.planes.triangles import ScaleneTriangle

    triangle: ScaleneTriangle = ScaleneTriangle(3, 4, 5)

    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")
    ```
    """

    def __init__(self, side_one: float, side_b: float, side_c: float):
        validation.validate_positive(side_one, "side_a")
        validation.validate_positive(side_b, "side_b")
        validation.validate_positive(side_c, "side_c")
        validation.validate_triangle(side_one, side_b, side_c)
        self._side_a = side_one
        self._side_b = side_b
        self._side_c = side_c

    @property
    def side_a(self) -> float:
        """
        Returns the length of side A of the triangle.
        """
        return self._side_a

    @property
    def side_b(self) -> float:
        """
        Returns the length of side B of the triangle.
        """
        return self._side_b

    @property
    def side_c(self) -> float:
        """
        Returns the length of side C of the triangle.
        """
        return self._side_c

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c

    def area(self) -> float:
        s = self.perimeter() / 2
        return pow(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c), 0.5)
