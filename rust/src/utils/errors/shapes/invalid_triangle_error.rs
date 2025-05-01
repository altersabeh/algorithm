use std::error::Error;
use std::fmt::{Display, Formatter, Result};

use super::super::ShapeError;

/// # InvalidTriangleError
/// Error returned when the provided side lengths cannot form a triangle.
///
/// ## Parameters
/// - `side_a (f64)` The length of the first side.
/// - `side_b (f64)` The length of the second side.
/// - `side_c (f64)` The length of the third side.
///
/// ## Example
/// ```rust
/// use algorithm::utils::errors::shapes::InvalidTriangleError;
///
/// let side_a = 3.0;
/// let side_b = 4.0;
/// let side_c = 8.0;
/// let err = InvalidTriangleError::new(side_a, side_b, side_c);
///
/// println!("{}", err);  // INVALID TRIANGLE
/// ```
///
/// ## Note
/// This error is returned when the sum of the lengths of any two sides is less
/// than or equal to the length of the third side.
#[derive(Debug)]
pub struct InvalidTriangleError {
    pub dimensions: [f64; 3],
}

impl InvalidTriangleError {
    pub fn new(side_a: f64, side_b: f64, side_c: f64) -> Self {
        Self { dimensions: [side_a, side_b, side_c] }
    }
}

impl ShapeError for InvalidTriangleError {
    fn shape(&self) -> &str {
        "Triangle"
    }

    fn dimensions(&self) -> &[f64] {
        &self.dimensions
    }

    fn reason(&self) -> &str {
        "Side lengths do not form a triangle"
    }
}

impl Display for InvalidTriangleError {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{}", self.display())
    }
}

impl Error for InvalidTriangleError {}
