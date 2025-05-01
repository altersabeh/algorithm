use std::error::Error;
use std::fmt::{Display, Formatter, Result};

use super::super::ParameterError;

/// # NegativeParameterError
/// Error returned when a negative value is provided for a parameter that
/// requires a non-negative value.
///
/// ## Example
/// ```rust
/// use algorithm::utils::errors::parameters::NegativeParameterError;
///
/// let name = "length".to_string();
/// let value = -5.0;
/// let err = NegativeParameterError::new(name, value);
///
/// println!("{}", err);  // INVALID LENGTH
/// ```
#[derive(Debug)]
pub struct NegativeParameterError {
    pub name: String,
    pub value: f64,
}

impl NegativeParameterError {
    /// Creates a new instance of `NegativeParameterError`.
    ///
    /// This constructor accepts a parameter name as a `str` and a value as a
    /// `float`.
    ///
    /// - **Parameters**
    ///     - **name** The name of the parameter that caused the error.
    ///     - **value** The invalid (negative) value provided.
    pub fn new(name: String, value: f64) -> Self {
        NegativeParameterError { name, value }
    }
}

impl ParameterError for NegativeParameterError {
    fn name(&self) -> &str {
        &self.name
    }

    fn value(&self) -> f64 {
        self.value
    }

    fn required(&self) -> &str {
        "a non-negative value"
    }
}

impl Display for NegativeParameterError {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{}", self.display())
    }
}

impl Error for NegativeParameterError {}
