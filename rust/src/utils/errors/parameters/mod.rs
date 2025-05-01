//! # parameters
//!
//! This module contains types for handling specific error cases related to
//! parameters.

mod negative_parameter_error;
mod zero_parameter_error;

pub use negative_parameter_error::NegativeParameterError;
pub use zero_parameter_error::ZeroParameterError;
