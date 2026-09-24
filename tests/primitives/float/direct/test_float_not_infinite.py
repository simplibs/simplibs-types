"""Tests for float_not_infinite validated type."""

import pytest
from simplibs.types.primitives.float.direct.float_not_infinite import float_not_infinite
from simplibs.validate.testing import assert_type_contract


def test_float_not_infinite_contract(subtests: pytest.Item) -> None:
    """Verify that float_not_infinite satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=float_not_infinite,
        valid_values=[
            0.0,
            1.5,
            -100.25,
        ],
        invalid_values=[
            float("inf"),
            float("-inf"),
        ],
        expected_error_name="NOT_RULE_ERROR",
    )