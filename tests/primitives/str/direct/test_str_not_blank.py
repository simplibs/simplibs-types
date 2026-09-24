"""Tests for str_not_blank validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_not_blank import str_not_blank
from simplibs.validate.testing import assert_type_contract


def test_str_not_blank_contract(subtests: pytest.Item) -> None:
    """Verify that str_not_blank satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_not_blank,
        valid_values=[
            "a",
            "  hello  ",
            "123",
        ],
        invalid_values=[
            "",
            " ",
            "   \t\n  ",
        ],
        expected_error_name="NOT_BLANK_ERROR",
    )