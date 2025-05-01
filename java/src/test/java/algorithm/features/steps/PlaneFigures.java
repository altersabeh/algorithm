package algorithm.features.steps;

import static org.junit.jupiter.api.Assertions.assertEquals;

import algorithm.geometry.planes.Circle;
import algorithm.geometry.planes.Rectangle;
import algorithm.geometry.planes.Square;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class PlaneFigures {
    private Circle circle;
    private Rectangle rectangle;
    private Square square;

    private double circleRadius;
    private double rectangleWidth;
    private double rectangleHeight;
    private double squareSide;

    // #region CIRCLE STEPS
    @Given("a circle radius of {double}")
    public void a_circle_radius_of(double radius) {
        this.circleRadius = radius;
    }

    @When("the circle is created")
    public void the_circle_is_created() throws Exception {
        this.circle = new Circle(circleRadius);
    }

    @Then("the circle's radius should be {double}")
    public void the_circle_s_radius_should_be(double expected) {
        double actual = circle.getRadius();
        assertEquals(expected, actual, generateErrorMessage(actual, expected));
    }
    // #endregion

    // #region RECTANGLE STEPS
    @Given("a rectangle width of {double}")
    public void a_rectangle_width_of(double width) {
        this.rectangleWidth = width;
    }

    @Given("a rectangle height of {double}")
    public void a_rectangle_height_of(double height) {
        this.rectangleHeight = height;
    }

    @When("the rectangle is created")
    public void the_rectangle_is_created() throws Exception {
        this.rectangle = new Rectangle(rectangleWidth, rectangleHeight);
    }

    @Then("the rectangle's width should be {double}")
    public void the_rectangle_s_width_should_be(double expected) {
        double actual = rectangle.getWidth();
        assertEquals(expected, actual, generateErrorMessage(actual, expected));
    }

    @Then("the rectangle's height should be {double}")
    public void the_rectangle_s_height_should_be(double expected) {
        double actual = rectangle.getHeight();
        assertEquals(expected, actual, generateErrorMessage(actual, expected));
    }
    // #endregion

    // #region SQUARE STEPS
    @Given("a square side length of {double}")
    public void a_square_side_length_of(double side) {
        this.squareSide = side;
    }

    @When("the square is created")
    public void the_square_is_created() throws Exception {
        this.square = new Square(squareSide);
    }

    @Then("the square's side length should be {double}")
    public void the_square_s_side_length_should_be(double expected) {
        double actual = square.getSide();
        assertEquals(expected, actual, generateErrorMessage(actual, expected));
    }
    // #endregion

    private <T> String generateErrorMessage(T actual, T expected) {
        return String.format("Actual: %s\nExpected: %s", actual, expected);
    }
}
