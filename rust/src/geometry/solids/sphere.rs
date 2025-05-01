use std::error::Error;
use std::f64::consts::PI;

use crate::geometry::Solid;
use crate::utils::validation;

pub struct Sphere {
    radius: f64,
}

impl Sphere {
    pub fn new(radius: f64) -> Result<Self, Box<dyn Error>> {
        validation::validate_positive(radius, "radius")?;
        Ok(Sphere { radius })
    }

    pub fn radius(&self) -> f64 {
        self.radius
    }
}

impl Solid for Sphere {
    fn surface_area(&self) -> f64 {
        4.0 * PI * self.radius.powi(2)
    }

    fn volume(&self) -> f64 {
        (4.0 / 3.0) * PI * self.radius.powi(3)
    }
}
