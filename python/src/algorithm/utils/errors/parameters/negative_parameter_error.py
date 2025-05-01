from typing import final

from .. import ParameterError


@final
class NegativeParameterError(ParameterError):
    """
    `NegativeValueError`
    ====================

    Exception raised when a negative value is provided for a parameter that
    requires a non-negative value.

    Parameters:
        * `name (str)` The name of the parameter.
        * `value (float)` The invalid (negative) value provided.

    Example:

        from algorithm.utils.errors import NegativeParameterError

        name = "length"
        value = -5.0
        err = NegativeParameterError(name, value)

        print(err) # INVALID LENGTH
    """

    def __init__(self, name: str, value: float):
        super().__init__(name, value, "a non-negative value")
