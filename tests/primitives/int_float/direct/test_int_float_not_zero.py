"""Tests for int_float_not_zero validated type."""

import pytest
from simplibs.types.primitives.int_float.direct.int_float_not_zero import int_float_not_zero
from simplibs.validate.testing import assert_type_contract


def test_int_float_not_zero_contract(subtests: pytest.Item) -> None:
    """Verify that int_float_not_zero satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_float_not_zero,
        valid_values=[
            1,
            -1,
            0.00001,
            -123.45,
        ],
        invalid_values=[
            0,
            0.0,
            -0.0,
        ],
        expected_error_name="NOT_RULE_ERROR",
    )