package algorithm.geometry.solids;

import algorithm.geometry.Solid;
import algorithm.utils.Validation;

public final class Cylinder implements Solid {
    private double radius;
    private double height;

    public Cylinder(double radius, double height) throws Exception {
        Validation.validatePositive(radius, "radius");
        Validation.validatePositive(height, "height");
        this.radius = radius;
        this.height = height;
    }

    public double getRadius() {
        return radius;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public double volume() {
        return Math.PI * Math.pow(radius, 2) * height;
    }

    @Override
    public double surfaceArea() {
        return 2 * Math.PI * radius * (radius + height);
    }
}
