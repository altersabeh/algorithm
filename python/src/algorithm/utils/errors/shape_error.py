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
        dim_label = "dimension" if len(self.dimensions) == 1 else "dimensions"
        return (
            f"{self.shape} with {dim_label} {self._format_dimensions()} is invalid. {self.reason}"
        )

    def __str__(self):
        return f"{self.__class__.__name__}: {self._message()}"
