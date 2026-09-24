"""Tests for float_zero validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_zero import float_zero
from simplibs.validate.testing import assert_type_contract


def test_float_zero_contract(subtests: pytest.Item) -> None:
    """Verify that float_zero satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_zero,
        valid_values=[
            0.0,
            -0.0,
        ],
        invalid_values=[
            0.00001,
            -0.00001,
            1.0,
            -1.0,
        ],
        expected_error_name="IS_ZERO_ERROR",
    )