from typing import final

from .. import ParameterError


@final
class NegativeParameterError(ParameterError):
    """
    NegativeValueError
    ==================
    Exception raised when a negative value is provided for a parameter that
    requires a non-negative value.

    Example
    -------
    ```python
    from algorithm.utils.errors import NegativeParameterError

    name = "length"
    value = -5.0
    err = NegativeParameterError(name, value)

    print(err)  # INVALID LENGTH
    ```
    """

    def __init__(self, name: str, value: float):
        """
        Initializes a new instance of `NegativeParameterError`.

        This constructor accepts a parameter name as a `str` and a value as a
        `float`.

        - **Parameters**
            - **name** The name of the parameter that caused the error.
            - **value** The invalid (negative) value provided.
        """
        super().__init__(name, value, "a non-negative value")
