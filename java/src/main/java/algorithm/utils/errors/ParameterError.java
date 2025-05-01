package algorithm.utils.errors;

/**
 * Abstract class for all parameter-related errors.
 */
public abstract class ParameterError extends Exception {
    protected final String name;
    protected final double value;
    protected final String required;

    public ParameterError(String name, double value, String required) {
        this.name = name;
        this.value = value;
        this.required = required;
    }

    @Override
    public String toString() {
        String name = this.getClass().getSimpleName();
        String message = getMessage();
        return String.format("%s: %s", name, message);
    }

    @Override
    public String getMessage() {
        String name = this.name.toUpperCase();
        return String.format("%s is %s, but it must be %s.", name, this.value, this.required);
    }
}
