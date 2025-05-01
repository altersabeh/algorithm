from typing import final

from .. import ParameterError


@final
class ZeroParameterError(ParameterError):
    """
    `ZeroValueError`
    ================
    Exception raised when a zero value is encountered where a nonzero value is
    expected.

    Parameters
    ----------
    - `name (str)` The name of the parameter.
    - `value (float)` The invalid (zero) value provided.

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
        super().__init__(name, value, "a nonzero value")
