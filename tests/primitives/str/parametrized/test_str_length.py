"""Tests for str_length parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_length import str_length
from simplibs.validate.testing import assert_type_contract


def test_str_length_contract(subtests: pytest.Item) -> None:
    """Verify that str_length satisfies full type contract & @validate_call integration."""
    four_chars = str_length(4)

    assert_type_contract(
        subtests,
        type_=four_chars,
        valid_values=[
            "abcd",
            "1234",
        ],
        invalid_values=[
            "",
            "abc",
            "abcde",
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )