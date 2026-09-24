"""Tests for bool_true validated type."""

import pytest
from simplibs.types.primitives.bool.direct.bool_true import bool_true
from simplibs.validate.testing import assert_type_contract


def test_bool_true_contract(subtests: pytest.Item) -> None:
    """Verify that bool_true satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=bool_true,
        valid_values=[
            True,
        ],
        invalid_values=[
            False,
        ],
        expected_error_name="IS_TRUE_ERROR",
    )