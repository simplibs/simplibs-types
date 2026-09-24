"""Tests for int_ge parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_ge import int_ge
from simplibs.validate.testing import assert_type_contract


def test_int_ge_contract(subtests: pytest.Item) -> None:
    """Verify that int_ge satisfies full type contract & @validate_call integration."""
    ge_zero = int_ge(0)

    assert_type_contract(
        subtests,
        type_=ge_zero,
        valid_values=[
            0,
            1,
            100,
        ],
        invalid_values=[
            -1,
            -10,
        ],
        expected_error_name="GREATER_OR_EQUAL_ERROR",
    )