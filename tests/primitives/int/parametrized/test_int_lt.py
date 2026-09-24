"""Tests for int_lt parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_lt import int_lt
from simplibs.validate.testing import assert_type_contract


def test_int_lt_contract(subtests: pytest.Item) -> None:
    """Verify that int_lt satisfies full type contract & @validate_call integration."""
    lt_hundred = int_lt(100)

    assert_type_contract(
        subtests,
        type_=lt_hundred,
        valid_values=[
            -10,
            0,
            99,
        ],
        invalid_values=[
            100,       # Fails: strictly less than 100 required
            101,
        ],
        expected_error_name="LESS_THAN_ERROR",
    )