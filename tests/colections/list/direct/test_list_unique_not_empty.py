"""Tests for list_unique_not_empty validated type."""

import pytest
from simplibs.types.collections.list.direct.list_unique_not_empty import list_unique_not_empty
from simplibs.validate.testing import assert_type_contract


def test_list_unique_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that list_unique_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=list_unique_not_empty,
        valid_values=[
            [1],
            [1, 2, 3],
            ["a", "b", "c"],
        ],
        invalid_values=[
            [],       # Fails on NOT_EMPTY
            [1, 1],    # Fails on ALL_UNIQUE
        ],
        expected_error_name=[
            "NOT_EMPTY_ERROR",
            "ALL_UNIQUE_ERROR",
        ],
    )