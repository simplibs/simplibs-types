"""Tests for set_not_empty validated type."""

import pytest
from simplibs.types.collections.set.direct.set_not_empty import set_not_empty
from simplibs.validate.testing import assert_type_contract


def test_set_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that set_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=set_not_empty,
        valid_values=[
            {1},
            {"a", "b"},
            {True, False},
        ],
        invalid_values=[
            set(),  # Empty set
        ],
        expected_error_name="NOT_EMPTY_ERROR",
    )