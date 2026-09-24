"""Tests for float_not_zero validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_not_zero import float_not_zero
from simplibs.validate.testing import assert_type_contract


def test_float_not_zero_contract(subtests: pytest.Item) -> None:
    """Verify that float_not_zero satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_not_zero,
        valid_values=[
            1.0,
            -1.0,
            100.5,
            -100.5,
        ],
        invalid_values=[
            0.0,
            -0.0,
        ],
        expected_error_name="NOT_RULE_ERROR",
    )