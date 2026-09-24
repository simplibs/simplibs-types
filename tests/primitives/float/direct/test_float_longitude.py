"""Tests for float_longitude validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_longitude import float_longitude
from simplibs.validate.testing import assert_type_contract


def test_float_longitude_contract(subtests: pytest.Item) -> None:
    """Verify that float_longitude satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_longitude,
        valid_values=[
            -180.0,
            0.0,
            14.4378,
            180.0,
        ],
        invalid_values=[
            -180.0001,
            180.0001,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )