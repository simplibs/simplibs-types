"""Tests for int_divisible_by parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_divisible_by import int_divisible_by
from simplibs.validate.testing import assert_type_contract


def test_int_divisible_by_contract(subtests: pytest.Item) -> None:
    """Verify that int_divisible_by satisfies full type contract & @validate_call integration."""
    divisible_by_five = int_divisible_by(5)

    assert_type_contract(
        subtests,
        type_=divisible_by_five,
        valid_values=[
            0,
            5,
            10,
            -15,
        ],
        invalid_values=[
            1,
            2,
            -3,
        ],
        expected_error_name="DIVISIBLE_BY_ERROR",
    )