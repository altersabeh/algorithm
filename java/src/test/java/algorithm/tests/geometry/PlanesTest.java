package algorithm.tests.geometry;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.function.Executable;

import algorithm.geometry.planes.Circle;
import algorithm.geometry.planes.Rectangle;
import algorithm.geometry.planes.Square;
import algorithm.tests.fixtures.Helper;
import algorithm.utils.errors.parameters.NegativeParameterError;
import algorithm.utils.errors.parameters.ZeroParameterError;

@Nested
@DisplayName("Plane Figures Test Suite")
public class PlanesTest {
    @Nested
    @DisplayName("Circle Test Suite")
    class CircleTest {
        @Test
        @DisplayName("Circle Negative or Zero Radius Test")
        void newCircle_negativeOrZeroRadius_throwsException() {
            Executable negativeCircle = () -> new Circle(-1);
            Executable zeroCircle = () -> new Circle(0);
            assertThrows(NegativeParameterError.class, negativeCircle);
            assertThrows(ZeroParameterError.class, zeroCircle);
        }

        @Test
        @DisplayName("Circle Radius Test")
        void circleRadius_returnsCorrectValue() throws Exception {
            Circle circle = new Circle(3.0);
            double actual = circle.getRadius();
            double expected = 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Circle Area Test")
        void circleArea_returnsCorrectValue() throws Exception {
            Circle circle = new Circle(3.0);
            double actual = circle.area();
            double expected = Math.PI * Math.pow(3.0, 2);
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Circle Perimeter Test")
        void circlePerimeter_returnsCorrectValue() throws Exception {
            Circle circle = new Circle(3.0);
            double actual = circle.perimeter();
            double expected = 2 * Math.PI * 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }
    }

    @Nested
    @DisplayName("Rectangle Test Suite")
    class RectangleTest {
        @Test
        @DisplayName("Rectangle Negative or Zero Length Test")
        void newRectangle_negativeOrZeroLength_throwsException() {
            Executable negativeRectangle = () -> new Rectangle(-1, 2);
            Executable zeroRectangle = () -> new Rectangle(0, 2);
            assertThrows(NegativeParameterError.class, negativeRectangle);
            assertThrows(ZeroParameterError.class, zeroRectangle);
        }

        @Test
        @DisplayName("Rectangle Negative or Zero Width Test")
        void newRectangle_negativeOrZeroWidth_throwsException() {
            Executable negativeRectangle = () -> new Rectangle(1, -2);
            Executable zeroRectangle = () -> new Rectangle(1, 0);
            assertThrows(NegativeParameterError.class, negativeRectangle);
            assertThrows(ZeroParameterError.class, zeroRectangle);
        }

        @Test
        @DisplayName("Rectangle Length Test")
        void rectangleLength_returnsCorrectValue() throws Exception {
            Rectangle rectangle = new Rectangle(3.0, 4.0);
            double actual = rectangle.getWidth();
            double expected = 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Rectangle Width Test")
        void rectangleWidth_returnsCorrectValue() throws Exception {
            Rectangle rectangle = new Rectangle(3.0, 4.0);
            double actual = rectangle.getHeight();
            double expected = 4.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Rectangle Area Test")
        void rectangleArea_returnsCorrectValue() throws Exception {
            Rectangle rectangle = new Rectangle(3.0, 4.0);
            double actual = rectangle.area();
            double expected = 3.0 * 4.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Rectangle Perimeter Test")
        void rectanglePerimeter_returnsCorrectValue() throws Exception {
            Rectangle rectangle = new Rectangle(3.0, 4.0);
            double actual = rectangle.perimeter();
            double expected = 2 * (3.0 + 4.0);
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }
    }

    @Nested
    @DisplayName("Square Test Suite")
    class SquareTest {
        @Test
        @DisplayName("Square Negative or Zero Side Test")
        void newSquare_negativeOrZeroSide_throwsException() {
            Executable negativeSquare = () -> new Square(-1);
            Executable zeroSquare = () -> new Square(0);
            assertThrows(NegativeParameterError.class, negativeSquare);
            assertThrows(ZeroParameterError.class, zeroSquare);
        }

        @Test
        @DisplayName("Square Side Test")
        void squareSide_returnsCorrectValue() throws Exception {
            Square square = new Square(3.0);
            double actual = square.getSide();
            double expected = 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Square Area Test")
        void squareArea_returnsCorrectValue() throws Exception {
            Square square = new Square(3.0);
            double actual = square.area();
            double expected = Math.pow(3.0, 2);
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Square Perimeter Test")
        void squarePerimeter_returnsCorrectValue() throws Exception {
            Square square = new Square(3.0);
            double actual = square.perimeter();
            double expected = 4 * 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }
    }
}
