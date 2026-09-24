"""Tests for int_port validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_port import int_port
from simplibs.validate.testing import assert_type_contract


def test_int_port_contract(subtests: pytest.Item) -> None:
    """Verify that int_port satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_port,
        valid_values=[
            0,
            80,
            443,
            8080,
            65535,
        ],
        invalid_values=[
            -1,
            65536,
            100000,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )