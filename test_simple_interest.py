import pytest

from simple_interest.calculator import calculate_simple_interest
from simple_interest.validation import validate_simple_interest_payload


def test_calculate_simple_interest():
    assert calculate_simple_interest(1000.0, 5.0, 2.0) == 100.0


def test_validate_simple_interest_payload_success():
    payload = {"principal": 1000, "rate": 5, "time": 2}
    validated = validate_simple_interest_payload(payload)

    assert isinstance(validated, dict)
    assert validated == {"principal": 1000.0, "rate": 5.0, "time": 2.0}


@pytest.mark.parametrize(
    "payload, expected_error",
    [
        ({}, "Missing required field(s): principal, rate, time."),
        ({"principal": "abc", "rate": 5, "time": 2}, "principal must be numeric."),
        ({"principal": -1000, "rate": 5, "time": 2}, "principal must be non-negative."),
        ({"principal": True, "rate": 5, "time": 2}, "principal must be a numeric value."),
    ],
)
def test_validate_simple_interest_payload_errors(payload, expected_error):
    error = validate_simple_interest_payload(payload)

    assert isinstance(error, str)
    assert expected_error in error
