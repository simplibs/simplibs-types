"""Tests for float_ge parametrized validated type."""

import pytest
from simplibs.types.primitives.float.parametrized.float_ge import float_ge
from simplibs.validate.testing import assert_type_contract


def test_float_ge_contract(subtests: pytest.Item) -> None:
    """Verify that float_ge satisfies full type contract & @validate_call integration."""
    ge_zero = float_ge(0.0)

    assert_type_contract(
        subtests,
        type_=ge_zero,
        valid_values=[
            0.0,
            0.1,
            100.5,
        ],
        invalid_values=[
            -0.1,
            -10.0,
        ],
        expected_error_name="GREATER_OR_EQUAL_ERROR",
    )