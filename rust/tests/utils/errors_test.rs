use algorithm::utils::errors::parameters::{NegativeParameterError, ZeroParameterError};

use crate::fixtures::helper;

#[test]
fn negative_value_error_returns_correct_message() {
    let name = "dimension".to_string();
    let value = -2.0;

    let negative: NegativeParameterError = NegativeParameterError { name, value };

    let actual = format!("{negative}");
    let expected = "NegativeParameterError: DIMENSION is -2, but it must be a positive value.";

    assert_eq!(actual, expected, "{}", helper::error_message(&actual, &expected.to_string()));
}

#[test]
fn test_zero_value_error_returns_correct_message() {
    let name = "dimension".to_string();
    let value = 0.0;

    let zero: ZeroParameterError = ZeroParameterError { name, value };

    let actual = format!("{zero}");
    let expected = "ZeroParameterError: DIMENSION is 0, but it must be a nonzero value.";

    assert_eq!(actual, expected, "{}", helper::error_message(&actual, &expected.to_string()));
}
