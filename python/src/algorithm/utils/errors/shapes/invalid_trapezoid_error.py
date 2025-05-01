from typing import final

from .. import ShapeError


@final
class InvalidTrapezoidError(ShapeError):
    """
    `InvalidTrapezoidError`
    ==========================

    Exception raised when the provided bases cannot form a valid trapezoid.

    Parameters:
        base_a (float): Length of base a.
        base_b (float): Length of base b.

    Example:
    >>> from algorithm.utils.errors import InvalidTrapezoidError
    >>> raise InvalidTrapezoidError(2, 2)  # Invalid trapezoid
    """

    def __init__(self, base_a: float, base_b: float):
        super().__init__("Trapezoid", [base_a, base_b], "Bases do not form a trapezoid")
