package algorithm.geometry.planes;

import algorithm.geometry.Plane;
import algorithm.utils.Validation;

public final class Circle implements Plane {
    private final double radius;

    public Circle(double radius) throws Exception {
        Validation.validatePositive(radius, "radius");
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }
}
