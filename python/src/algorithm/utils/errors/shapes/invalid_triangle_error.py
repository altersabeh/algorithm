from typing import final

from .. import ShapeError


@final
class InvalidTriangleError(ShapeError):
    """
    InvalidTriangleError
    ====================
    Exception raised when the provided side lengths cannot form a valid triangle.

    Example
    -------
    ```python
    from algorithm.utils.errors import InvalidTriangleError

    side_a = 3.0
    side_b = 4.0
    side_c = 10.0
    err = InvalidTriangleError(side_a, side_b, side_c)

    print(err)  # INVALID TRIANGLE
    ```

    Note
    ----
    This error is raised when the sum of the lengths of any two sides is less
    than or equal to the length of the third side.
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Initializes a new instance of `InvalidTriangleError`.

        This constructor accepts three side lengths as `float` values.

        - **Parameters**
            - **side_a** The length of the first side.
            - **side_b** The length of the second side.
            - **side_c** The length of the third side.
        """
        super().__init__(
            "Triangle",
            [side_a, side_b, side_c],
            "Side lengths do not form a triangle",
        )
