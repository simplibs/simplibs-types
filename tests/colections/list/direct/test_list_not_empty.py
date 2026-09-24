"""Tests for list_not_empty validated type."""

import pytest
from simplibs.types.collections.list.direct.list_not_empty import list_not_empty
from simplibs.validate.testing import assert_type_contract


def test_list_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that list_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=list_not_empty,
        valid_values=[
            [1],
            ["a", "b"],
            [True, False, None],
        ],
        invalid_values=[
            [],  # Empty list
        ],
        expected_error_name="NOT_EMPTY_ERROR",
    )