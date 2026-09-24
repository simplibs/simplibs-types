"""Tests for str_single_line validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_single_line import str_single_line
from simplibs.validate.testing import assert_type_contract


def test_str_single_line_contract(subtests: pytest.Item) -> None:
    """Verify that str_single_line satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_single_line,
        valid_values=[
            "",
            "Hello World",
            "  spaces and \t tabs  ",
        ],
        invalid_values=[
            "hello\nworld",
            "line1\rline2",
            "line1\r\nline2",
        ],
        expected_error_name="REGEX_ERROR",
    )