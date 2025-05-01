package algorithm.utils.errors.shapes;

import java.util.List;

import algorithm.utils.errors.ShapeError;

/**
 * <h1>InvalidTriangleError</h1>
 *
 * Exception raised when the provided side lengths cannot form a valid triangle.
 *
 * <h2>Example</h2>
 *
 * <pre>
 * <code>
 * import algorithm.utils.errors.shapes.InvalidTriangleError;
 *
 * var sideA = 3.0;
 * var sideB = 4.0;
 * var sideC = 10.0;
 * var err = new InvalidTriangleError(sideA, sideB, sideC);
 *
 * System.out.println(err);  // INVALID TRIANGLE
 * </code>
 * </pre>
 */
public final class InvalidTriangleError extends ShapeError {
    /**
     * Initializes a new instance of <code>InvalidTriangleError</code>.
     * <p>
     * This constructor accepts three side lengths as `float` values.
     *
     * @param sideA The length of the first side.
     * @param sideB The length of the second side.
     * @param sideC The length of the third side.
     */
    public InvalidTriangleError(double sideA, double sideB, double sideC) {
        super("Triangle", List.of(sideA, sideB, sideC), "Side lengths do not form a triangle");
    }
}
