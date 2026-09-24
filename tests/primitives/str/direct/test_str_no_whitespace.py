"""Tests for str_no_whitespace validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_no_whitespace import str_no_whitespace
from simplibs.validate.testing import assert_type_contract


def test_str_no_whitespace_contract(subtests: pytest.Item) -> None:
    """Verify that str_no_whitespace satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_no_whitespace,
        valid_values=[
            "",
            "hello",
            "123-abc_xyz",
        ],
        invalid_values=[
            "hello world",
            " ",
            "hello\nworld",
            "\ttest",
        ],
        expected_error_name="REGEX_ERROR",
    )