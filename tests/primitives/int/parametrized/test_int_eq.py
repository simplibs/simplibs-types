"""Tests for int_eq parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_eq import int_eq
from simplibs.validate.testing import assert_type_contract


def test_int_eq_contract(subtests: pytest.Item) -> None:
    """Verify that int_eq satisfies full type contract & @validate_call integration."""
    must_be_seven = int_eq(7)

    assert_type_contract(
        subtests,
        type_=must_be_seven,
        valid_values=[
            7,
        ],
        invalid_values=[
            0,
            6,
            8,
            -7,
        ],
        expected_error_name="EQUALS_ERROR",
    )