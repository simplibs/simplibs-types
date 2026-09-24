"""Tests for tuple_of parametrized validated type."""

import pytest
from simplibs.rules import greater_than
from simplibs.types.collections.tuple.parametrized.tuple_of import tuple_of
from simplibs.validate.testing import assert_type_contract


def test_tuple_of_contract(subtests: pytest.Item) -> None:
    """Verify that tuple_of satisfies full type contract & @validate_call integration."""
    positive_int_tuple = tuple_of(greater_than(0))

    assert_type_contract(
        subtests,
        type_=positive_int_tuple,
        valid_values=[
            (),             # Empty tuple vacuously satisfies for_each
            (1,),
            (1, 2, 100),
        ],
        invalid_values=[
            (0,),           # 0 is not > 0
            (-1, 2, 3),     # -1 is not > 0
            (1, 2, -5),     # -5 is not > 0
        ],
        expected_error_name="GREATER_THAN_ERROR",
        check_value=False,
    )