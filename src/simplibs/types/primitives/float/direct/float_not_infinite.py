from simplibs.validate import validated_type
from simplibs.rules import negate, is_infinity


float_not_infinite = validated_type(float, negate(is_infinity))
"""Validated type for a float that is not +/-infinity.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must not be infinite (negated `is_infinity`).

Detailed description:
    Unlike `float_finite`, this only excludes +/-infinity — NaN is still
    accepted. Use `float_finite` if both NaN and infinity should be
    rejected.

Example:
    @validate_call
    def process(value: float_not_infinite): ...
"""