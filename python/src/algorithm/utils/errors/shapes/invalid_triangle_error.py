class InvalidTriangleError(Exception):
    """
    `InvalidTriangleError`
    =========================

    Exception raised when the provided side lengths cannot form a valid triangle.

    Attributes:
        side_a (float): Length of side a.
        side_b (float): Length of side b.
        side_c (float): Length of side c.

    Example:
    >>> from algorithm.utils.errors import InvalidTriangleError
    >>> raise InvalidTriangleError(1, 2, 10)  # Impossible triangle
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        super().__init__(self.__str__())

    def __str__(self):
        error_name = self.__class__.__name__
        # pylint: disable=consider-using-f-string
        message = "{}: The side lengths {}, {}, {} do not satisfy the triangle inequality.".format(
            error_name,
            self.side_a,
            self.side_b,
            self.side_c,
        )
        return message
