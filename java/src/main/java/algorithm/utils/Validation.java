package algorithm.utils;

import algorithm.utils.errors.parameters.NegativeParameterError;
import algorithm.utils.errors.parameters.ZeroParameterError;

public final class Validation {
    private Validation() {}

    public static void validatePositive(double value, String name) throws Exception {
        if (value < 0.0) {
            throw new NegativeParameterError(name, value);
        } else if (value == 0.0) {
            throw new ZeroParameterError(name, value);
        }
    }
}
