from typing import final

from .. import ShapeError


@final
class InvalidTriangleError(ShapeError):
    """
    `InvalidTriangleError`
    =========================

    Exception raised when the provided side lengths cannot form a valid triangle.

    Parameters:
        * `side_a (float)` The length of the first side.
        * `side_b (float)` The length of the second side.
        * `side_c (float)` The length of the third side.

    Example:

        from algorithm.utils.errors import InvalidTriangleError

        side_a = 3.0
        side_b = 4.0
        side_c = 10.0
        err = InvalidTriangleError(side_a, side_b, side_c)

        print(err) # INVALID TRIANGLE
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__(
            "Triangle",
            [side_a, side_b, side_c],
            "Side lengths do not form a triangle",
        )
