class AcuteAngleError(ValueError):
    """
    `AcuteAngleError`
    =================

    Exception raised when the provided angle is not acute.

    Parameters:
        name (str): The name of the entity that has the angle.
        value (float): The value of the angle that was provided.

    Example:
    >>> from algorithm.utils.errors import AcuteAngleError
    >>> raise AcuteAngleError("angle", 95)  # Invalid acute angle
    """

    def __init__(self, name: str, value: float):
        super().__init__(self.__str__())
        self.name = name
        self.value = value

    def __str__(self):
        error_name = self.__class__.__name__
        # pylint: disable=consider-using-f-string
        message = ("{}: {} must be an acute angle (between 0 and 90 degrees), got '{}'.").format(
            error_name,
            self.name.upper(),
            self.value,
        )

        return message
