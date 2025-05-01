package algorithm.tests.utils;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import algorithm.tests.fixtures.Helper;
import algorithm.utils.errors.parameters.NegativeParameterError;
import algorithm.utils.errors.parameters.ZeroParameterError;

@DisplayName("Errors Test Suite")
public class ErrorsTest {
    @Test
    @DisplayName("Negative Value Error Test")
    void negativeValuError_returnsCorrectMessage() {
        String name = "dimension";
        double value = -2.0;

        NegativeParameterError negative = new NegativeParameterError(name, value);

        String actual = negative.toString();
        String expected = "NegativeParameterError: DIMENSION is -2.0, but it must be a non-negative value.";

        assertEquals(expected, actual, Helper.errorMessage(actual, expected));
    }

    @Test
    @DisplayName("Zero Value Error Test")
    void zeroValueError_returnsCorrectMessage() {
        String name = "dimension";
        double value = 0.0;

        ZeroParameterError zero = new ZeroParameterError(name, value);

        String actual = zero.toString();
        String expected = "ZeroParameterError: DIMENSION is 0.0, but it must be a nonzero value.";

        assertEquals(expected, actual, Helper.errorMessage(actual, expected));
    }
}
