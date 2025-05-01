use std::error::Error;
use std::fmt::{Display, Formatter, Result};

use super::super::ShapeError;

/// # InvalidTrapezoidError
/// Error returned when the provided bases cannot form a trapezoid.
///
/// ## Example
/// ```rust
/// use algorithm::utils::errors::shapes::InvalidTrapezoidError;
///
/// let base_a = 5.0;
/// let base_b = 5.0;
/// let err = InvalidTrapezoidError::new(base_a, base_b);
///
/// println!("{}", err);  // INVALID TRAPEZOID
/// ```
///
/// ## Note
/// This error is returned when the two bases are equal, which does not form a
/// trapezoid.
#[derive(Debug)]
pub struct InvalidTrapezoidError {
    pub dimensions: [f64; 2],
}

impl InvalidTrapezoidError {
    /// Creates a new instance of `InvalidTrapezoidError`.
    ///
    /// This constructor accepts two base lengths as `f64` values.
    ///
    /// - **Parameters**
    ///     - **base_a** The length of the first base.
    ///     - **base_b** The length of the second base.
    pub fn new(base_a: f64, base_b: f64) -> Self {
        Self { dimensions: [base_a, base_b] }
    }
}

impl ShapeError for InvalidTrapezoidError {
    fn shape(&self) -> &str {
        "Trapezoid"
    }

    fn dimensions(&self) -> &[f64] {
        &self.dimensions
    }

    fn reason(&self) -> &str {
        "Bases do not form a trapezoid"
    }
}

impl Display for InvalidTrapezoidError {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{}", self.display())
    }
}

impl Error for InvalidTrapezoidError {}
