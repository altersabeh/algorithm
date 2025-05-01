use std::f64::consts::PI;

use algorithm::geometry::Solid;
use algorithm::geometry::solids::{Cylinder, Sphere};
use algorithm::utils::errors::parameters::{NegativeParameterError, ZeroParameterError};

use crate::fixtures::helper;

#[cfg(test)]
mod cylinder_test {
    use super::*;

    #[test]
    fn cylinder_new_negative_or_zero_radius_returns_error() {
        let negative_cylinder = Cylinder::new(-1.0, 2.0);
        let zero_cylinder = Cylinder::new(0.0, 2.0);
        assert!(matches!(negative_cylinder, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_cylinder, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn cylinder_new_negative_or_zero_height_returns_error() {
        let negative_cylinder = Cylinder::new(2.0, -1.0);
        let zero_cylinder = Cylinder::new(2.0, 0.0);
        assert!(matches!(negative_cylinder, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_cylinder, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn cylinder_radius_returns_correct_value() {
        let cylinder = Cylinder::new(3.0, 4.0).unwrap();
        let actual = cylinder.radius();
        let expected = 3.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn cylinder_height_returns_correct_value() {
        let cylinder = Cylinder::new(3.0, 4.0).unwrap();
        let actual = cylinder.height();
        let expected = 4.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn cylinder_surface_area_returns_correct_value() {
        let cylinder = Cylinder::new(3.0, 4.0).unwrap();
        let actual = cylinder.surface_area();
        let expected = 2.0 * PI * 3.0 * (3.0 + 4.0);
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn cylinder_volume_returns_correct_value() {
        let cylinder = Cylinder::new(3.0, 4.0).unwrap();
        let actual = cylinder.volume();
        let expected = PI * 3.0f64.powi(2) * 4.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }
}

#[cfg(test)]
mod sphere_test {
    use super::*;

    #[test]
    fn sphere_new_negative_or_zero_radius_returns_error() {
        let negative_sphere = Sphere::new(-1.0);
        let zero_sphere = Sphere::new(0.0);
        assert!(matches!(negative_sphere, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_sphere, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn sphere_radius_returns_correct_value() {
        let sphere = Sphere::new(3.0).unwrap();
        let actual = sphere.radius();
        let expected = 3.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn sphere_surface_area_returns_correct_value() {
        let sphere = Sphere::new(3.0).unwrap();
        let actual = sphere.surface_area();
        let expected = 4.0 * PI * 3.0f64.powi(2);
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn sphere_volume_returns_correct_value() {
        let sphere = Sphere::new(3.0).unwrap();
        let actual = sphere.volume();
        let expected = (4.0 / 3.0) * PI * 3.0f64.powi(3);
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }
}
