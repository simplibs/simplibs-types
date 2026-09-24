"""Tests for int_even validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_even import int_even
from simplibs.validate.testing import assert_type_contract


def test_int_even_contract(subtests: pytest.Item) -> None:
    """Verify that int_even satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_even,
        valid_values=[
            0,
            2,
            -2,
            100,
            -100,
        ],
        invalid_values=[
            1,
            -1,
            3,
            99,
        ],
        expected_error_name="IS_EVEN_ERROR",
    )