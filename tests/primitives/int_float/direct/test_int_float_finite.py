"""Tests for int_float_finite validated type."""

import pytest
from simplibs.types.primitives.int_float.direct.int_float_finite import int_float_finite
from simplibs.validate.testing import assert_type_contract


def test_int_float_finite_contract(subtests: pytest.Item) -> None:
    """Verify that int_float_finite satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_float_finite,
        valid_values=[
            0,
            42,
            -100,
            0.0,
            3.14159,
            -123.45,
        ],
        invalid_values=[
            float("nan"),
            float("inf"),
            float("-inf"),
        ],
        expected_error_name="IS_FINITE_ERROR",
    )