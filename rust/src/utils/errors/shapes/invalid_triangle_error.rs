use std::error::Error;
use std::fmt::{Display, Formatter, Result};

use super::super::ShapeError;

/// # InvalidTriangleError
/// Error returned when the provided side lengths cannot form a triangle.
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
    pub dimensions: Vec<f64>,
}

impl InvalidTriangleError {
    /// Creates a new instance of `InvalidTriangleError`.
    ///
    /// This constructor accepts three side lengths as `f64` values.
    ///
    /// - **Parameters**
    ///     - **side_a** The length of the first side.
    ///     - **side_b** The length of the second side.
    ///     - **side_c** The length of the third side.
    pub fn new(side_a: f64, side_b: f64, side_c: f64) -> Self {
        Self { dimensions: vec![side_a, side_b, side_c] }
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
