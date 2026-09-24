from simplibs.validate import validated_type
from simplibs.rules import in_range


int_day_of_month = validated_type(int, in_range(1, 31))
"""Validated type for an integer representing a day of the month.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [1, 31].

Detailed description:
    This only enforces the general [1, 31] bound — it does not account
    for month length or leap years (e.g. it accepts 31 even for a month
    that only has 30 days). Combine with additional application-level
    logic if calendar-accurate day validation is required.

Example:
    @validate_call
    def process(value: int_day_of_month): ...
"""