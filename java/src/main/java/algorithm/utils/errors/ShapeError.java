package algorithm.utils.errors;

import java.util.List;

/**
 * Abstract class for all shape-related errors.
 */
public class ShapeError extends Exception {
    protected final String shape;
    protected final List<Double> dimensions;
    protected final String reason;

    public ShapeError(String shape, List<Double> dimensions, String reason) {
        this.shape = shape;
        this.dimensions = dimensions;
        this.reason = reason;
    }

    @Override
    public String toString() {
        String name = this.getClass().getSimpleName();
        String message = getMessage();
        return String.format("%s: %s", name, message);
    }

    @Override
    public String getMessage() {
        String shape = this.shape.toUpperCase();
        String dimLabel = dimensions.size() == 1 ? "dimension" : "dimensions";
        String dimensions = formatDimensions();
        String reason = this.reason;
        return String.format("%s with %s %s is invalid. %s", shape, dimLabel, dimensions, reason);
    }

    private String formatDimensions() {
        if (dimensions == null || dimensions.isEmpty()) {
            return "no dimensions";
        }
        switch (dimensions.size()) {
            case 1:
                return String.valueOf(dimensions.get(0));
            case 2:
                return String.format("%s and %s", dimensions.get(0), dimensions.get(1));
            default:
                Double last = dimensions.get(dimensions.size() - 1);
                String restStr = dimensions.subList(0, dimensions.size() - 1)
                    .stream()
                    .map(String::valueOf)
                    .reduce((a, b) -> a + ", " + b)
                    .orElse("");
                return String.format("%s, and %s", restStr, last);
        }
    }
}
