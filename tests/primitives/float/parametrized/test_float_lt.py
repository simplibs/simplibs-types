"""Tests for float_lt parametrized validated type."""

import pytest
from simplibs.types.primitives.float.parametrized.float_lt import float_lt
from simplibs.validate.testing import assert_type_contract


def test_float_lt_contract(subtests: pytest.Item) -> None:
    """Verify that float_lt satisfies full type contract & @validate_call integration."""
    lt_hundred = float_lt(100.0)

    assert_type_contract(
        subtests,
        type_=lt_hundred,
        valid_values=[
            -10.0,
            0.0,
            99.9,
        ],
        invalid_values=[
            100.0,       # Fails: strictly less than 100.0 required
            100.1,
        ],
        expected_error_name="LESS_THAN_ERROR",
    )