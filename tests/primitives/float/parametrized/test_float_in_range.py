"""Tests for float_in_range parametrized validated type."""

import pytest
from simplibs.types.primitives.float.parametrized.float_in_range import float_in_range
from simplibs.validate.testing import assert_type_contract


def test_float_in_range_contract(subtests: pytest.Item) -> None:
    """Verify that float_in_range satisfies full type contract & @validate_call integration."""
    unit_range = float_in_range(0.0, 1.0)

    assert_type_contract(
        subtests,
        type_=unit_range,
        valid_values=[
            0.0,         # Inclusive min
            0.5,
            1.0,         # Inclusive max
        ],
        invalid_values=[
            -0.1,        # Less than min
            1.1,         # Greater than max
        ],
        expected_error_name="IN_RANGE_ERROR",
    )