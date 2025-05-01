use algorithm::geometry::Plane;
use algorithm::geometry::planes::{Circle, Rectangle, Square};
use algorithm::utils::errors::parameters::{NegativeParameterError, ZeroParameterError};

use crate::fixtures::helper;

#[cfg(test)]
mod circle_test {
    use super::*;

    #[test]
    fn circle_new_negative_or_zero_radius_returns_error() {
        let negative_circle = Circle::new(-1.0);
        let zero_circle = Circle::new(0.0);
        assert!(matches!(negative_circle, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_circle, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn circle_radius_returns_correct_value() {
        let circle = Circle::new(3.0).unwrap();
        let actual = circle.radius();
        let expected = 3.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn circle_area_returns_correct_value() {
        let circle = Circle::new(3.0).unwrap();
        let actual = circle.area();
        let expected = 28.274333882308138;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn circle_perimeter_returns_correct_value() {
        let circle = Circle::new(3.0).unwrap();
        let actual = circle.perimeter();
        let expected = 18.84955592153876;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }
}

#[cfg(test)]
mod rectangle_test {
    use super::*;
    #[test]
    fn rectangle_new_negative_or_zero_width_returns_error() {
        let negative_rectangle = Rectangle::new(-1.0, 2.0);
        let zero_rectangle = Rectangle::new(0.0, 2.0);
        assert!(matches!(negative_rectangle, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_rectangle, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn rectangle_new_negative_or_zero_height_returns_error() {
        let negative_rectangle = Rectangle::new(2.0, -1.0);
        let zero_rectangle = Rectangle::new(2.0, 0.0);
        assert!(matches!(negative_rectangle, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_rectangle, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn rectangle_width_returns_correct_value() {
        let rectangle = Rectangle::new(4.0, 5.0).unwrap();
        let actual = rectangle.width();
        let expected = 4.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn rectangle_height_returns_correct_value() {
        let rectangle = Rectangle::new(4.0, 5.0).unwrap();
        let actual = rectangle.height();
        let expected = 5.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn rectangle_area_returns_correct_value() {
        let rectangle = Rectangle::new(4.0, 5.0).unwrap();
        let actual = rectangle.area();
        let expected = 20.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn rectangle_perimeter_returns_correct_value() {
        let rectangle = Rectangle::new(4.0, 5.0).unwrap();
        let actual = rectangle.perimeter();
        let expected = 18.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }
}

#[cfg(test)]
mod square_test {
    use super::*;

    #[test]
    fn square_new_negative_or_zero_side_returns_error() {
        let negative_square = Square::new(-1.0);
        let zero_square = Square::new(0.0);
        assert!(matches!(negative_square, Err(e) if e.is::<NegativeParameterError>()));
        assert!(matches!(zero_square, Err(e) if e.is::<ZeroParameterError>()));
    }

    #[test]
    fn square_side_returns_correct_value() {
        let square = Square::new(4.0).unwrap();
        let actual = square.side();
        let expected = 4.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn square_area_returns_correct_value() {
        let square = Square::new(4.0).unwrap();
        let actual = square.area();
        let expected = 16.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }

    #[test]
    fn square_perimeter_returns_correct_value() {
        let square = Square::new(4.0).unwrap();
        let actual = square.perimeter();
        let expected = 16.0;
        assert_eq!(actual, expected, "{}", helper::error_message(actual, expected));
    }
}
