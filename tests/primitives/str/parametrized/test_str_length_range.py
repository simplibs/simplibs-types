"""Tests for str_length_range parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_length_range import str_length_range
from simplibs.validate.testing import assert_type_contract


def test_str_length_range_contract(subtests: pytest.Item) -> None:
    """Verify that str_length_range satisfies full type contract & @validate_call integration."""
    username_str = str_length_range(3, 5)

    assert_type_contract(
        subtests,
        type_=username_str,
        valid_values=[
            "abc",    # Min limit
            "abcd",
            "abcde",  # Max limit
        ],
        invalid_values=[
            "",
            "ab",
            "abcdef",
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )