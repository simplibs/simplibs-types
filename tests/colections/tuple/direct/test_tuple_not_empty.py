"""Tests for tuple_not_empty validated type."""

import pytest
from simplibs.types.collections.tuple.direct.tuple_not_empty import tuple_not_empty
from simplibs.validate.testing import assert_type_contract


def test_tuple_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that tuple_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=tuple_not_empty,
        valid_values=[
            (1,),
            ("a", "b"),
            (True, False, None),
        ],
        invalid_values=[
            (),  # Empty tuple
        ],
        expected_error_name="NOT_EMPTY_ERROR",
    )