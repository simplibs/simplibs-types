"""Tests for float_non_negative validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_non_negative import float_non_negative
from simplibs.validate.testing import assert_type_contract


def test_float_non_negative_contract(subtests: pytest.Item) -> None:
    """Verify that float_non_negative satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_non_negative,
        valid_values=[
            0.0,
            0.00001,
            42.0,
        ],
        invalid_values=[
            -0.00001,
            -1.0,
            -100.0,
        ],
        expected_error_name="GREATER_OR_EQUAL_ERROR",
    )