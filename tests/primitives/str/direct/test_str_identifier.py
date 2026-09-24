"""Tests for str_identifier validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_identifier import str_identifier
from simplibs.validate.testing import assert_type_contract


def test_str_identifier_contract(subtests: pytest.Item) -> None:
    """Verify that str_identifier satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_identifier,
        valid_values=[
            "foo",
            "_bar",
            "variable_123",
            "MyClass",
        ],
        invalid_values=[
            "",
            "123variable",
            "foo-bar",
            "hello world",
        ],
        expected_error_name="IS_IDENTIFIER_ERROR",
    )