"""Tests for float_negative validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_negative import float_negative
from simplibs.validate.testing import assert_type_contract


def test_float_negative_contract(subtests: pytest.Item) -> None:
    """Verify that float_negative satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_negative,
        valid_values=[
            -0.00001,
            -1.0,
            -1000.5,
        ],
        invalid_values=[
            0.0,
            0.00001,
            1.0,
        ],
        expected_error_name="LESS_THAN_ERROR",
    )