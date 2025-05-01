package algorithm.geometry.solids;

import algorithm.geometry.Solid;
import algorithm.utils.Validation;

public final class Sphere implements Solid {
    private double radius;

    public Sphere(double radius) throws Exception {
        Validation.validatePositive(radius, "radius");
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    @Override
    public double volume() {
        return (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);
    }

    @Override
    public double surfaceArea() {
        return 4 * Math.PI * Math.pow(radius, 2);
    }
}
