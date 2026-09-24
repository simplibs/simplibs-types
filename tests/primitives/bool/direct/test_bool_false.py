"""Tests for bool_false validated type."""

import pytest
from simplibs.types.primitives.bool.direct.bool_false import bool_false
from simplibs.validate.testing import assert_type_contract


def test_bool_false_contract(subtests: pytest.Item) -> None:
    """Verify that bool_false satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=bool_false,
        valid_values=[
            False,
        ],
        invalid_values=[
            True,
        ],
        expected_error_name="IS_FALSE_ERROR",
    )