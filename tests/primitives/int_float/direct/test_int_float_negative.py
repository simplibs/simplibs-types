"""Tests for int_float_negative validated type."""

import pytest
from simplibs.types.primitives.int_float.direct.int_float_negative import int_float_negative
from simplibs.validate.testing import assert_type_contract


def test_int_float_negative_contract(subtests: pytest.Item) -> None:
    """Verify that int_float_negative satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_float_negative,
        valid_values=[
            -1,
            -100,
            -0.00001,
            -1.5,
        ],
        invalid_values=[
            0,
            0.0,
            1,
            1.5,
        ],
        expected_error_name="LESS_THAN_ERROR",
    )