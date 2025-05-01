from abc import ABC, abstractmethod


class ShapeError(ABC, Exception):
    """
    Base exception class for all shape-related errors.
    """

    @abstractmethod
    def __init__(self, shape: str, dimensions: list[float], reason: str):
        self.shape = shape
        self.dimensions = dimensions
        self.reason = reason
        super().__init__(self.__str__)

    def _format_dimensions(self):
        match self.dimensions:
            case [d]:
                return str(d)
            case [d1, d2]:
                return f"{d1} and {d2}"
            case [*rest, last]:
                return f"{', '.join(map(str, rest))}, and {last}"
            case _:
                return "no dimensions"

    def _message(self):
        shape = self.shape.upper()
        dim_label = "dimension" if len(self.dimensions) == 1 else "dimensions"
        dimensions = self._format_dimensions()
        reason = self.reason
        return f"{shape} with {dim_label} {dimensions} is invalid. {reason}"

    def __str__(self):
        name = self.__class__.__name__
        message = self._message()
        return f"{name}: {message}"
