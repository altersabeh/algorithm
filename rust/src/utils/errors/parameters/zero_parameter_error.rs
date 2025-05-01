use std::error::Error;
use std::fmt::{Display, Formatter, Result};

use super::super::ParameterError;

/// # `ZeroParameterError`
/// Error returned when a zero value is provided for a parameter that requires a
/// non-zero value.
///
/// ## Example
/// ```rust
/// use algorithm::utils::errors::parameters::ZeroParameterError;
///
/// let name = "length".to_string();
/// let value = 0.0;
/// let err = ZeroParameterError::new(name, value);
///
/// println!("{}", err);  // INVALID LENGTH
/// ```
#[derive(Debug)]
pub struct ZeroParameterError {
    pub name: String,
    pub value: f64,
}

impl ZeroParameterError {
    /// Creates a new instance of `ZeroParameterError`.
    ///
    /// This constructor accepts a parameter name as a `str` and a value as a
    /// `float`.
    ///
    /// - **Parameters**
    ///    - **name** The name of the parameter that caused the error.
    ///    - **value** The invalid (zero) value provided.
    pub fn new(name: String, value: f64) -> Self {
        ZeroParameterError { name, value }
    }
}

impl ParameterError for ZeroParameterError {
    fn name(&self) -> &str {
        &self.name
    }

    fn value(&self) -> f64 {
        self.value
    }

    fn required(&self) -> &str {
        "a nonzero value"
    }
}

impl Display for ZeroParameterError {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{}", self.display())
    }
}

impl Error for ZeroParameterError {}
