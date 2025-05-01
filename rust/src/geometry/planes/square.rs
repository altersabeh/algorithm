use std::error::Error;

use crate::geometry::Plane;
use crate::utils::validation;

#[derive(Debug)]
pub struct Square {
    side: f64,
}

impl Square {
    pub fn new(side: f64) -> Result<Self, Box<dyn Error>> {
        validation::validate_positive(side, "side")?;
        Ok(Square { side })
    }

    pub fn side(&self) -> f64 {
        self.side
    }
}

impl Plane for Square {
    fn perimeter(&self) -> f64 {
        4.0 * self.side
    }

    fn area(&self) -> f64 {
        self.side.powi(2)
    }
}
