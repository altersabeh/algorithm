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
        self.message = f"{self.shape} with dimensions {self.dimensions} is invalid. {self.reason}"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"
