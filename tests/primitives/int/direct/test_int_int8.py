"""Tests for int_int8 validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_int8 import int_int8
from simplibs.validate.testing import assert_type_contract


def test_int_int8_contract(subtests: pytest.Item) -> None:
    """Verify that int_int8 satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_int8,
        valid_values=[
            -128,
            0,
            127,
        ],
        invalid_values=[
            -129,
            128,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )