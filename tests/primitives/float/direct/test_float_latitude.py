"""Tests for float_latitude validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_latitude import float_latitude
from simplibs.validate.testing import assert_type_contract


def test_float_latitude_contract(subtests: pytest.Item) -> None:
    """Verify that float_latitude satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_latitude,
        valid_values=[
            -90.0,
            0.0,
            50.0755,
            90.0,
        ],
        invalid_values=[
            -90.0001,
            90.0001,
            -180.0,
            180.0,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )