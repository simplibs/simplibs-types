"""Tests for int_multiple_of parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_multiple_of import int_multiple_of
from simplibs.validate.testing import assert_type_contract


def test_int_multiple_of_contract(subtests: pytest.Item) -> None:
    """Verify that int_multiple_of satisfies full type contract & @validate_call integration."""
    multiple_of_five = int_multiple_of(5)

    assert_type_contract(
        subtests,
        type_=multiple_of_five,
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