use std::error::Error;

use crate::geometry::Plane;
use crate::utils::validation;

#[derive(Debug)]
pub struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    pub fn new(width: f64, height: f64) -> Result<Self, Box<dyn Error>> {
        validation::validate_positive(width, "width")?;
        validation::validate_positive(height, "height")?;
        Ok(Rectangle { width, height })
    }

    pub fn width(&self) -> f64 {
        self.width
    }

    pub fn height(&self) -> f64 {
        self.height
    }
}

impl Plane for Rectangle {
    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    fn area(&self) -> f64 {
        self.width * self.height
    }
}
