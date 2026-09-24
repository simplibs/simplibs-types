"""Tests for str_contains parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_contains import str_contains
from simplibs.validate.testing import assert_type_contract


def test_str_contains_contract(subtests: pytest.Item) -> None:
    """Verify that str_contains satisfies full type contract & @validate_call integration."""
    must_mention_error = str_contains("error")

    assert_type_contract(
        subtests,
        type_=must_mention_error,
        valid_values=[
            "error",
            "internal error occurred",
            "syntax_error_log",
        ],
        invalid_values=[
            "",
            "ERROR",  # Case-sensitive check
            "warning",
        ],
        expected_error_name="CONTAINS_ERROR",
    )