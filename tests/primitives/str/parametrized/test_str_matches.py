"""Tests for str_matches parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_matches import str_matches
from simplibs.validate.testing import assert_type_contract


def test_str_matches_contract(subtests: pytest.Item) -> None:
    """Verify that str_matches satisfies full type contract & @validate_call integration."""
    digits_only = str_matches(r"^\d+$")

    assert_type_contract(
        subtests,
        type_=digits_only,
        valid_values=[
            "0",
            "12345",
        ],
        invalid_values=[
            "",
            "123a",
            "abc",
        ],
        expected_error_name="REGEX_ERROR",
    )