"""Tests for str_alpha validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_alpha import str_alpha
from simplibs.validate.testing import assert_type_contract


def test_str_alpha_contract(subtests: pytest.Item) -> None:
    """Verify that str_alpha satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_alpha,
        valid_values=[
            "abc",
            "Python",
            "Hello",
        ],
        invalid_values=[
            "",
            "abc123",
            "hello world",
            "test!",
        ],
        expected_error_name="IS_ALPHA_ERROR",
    )