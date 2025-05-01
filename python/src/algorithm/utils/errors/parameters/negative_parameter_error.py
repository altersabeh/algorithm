from typing import final

from .. import ParameterError


@final
class NegativeParameterError(ParameterError):
    """
    `NegativeValueError`
    ====================

    Exception raised when a negative value is encountered where a positive value
    is expected.

    Parameters:
        name (str): The name of the parameter or variable that caused the error.
        value (float): The invalid (negative) value provided.

    Example:
    >>> from algorithm.utils.errors import NegativeValueError
    >>> raise NegativeValueError("length", -5)  # Invalid length
    """

    def __init__(self, name: str, value: float):
        super().__init__(name, value, "a positive value")
