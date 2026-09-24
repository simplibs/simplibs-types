"""Tests for float_le parametrized validated type."""

import pytest
from simplibs.types.primitives.float.parametrized.float_le import float_le
from simplibs.validate.testing import assert_type_contract


def test_float_le_contract(subtests: pytest.Item) -> None:
    """Verify that float_le satisfies full type contract & @validate_call integration."""
    le_hundred = float_le(100.0)

    assert_type_contract(
        subtests,
        type_=le_hundred,
        valid_values=[
            -10.0,
            0.0,
            100.0,
        ],
        invalid_values=[
            100.1,
            200.0,
        ],
        expected_error_name="LESS_OR_EQUAL_ERROR",
    )