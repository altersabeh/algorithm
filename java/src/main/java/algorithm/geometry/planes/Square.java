package algorithm.geometry.planes;

import algorithm.geometry.Plane;
import algorithm.utils.Validation;

public final class Square implements Plane {
    private final double side;

    public Square(double side) throws Exception {
        Validation.validatePositive(side, "side");
        this.side = side;
    }

    public double getSide() {
        return side;
    }

    @Override
    public double perimeter() {
        return 4 * side;
    }

    @Override
    public double area() {
        return Math.pow(side, 2);
    }

}
