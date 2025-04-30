from abc import ABC, abstractmethod


class SolidFigure(ABC):
    """
    Abstract base class for three-dimensional solid figures.

    This class defines the interface for all shapes that occupy space in three
    dimensions. Subclasses must implement methods for computing surface area and
    volume.
    """

    @abstractmethod
    def surface_area(self) -> float:
        """
        Calculate and return the surface area of the solid figure.
        """

    @abstractmethod
    def volume(self) -> float:
        """
        Calculate and return the volume of the solid figure.
        """
