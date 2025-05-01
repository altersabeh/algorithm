use std::any::type_name;
use std::error::Error;
use std::fmt::{Debug, Display};

/// Base trait for all parameter-related errors.
pub trait ParameterError: Debug + Display + Error {
    fn name(&self) -> &str;
    fn value(&self) -> f64;
    fn required(&self) -> &str;

    fn display(&self) -> String {
        let name = type_name::<Self>().split("::").last().unwrap();
        let message = self.message();
        format!("{}: {}", name, message)
    }

    fn message(&self) -> String {
        let name = self.name().to_uppercase();
        format!("{} is {}, but it must be {}.", name, self.value(), self.required())
    }
}
