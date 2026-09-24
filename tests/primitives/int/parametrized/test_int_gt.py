"""Tests for int_gt parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_gt import int_gt
from simplibs.validate.testing import assert_type_contract


def test_int_gt_contract(subtests: pytest.Item) -> None:
    """Verify that int_gt satisfies full type contract & @validate_call integration."""
    gt_zero = int_gt(0)

    assert_type_contract(
        subtests,
        type_=gt_zero,
        valid_values=[
            1,
            10,
            100,
        ],
        invalid_values=[
            0,         # Fails: strictly greater than 0 required
            -1,
            -10,
        ],
        expected_error_name="GREATER_THAN_ERROR",
    )