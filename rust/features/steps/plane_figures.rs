use std::error::Error;
use std::fmt::Display;

use algorithm::geometry::planes::{Circle, Rectangle, Square};
use cucumber::{given, then, when};

#[derive(Debug, Default, cucumber::World)]
pub struct PlaneTest {
    // Circle
    circle_radius: Option<f64>,
    circle_result: Option<Result<Circle, Box<dyn Error>>>,

    // Rectangle
    rectangle_width: Option<f64>,
    rectangle_height: Option<f64>,
    rectangle_result: Option<Result<Rectangle, Box<dyn Error>>>,

    // Square
    square_side: Option<f64>,
    square_result: Option<Result<Square, Box<dyn Error>>>,
}

impl PlaneTest {
    fn circle(&self) -> &Circle {
        self.circle_result
            .as_ref()
            .expect("Circle result missing")
            .as_ref()
            .expect("Circle creation failed")
    }

    fn rectangle(&self) -> &Rectangle {
        self.rectangle_result
            .as_ref()
            .expect("Rectangle result missing")
            .as_ref()
            .expect("Rectangle creation failed")
    }

    fn square(&self) -> &Square {
        self.square_result
            .as_ref()
            .expect("Square result missing")
            .as_ref()
            .expect("Square creation failed")
    }
}

// region:CIRCLE STEPS
#[given(expr = "a circle radius of {float}")]
async fn given_circle_radius(plane_test: &mut PlaneTest, radius: f64) {
    plane_test.circle_radius = Some(radius);
}

#[when("the circle is created")]
async fn when_circle_created(plane_test: &mut PlaneTest) {
    if let Some(radius) = plane_test.circle_radius {
        plane_test.circle_result = Some(Circle::new(radius));
    }
}

#[then(expr = "the circle's radius should be {float}")]
async fn then_circle_radius(plane_test: &mut PlaneTest, expected: f64) {
    let actual = plane_test.circle().radius();
    assert_eq!(actual, expected, "{}", generate_error_report(actual, expected));
}
// endregion

// region:RECTANGLE STEPS
#[given(expr = "a rectangle width of {float}")]
async fn given_rectangle_width(plane_test: &mut PlaneTest, width: f64) {
    plane_test.rectangle_width = Some(width);
}

#[given(expr = "a rectangle height of {float}")]
async fn given_rectangle_height(plane_test: &mut PlaneTest, height: f64) {
    plane_test.rectangle_height = Some(height);
}

#[when("the rectangle is created")]
async fn when_rectangle_created(plane_test: &mut PlaneTest) {
    if let (Some(width), Some(height)) = (plane_test.rectangle_width, plane_test.rectangle_height) {
        plane_test.rectangle_result = Some(Rectangle::new(width, height));
    }
}

#[then(expr = "the rectangle's width should be {float}")]
async fn then_rectangle_width(plane_test: &mut PlaneTest, expected: f64) {
    let actual = plane_test.rectangle().width();
    assert_eq!(actual, expected, "{}", generate_error_report(actual, expected));
}

#[then(expr = "the rectangle's height should be {float}")]
async fn then_rectangle_height(plane_test: &mut PlaneTest, expected: f64) {
    let actual = plane_test.rectangle().height();
    assert_eq!(actual, expected, "{}", generate_error_report(actual, expected));
}
// endregion

// region:SQUARE STEPS
#[given(expr = "a square side length of {float}")]
async fn given_square_side(plane_test: &mut PlaneTest, side: f64) {
    plane_test.square_side = Some(side);
}

#[when("the square is created")]
async fn when_square_created(plane_test: &mut PlaneTest) {
    if let Some(side) = plane_test.square_side {
        plane_test.square_result = Some(Square::new(side));
    }
}

#[then(expr = "the square's side length should be {float}")]
async fn then_square_side(plane_test: &mut PlaneTest, expected: f64) {
    let actual = plane_test.square().side();
    assert_eq!(actual, expected, "{}", generate_error_report(actual, expected));
}
// endregion

fn generate_error_report<T: Display>(actual: T, expected: T) -> String {
    format!("Actual: {actual}\nExpected: {expected}")
}
