"""Tests for str_hex_color validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_hex_color import str_hex_color
from simplibs.validate.testing import assert_type_contract


def test_str_hex_color_contract(subtests: pytest.Item) -> None:
    """Verify that str_hex_color satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_hex_color,
        valid_values=[
            "#ffffff",
            "#000000",
            "#FF0000",
            "#1a2b3c",
        ],
        invalid_values=[
            "ffffff",
            "#fff",
            "#fffffff",
            "#12345g",
        ],
        expected_error_name="REGEX_ERROR",
    )