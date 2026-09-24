"""Tests for str_printable validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_printable import str_printable
from simplibs.validate.testing import assert_type_contract


def test_str_printable_contract(subtests: pytest.Item) -> None:
    """Verify that str_printable satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_printable,
        valid_values=[
            "",
            "Hello World!",
            "1234567890",
            "  spaces  ",
        ],
        invalid_values=[
            "hello\nworld",
            "test\tline",
            "\x00",
        ],
        expected_error_name="IS_PRINTABLE_ERROR",
    )