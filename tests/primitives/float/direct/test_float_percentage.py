"""Tests for float_percentage validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_percentage import float_percentage
from simplibs.validate.testing import assert_type_contract


def test_float_percentage_contract(subtests: pytest.Item) -> None:
    """Verify that float_percentage satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_percentage,
        valid_values=[
            0.0,
            50.0,
            99.9,
            100.0,
        ],
        invalid_values=[
            -0.0001,
            100.0001,
            -15.0,
            150.0,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )