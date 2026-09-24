"""Tests for str_whitespace validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_whitespace import str_whitespace
from simplibs.validate.testing import assert_type_contract


def test_str_whitespace_contract(subtests: pytest.Item) -> None:
    """Verify that str_whitespace satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_whitespace,
        valid_values=[
            " ",
            "   ",
            "\t\n\r",
            " \t \n ",
        ],
        invalid_values=[
            "",
            " a ",
            "hello",
            "  .  ",
        ],
        expected_error_name="IS_WHITESPACE_ERROR",
    )