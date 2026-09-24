"""Tests for str_digit validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_digit import str_digit
from simplibs.validate.testing import assert_type_contract


def test_str_digit_contract(subtests: pytest.Item) -> None:
    """Verify that str_digit satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_digit,
        valid_values=[
            "0",
            "1234567890",
        ],
        invalid_values=[
            "",
            "123a",
            "-123",
            "12.3",
        ],
        expected_error_name="IS_DIGIT_STRING_ERROR",
    )