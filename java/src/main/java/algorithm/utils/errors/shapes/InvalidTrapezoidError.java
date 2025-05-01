package algorithm.utils.errors.shapes;

import java.util.List;

import algorithm.utils.errors.ShapeError;

/**
 * <h1>InvalidTrapezoidError</h1>
 *
 * Exception raised when the provided base lengths cannot form a valid
 * trapezoid.
 *
 * <h2>Example</h2>
 *
 * <pre>
 * <code>
 * import algorithm.utils.errors.shapes.InvalidTrapezoidError;
 *
 * var baseA = 3.0;
 * var baseB = 4.0;
 * var err = new InvalidTrapezoidError(baseA, baseB);
 *
 * System.out.println(err);  // INVALID TRAPEZOID
 * </code>
 * </pre>
 */
public final class InvalidTrapezoidError extends ShapeError {
    /**
     * Initializes a new instance of <code>InvalidTrapezoidError</code>.
     * <p>
     * This constructor accepts two base lengths as `float` values.
     *
     * @param baseA The length of the first base.
     * @param baseB The length of the second base.
     */
    public InvalidTrapezoidError(double baseA, double baseB) {
        super("Trapezoid", List.of(baseA, baseB), "Bases do not form a trapezoid");
    }
}
