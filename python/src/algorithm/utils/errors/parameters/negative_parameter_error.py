class NegativeValueError(Exception):
    """
    `NegativeValueError`
    ====================

    Exception raised when a negative value is encountered where a positive value
    is expected.

    Attributes:
        name (str): The name of the parameter or variable that caused the error.
        value (float): The invalid (negative) value provided.

    Example:
    >>> from algorithm.utils.errors import NegativeValueError
    >>> raise NegativeValueError("length", -5)  # Invalid length
    """

    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value
        super().__init__(self.__str__())

    def __str__(self):
        error_name = self.__class__.__name__
        # pylint: disable=consider-using-f-string
        message = (
            "{}: Invalid value for '{}'. Received '{}', but '{}' must be a positive value."
        ).format(
            error_name,
            self.name.upper(),
            self.value,
            self.name.upper(),
        )

        return message
