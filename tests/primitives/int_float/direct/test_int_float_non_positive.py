"""Tests for int_float_non_positive validated type."""

import pytest
from simplibs.types.primitives.int_float.direct.int_float_non_positive import int_float_non_positive
from simplibs.validate.testing import assert_type_contract


def test_int_float_non_positive_contract(subtests: pytest.Item) -> None:
    """Verify that int_float_non_positive satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_float_non_positive,
        valid_values=[
            0,
            -10,
            0.0,
            -42.5,
        ],
        invalid_values=[
            1,
            10,
            0.00001,
            42.5,
        ],
        expected_error_name="LESS_OR_EQUAL_ERROR",
    )