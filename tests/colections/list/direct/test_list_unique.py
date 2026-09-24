"""Tests for list_unique validated type."""

import pytest
from simplibs.types.collections.list.direct.list_unique import list_unique
from simplibs.validate.testing import assert_type_contract


def test_list_unique_contract(subtests: pytest.Item) -> None:
    """Verify that list_unique satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=list_unique,
        valid_values=[
            [],
            [1, 2, 3],
            ["a", "b", "c"],
        ],
        invalid_values=[
            [1, 1],
            ["a", "b", "a"],
            [True, True],
        ],
        expected_error_name="ALL_UNIQUE_ERROR",
    )