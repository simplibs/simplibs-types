"""Tests for str_min_length parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_min_length import str_min_length
from simplibs.validate.testing import assert_type_contract


def test_str_min_length_contract(subtests: pytest.Item) -> None:
    """Verify that str_min_length satisfies full type contract & @validate_call integration."""
    non_trivial_str = str_min_length(3)

    assert_type_contract(
        subtests,
        type_=non_trivial_str,
        valid_values=[
            "abc",
            "abcd",
        ],
        invalid_values=[
            "",
            "ab",
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )