use std::error::Error;
use std::f64::consts::PI;

use crate::geometry::Plane;
use crate::utils::validation;

#[derive(Debug)]
pub struct Circle {
    radius: f64,
}

impl Circle {
    pub fn new(radius: f64) -> Result<Self, Box<dyn Error>> {
        validation::validate_positive(radius, "radius")?;
        Ok(Circle { radius })
    }

    pub fn radius(&self) -> f64 {
        self.radius
    }
}

impl Plane for Circle {
    fn perimeter(&self) -> f64 {
        2.0 * PI * self.radius
    }

    fn area(&self) -> f64 {
        PI * self.radius.powi(2)
    }
}
