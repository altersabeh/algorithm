class InvalidTrapezoidError(Exception):
    """
    `InvalidTrapezoidError`
    ==========================

    Exception raised when the provided bases cannot form a valid trapezoid.

    Attributes:
        base_a (float): Length of base a.
        base_b (float): Length of base b.

    Example:
    >>> from algorithm.utils.errors import InvalidTrapezoidError
    >>> raise InvalidTrapezoidError(2, 2)  # Invalid trapezoid
    """

    def __init__(self, base_a: float, base_b: float):
        self.base_a = base_a
        self.base_b = base_b
        super().__init__(self.__str__())

    def __str__(self):
        error_name = self.__class__.__name__
        # pylint: disable=consider-using-f-string
        message = "{}: The bases {}, {} do not satisfy the trapezoid inequality.".format(
            error_name,
            self.base_a,
            self.base_b,
        )
        return message
