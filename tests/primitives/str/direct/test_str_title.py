"""Tests for str_title validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_title import str_title
from simplibs.validate.testing import assert_type_contract


def test_str_title_contract(subtests: pytest.Item) -> None:
    """Verify that str_title satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_title,
        valid_values=[
            "Hello World",
            "Python Programming",
            "Title Case Test",
        ],
        invalid_values=[
            "",
            "hello world",
            "HELLO WORLD",
            "Hello world",
        ],
        expected_error_name="IS_TITLECASE_ERROR",
    )