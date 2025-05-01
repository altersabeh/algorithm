from fixtures import helper

from algorithm.utils.errors.parameters import NegativeParameterError, ZeroParameterError


def test_negative_value_error_returns_correct_message():
    name = "dimension"
    value = -2.0

    negative: NegativeParameterError = NegativeParameterError(name, value)

    actual = str(negative)
    expected = "NegativeParameterError: DIMENSION is -2.0, but it must be a positive value."

    assert actual == expected, helper.error_message(actual, expected)


def test_zero_value_error_returns_correct_message():
    name = "dimension"
    value = 0.0

    zero: ZeroParameterError = ZeroParameterError(name, value)

    actual = str(zero)
    expected = "ZeroParameterError: DIMENSION is 0.0, but it must be a nonzero value."

    assert actual == expected, helper.error_message(actual, expected)
