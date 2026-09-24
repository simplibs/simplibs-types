"""Tests for str_one_of parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_one_of import str_one_of
from simplibs.validate.testing import assert_type_contract


def test_str_one_of_contract(subtests: pytest.Item) -> None:
    """Verify that str_one_of satisfies full type contract & @validate_call integration."""
    status = str_one_of("pending", "active", "closed")

    assert_type_contract(
        subtests,
        type_=status,
        valid_values=[
            "pending",
            "active",
            "closed",
        ],
        invalid_values=[
            "",
            "PENDING",
            "unknown",
        ],
        expected_error_name="IS_IN_ERROR",
    )