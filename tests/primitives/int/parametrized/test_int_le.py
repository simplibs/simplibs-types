"""Tests for int_le parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_le import int_le
from simplibs.validate.testing import assert_type_contract


def test_int_le_contract(subtests: pytest.Item) -> None:
    """Verify that int_le satisfies full type contract & @validate_call integration."""
    le_hundred = int_le(100)

    assert_type_contract(
        subtests,
        type_=le_hundred,
        valid_values=[
            -10,
            0,
            100,
        ],
        invalid_values=[
            101,
            200,
        ],
        expected_error_name="LESS_OR_EQUAL_ERROR",
    )