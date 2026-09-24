"""Tests for str_not_empty validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_not_empty import str_not_empty
from simplibs.validate.testing import assert_type_contract


def test_str_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that str_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_not_empty,
        valid_values=[
            "a",
            " ",
            "hello",
        ],
        invalid_values=[
            "",
        ],
        expected_error_name="NOT_EMPTY_ERROR",
    )