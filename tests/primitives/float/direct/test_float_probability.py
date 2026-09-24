"""Tests for float_probability validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_probability import float_probability
from simplibs.validate.testing import assert_type_contract


def test_float_probability_contract(subtests: pytest.Item) -> None:
    """Verify that float_probability satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_probability,
        valid_values=[
            0.0,
            0.5,
            0.99,
            1.0,
        ],
        invalid_values=[
            -0.0001,
            1.0001,
            -0.5,
            1.5,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )