"""Tests for str_empty validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_empty import str_empty
from simplibs.validate.testing import assert_type_contract


def test_str_empty_contract(subtests: pytest.Item) -> None:
    """Verify that str_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_empty,
        valid_values=[
            "",
        ],
        invalid_values=[
            " ",
            "a",
            "hello",
        ],
        expected_error_name="IS_EMPTY_ERROR",
    )