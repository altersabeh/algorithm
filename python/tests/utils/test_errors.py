from fixtures import helper

from algorithm.utils.errors.values import NegativeValueError, ZeroValueError


def test_negative_value_error_returns_correct_message():
    name = "dimension"
    value = -2.0

    negative: NegativeValueError = NegativeValueError(name, value)

    actual = str(negative)
    expected = "NegativeValueError: Invalid value for 'DIMENSION'. Received '-2.0', but 'DIMENSION' must be a positive value."

    assert actual == expected, helper.error_message(actual, expected)


def test_zero_value_error_returns_correct_message():
    name = "dimension"
    value = 0.0

    zero: ZeroValueError = ZeroValueError(name, value)

    actual = str(zero)
    expected = "ZeroValueError: Invalid value for 'DIMENSION'. Received '0.0', but 'DIMENSION' must be a nonzero value."

    assert actual == expected, helper.error_message(actual, expected)
