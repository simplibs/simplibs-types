"""Tests for float_not_nan validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_not_nan import float_not_nan
from simplibs.validate.testing import assert_type_contract


def test_float_not_nan_contract(subtests: pytest.Item) -> None:
    """Verify that float_not_nan satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_not_nan,
        valid_values=[
            0.0,
            1.5,
            float("inf"),
            float("-inf"),
        ],
        invalid_values=[
            float("nan"),
        ],
        expected_error_name="NOT_RULE_ERROR",
    )