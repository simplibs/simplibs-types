"""Tests for str_blank validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_blank import str_blank
from simplibs.validate.testing import assert_type_contract


def test_str_blank_contract(subtests: pytest.Item) -> None:
    """Verify that str_blank satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_blank,
        valid_values=[
            "",
            " ",
            "   \t\n  ",
        ],
        invalid_values=[
            "a",
            "   a   ",
            "hello",
        ],
        expected_error_name="IS_BLANK_ERROR",
    )