"""Tests for int_float_positive validated type."""

import pytest
from simplibs.types.primitives.int_float.direct.int_float_positive import int_float_positive
from simplibs.validate.testing import assert_type_contract


def test_int_float_positive_contract(subtests: pytest.Item) -> None:
    """Verify that int_float_positive satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_float_positive,
        valid_values=[
            1,
            100,
            0.00001,
            123.45,
        ],
        invalid_values=[
            0,
            0.0,
            -1,
            -123.45,
        ],
        expected_error_name="GREATER_THAN_ERROR",
    )