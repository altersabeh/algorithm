package algorithm.geometry.planes;

import algorithm.geometry.Plane;
import algorithm.utils.Validation;

public final class Rectangle implements Plane {
    private final double width;
    private final double height;

    public Rectangle(double width, double height) throws Exception {
        Validation.validatePositive(width, "length");
        Validation.validatePositive(height, "width");
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public double perimeter() {
        return 2 * (width + height);
    }

    @Override
    public double area() {
        return width * height;
    }
}
