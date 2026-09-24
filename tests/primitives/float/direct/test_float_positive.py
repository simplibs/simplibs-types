"""Tests for float_positive validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_positive import float_positive
from simplibs.validate.testing import assert_type_contract


def test_float_positive_contract(subtests: pytest.Item) -> None:
    """Verify that float_positive satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_positive,
        valid_values=[
            0.00001,
            1.0,
            100.5,
        ],
        invalid_values=[
            0.0,
            -0.00001,
            -1.0,
        ],
        expected_error_name="GREATER_THAN_ERROR",
    )