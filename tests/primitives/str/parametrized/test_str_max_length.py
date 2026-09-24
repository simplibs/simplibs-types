"""Tests for str_max_length parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_max_length import str_max_length
from simplibs.validate.testing import assert_type_contract


def test_str_max_length_contract(subtests: pytest.Item) -> None:
    """Verify that str_max_length satisfies full type contract & @validate_call integration."""
    short_str = str_max_length(3)

    assert_type_contract(
        subtests,
        type_=short_str,
        valid_values=[
            "",
            "a",
            "abc",
        ],
        invalid_values=[
            "abcd",
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )