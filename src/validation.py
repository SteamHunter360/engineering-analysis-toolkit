import math
import numbers


def validate_real_number(value, parameter_name):
    if not isinstance(value, numbers.Real):
        raise TypeError(
            f"{parameter_name} must be a real number."
        )

    if not math.isfinite(value):
        raise ValueError(
            f"{parameter_name} must be finite."
        )


def validate_positive_number(value, parameter_name):
    validate_real_number(
        value,
        parameter_name,
    )

    if value <= 0:
        raise ValueError(
            f"{parameter_name} must be greater than zero."
        )

