from typing import final

from .. import ParameterError


@final
class ZeroParameterError(ParameterError):
    """
    `ZeroValueError`
    ==================

    Exception raised when a zero value is encountered where a nonzero value is
    expected.

    Parameters:
        name (str): The name of the parameter or variable that caused the error.
        value (float): The invalid (zero) value provided.

    Example:
    >>> from algorithm.utils.errors import ZeroValueError
    >>> raise ZeroValueError("length", 0)  # Invalid length
    """

    def __init__(self, name: str, value: float):
        super().__init__(name, value, "a nonzero value")
