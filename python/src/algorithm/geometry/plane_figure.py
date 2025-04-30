from abc import ABC, abstractmethod


class PlaneFigure(ABC):
    """
    Abstract base class for two-dimensional plane figures.

    This class defines the interface for all flat shapes that lie entirely
    within a single plane. Subclasses must implement methods for computing
    perimeter and area.
    """

    @abstractmethod
    def perimeter(self) -> float:
        """
        Calculate and return the perimeter of the plane figure.
        """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate and return the area of the plane figure.
        """
