from abc import ABC, abstractmethod


class ParameterError(ABC, Exception):
    """
    Base exception class for all parameter-related errors.
    """

    @abstractmethod
    def __init__(self, name: str, value: float, required: str):
        self.name = name
        self.value = value
        self.required = required
        super().__init__(self.__str__)

    def __str__(self):
        name = self.__class__.__name__
        message = self._message()
        return f"{name}: {message}"

    def _message(self):
        name = self.name.upper()
        return f"{name} is {self.value}, but it must be {self.required}."
