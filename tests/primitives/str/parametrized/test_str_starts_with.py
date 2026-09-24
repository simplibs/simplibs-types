"""Tests for str_starts_with parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_starts_with import str_starts_with
from simplibs.validate.testing import assert_type_contract


def test_str_starts_with_contract(subtests: pytest.Item) -> None:
    """Verify that str_starts_with satisfies full type contract & @validate_call integration."""
    https_url = str_starts_with("https://")

    assert_type_contract(
        subtests,
        type_=https_url,
        valid_values=[
            "https://",
            "https://example.com",
        ],
        invalid_values=[
            "",
            "http://example.com",
            "HTTPS://example.com",
        ],
        expected_error_name="STARTS_WITH_ERROR",
    )