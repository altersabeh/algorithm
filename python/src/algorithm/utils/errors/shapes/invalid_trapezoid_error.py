from typing import final

from .. import ShapeError


@final
class InvalidTrapezoidError(ShapeError):
    """
    `InvalidTrapezoidError`
    =======================
    Exception raised when the provided bases cannot form a valid trapezoid.

    Parameters
    ----------
    - `base_a (float)` The length of the first base.
    - `base_b (float)` The length of the second base.

    Example
    -------
    ```python
    from algorithm.utils.errors import InvalidTrapezoidError

    base_a = 2.0
    base_b = 2.0
    err = InvalidTrapezoidError(base_a, base_b)

    print(err)  # INVALID TRAPEZOID
    ```

    Note
    ----
    This error is raised when the two bases are equal, which does not form a
    trapezoid.
    """

    def __init__(self, base_a: float, base_b: float):
        super().__init__("Trapezoid", [base_a, base_b], "Bases do not form a trapezoid")
