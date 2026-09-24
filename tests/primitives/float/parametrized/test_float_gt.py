"""Tests for float_gt parametrized validated type."""

import pytest
from simplibs.types.primitives.float.parametrized.float_gt import float_gt
from simplibs.validate.testing import assert_type_contract


def test_float_gt_contract(subtests: pytest.Item) -> None:
    """Verify that float_gt satisfies full type contract & @validate_call integration."""
    gt_zero = float_gt(0.0)

    assert_type_contract(
        subtests,
        type_=gt_zero,
        valid_values=[
            0.1,
            1.0,
            100.5,
        ],
        invalid_values=[
            0.0,         # Fails: strictly greater than 0.0 required
            -0.1,
            -10.0,
        ],
        expected_error_name="GREATER_THAN_ERROR",
    )