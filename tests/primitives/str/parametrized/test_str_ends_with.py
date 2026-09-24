"""Tests for str_ends_with parametrized validated type."""

import pytest
from simplibs.types.primitives.str.parametrized.str_ends_with import str_ends_with
from simplibs.validate.testing import assert_type_contract


def test_str_ends_with_contract(subtests: pytest.Item) -> None:
    """Verify that str_ends_with satisfies full type contract & @validate_call integration."""
    pdf_filename = str_ends_with(".pdf")

    assert_type_contract(
        subtests,
        type_=pdf_filename,
        valid_values=[
            ".pdf",
            "document.pdf",
            "my.file.pdf",
        ],
        invalid_values=[
            "",
            "document.pdf.txt",
            "document.PDF",
        ],
        expected_error_name="ENDS_WITH_ERROR",
    )