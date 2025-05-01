use std::error::Error;

use super::errors::parameters::{NegativeParameterError, ZeroParameterError};

pub(crate) fn validate_positive(value: f64, name: &str) -> Result<(), Box<dyn Error>> {
    let name = name.to_string();
    match value {
        | v if v < 0.0 => Err(Box::new(NegativeParameterError { name, value })),
        | 0.0 => Err(Box::new(ZeroParameterError { name, value })),
        | _ => Ok(()),
    }
}
