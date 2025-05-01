use std::fmt::Display;

pub fn error_message<T: Display>(actual: T, expected: T) -> String {
    format!("Expected {expected}, but got {actual}")
}
