use std::any::type_name;
use std::error::Error;
use std::fmt::{Debug, Display};

/// Base trait for all shape-related errors.
pub trait ShapeError: Debug + Display + Error {
    fn shape(&self) -> &str;
    fn dimensions(&self) -> &[f64];
    fn reason(&self) -> &str;

    fn display(&self) -> String {
        let name = type_name::<Self>().split("::").last().unwrap();
        let message = self.message();
        format!("{}: {}", name, message)
    }

    fn message(&self) -> String {
        let shape = self.shape().to_uppercase();
        let dim_label = if self.dimensions().len() == 1 { "dimension" } else { "dimensions" };
        let dimensions = self.format_dimensions();
        let reason = self.reason().to_lowercase();
        format!("{} with {} {} is invalid: {}.", shape, dim_label, dimensions, reason)
    }

    fn format_dimensions(&self) -> String {
        match self.dimensions() {
            | [d] => format!("{}", d),
            | [d1, d2] => format!("{} and {}", d1, d2),
            | [rest @ .., last] if !rest.is_empty() => {
                let rest_str = rest.iter().map(|d| d.to_string()).collect::<Vec<_>>().join(", ");
                format!("{}, and {}", rest_str, last)
            },
            | _ => "no dimensions".to_string(),
        }
    }
}
