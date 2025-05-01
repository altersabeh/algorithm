from typing import final

from .. import ParameterError


@final
class ZeroParameterError(ParameterError):
    """
    ZeroValueError
    ==============
    Exception raised when a zero value is encountered where a nonzero value is
    expected.

    Example
    -------
    ```python
    from algorithm.utils.errors import ZeroParameterError

    name = "length"
    value = 0.0
    err = ZeroParameterError(name, value)

    print(err)  # INVALID LENGTH
    ```
    """

    def __init__(self, name: str, value: float):
        """
        Initializes a new instance of `ZeroParameterError`.

        This constructor accepts a parameter name as a `str` and a value as a
        `float`.

        - Parameters
            - **name** The name of the parameter that caused the error.
            - **value** The invalid (zero) value provided.
        """
        super().__init__(name, value, "a nonzero value")
