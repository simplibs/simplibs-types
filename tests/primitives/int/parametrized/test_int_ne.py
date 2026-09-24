"""Tests for int_ne parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_ne import int_ne
from simplibs.validate.testing import assert_type_contract


def test_int_ne_contract(subtests: pytest.Item) -> None:
    """Verify that int_ne satisfies full type contract & @validate_call integration."""
    not_thirteen = int_ne(13)

    assert_type_contract(
        subtests,
        type_=not_thirteen,
        valid_values=[
            0,
            12,
            14,
            -13,
        ],
        invalid_values=[
            13,        # Forbidden value
        ],
        expected_error_name="NOT_EQUALS_ERROR",
    )