"""Tests for str_upper validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_upper import str_upper
from simplibs.validate.testing import assert_type_contract


def test_str_upper_contract(subtests: pytest.Item) -> None:
    """Verify that str_upper satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_upper,
        valid_values=[
            "HELLO",
            "HELLO WORLD 123!",
            "ABC",
        ],
        invalid_values=[
            "",
            "Hello",
            "hello",
            "HELLo",
        ],
        expected_error_name="IS_UPPERCASE_ERROR",
    )