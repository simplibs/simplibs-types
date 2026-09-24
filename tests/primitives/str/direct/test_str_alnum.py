"""Tests for str_alnum validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_alnum import str_alnum
from simplibs.validate.testing import assert_type_contract


def test_str_alnum_contract(subtests: pytest.Item) -> None:
    """Verify that str_alnum satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_alnum,
        valid_values=[
            "abc123",
            "Python3",
            "12345",
            "abcdef",
        ],
        invalid_values=[
            "",
            "abc 123",
            "hello_world",
            "test!",
        ],
        expected_error_name="IS_ALNUM_ERROR",
    )