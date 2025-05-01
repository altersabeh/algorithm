from typing import final

from .. import ShapeError


@final
class InvalidTriangleError(ShapeError):
    """
    `InvalidTriangleError`
    =========================

    Exception raised when the provided side lengths cannot form a valid triangle.

    Attributes:
        side_a (float): Length of side a.
        side_b (float): Length of side b.
        side_c (float): Length of side c.

    Example:
    >>> from algorithm.utils.errors import InvalidTriangleError
    >>> raise InvalidTriangleError(1, 2, 10)  # Impossible triangle
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__(
            "Triangle",
            [side_a, side_b, side_c],
            "Side lengths do not form a triangle.",
        )
