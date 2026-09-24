"""Tests for list_of parametrized validated type."""

import pytest
from simplibs.rules import greater_than
from simplibs.types.collections.list.parametrized.list_of import list_of
from simplibs.validate.testing import assert_type_contract


def test_list_of_contract(subtests: pytest.Item) -> None:
    """Verify that list_of satisfies full type contract & @validate_call integration."""
    positive_int_list = list_of(greater_than(0))

    assert_type_contract(
        subtests,
        type_=positive_int_list,
        valid_values=[
            [],             # Empty list vacuously satisfies for_each
            [1],
            [1, 2, 100],
        ],
        invalid_values=[
            [0],            # Selže prvek 0
            [-1, 2, 3],     # Selže prvek -1
            [1, 2, -5],     # Selže prvek -5
        ],
        expected_error_name="GREATER_THAN_ERROR",
        check_value=False,
    )