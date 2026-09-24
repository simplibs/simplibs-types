"""Tests for str_ascii validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_ascii import str_ascii
from simplibs.validate.testing import assert_type_contract


def test_str_ascii_contract(subtests: pytest.Item) -> None:
    """Verify that str_ascii satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_ascii,
        valid_values=[
            "",
            "Hello World",
            "123!@#",
        ],
        invalid_values=[
            "Příliš žluťoučký kůň",
            "emoji 😀",
        ],
        expected_error_name="IS_ASCII_ERROR",
    )