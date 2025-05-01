//! # errors
//!
//! This module contains types for handling specific error cases.

mod parameter_error;
mod shapes_error;

pub mod parameters;
pub mod shapes;

pub use parameter_error::ParameterError;
pub use shapes_error::ShapeError;
