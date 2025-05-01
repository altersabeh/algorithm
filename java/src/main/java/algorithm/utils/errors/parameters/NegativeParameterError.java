package algorithm.utils.errors.parameters;

import algorithm.utils.errors.ParameterError;

/**
 * <h1>NegativeParameterError</h1>
 *
 * Exception raised when a negative value is provided for a parameter that
 * requires a non-negative value.
 *
 * <h2>Example</h2>
 *
 * <pre>
 * <code>
 * import algorithm.utils.errors.parameters.NegativeParameterError;
 *
 * var name = "length";
 * var value = -2.0;
 * var err = new NegativeParameterError(name, value);
 *
 * System.out.println(err);  // INVALID LENGTH
 * </code>
 * </pre>
 */
public final class NegativeParameterError extends ParameterError {
    /**
     * Initializes a new instance of <code>NegativeParameterError</code>.
     * <p>
     * This constructor accepts a parameter name as a `str` and a value as a
     * `float`.
     *
     * @param name  The name of the parameter that caused the error.
     * @param value The invalid (negative) value provided.
     */
    public NegativeParameterError(String name, double value) {
        super(name, value, "a non-negative value");
    }
}
