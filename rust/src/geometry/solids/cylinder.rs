use std::error::Error;
use std::f64::consts::PI;

use crate::geometry::Solid;
use crate::utils::validation;

pub struct Cylinder {
    radius: f64,
    height: f64,
}

impl Cylinder {
    pub fn new(radius: f64, height: f64) -> Result<Self, Box<dyn Error>> {
        validation::validate_positive(radius, "radius")?;
        validation::validate_positive(height, "height")?;
        Ok(Cylinder { radius, height })
    }

    pub fn radius(&self) -> f64 {
        self.radius
    }

    pub fn height(&self) -> f64 {
        self.height
    }
}

impl Solid for Cylinder {
    fn surface_area(&self) -> f64 {
        2.0 * PI * self.radius * (self.radius + self.height)
    }

    fn volume(&self) -> f64 {
        PI * self.radius.powi(2) * self.height
    }
}
