package algorithm.utils.errors.parameters;

import algorithm.utils.errors.ParameterError;

/**
 * <h1>ZeroParameterError</h1>
 *
 * Exception raised when a zero value is provided for a parameter that requires
 * a nonzero value.
 *
 * <h2>Example</h2>
 *
 * <pre>
 * <code>
 * import algorithm.utils.errors.parameters.ZeroParameterError;
 *
 * var name = "length";
 * var value = 0.0;
 * var err = new ZeroParameterError(name, value);
 *
 * System.out.println(err);  // INVALID LENGTH
 * </code>
 * </pre>
 */
public final class ZeroParameterError extends ParameterError {
    /**
     * Initializes a new instance of <code>ZeroParameterError</code>.
     * <p>
     * This constructor accepts a parameter name as a `str` and a value as a
     * `float`.
     *
     * @param name  The name of the parameter that caused the error.
     * @param value The invalid (zero) value provided.
     */
    public ZeroParameterError(String name, double value) {
        super(name, value, "a nonzero value");
    }
}
