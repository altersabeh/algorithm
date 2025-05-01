package algorithm.tests.fixtures;

public class Helper {
    public static <T> String errorMessage(T actual, T expected) {
        return String.format("Expected: %s, but got: %s", expected, actual);
    }
}
