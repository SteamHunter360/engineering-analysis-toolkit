import numpy as np

from src.validation import validate_positive_number


END_CONDITION_FACTORS = {
    "Pinned-Pinned": 1.0,
    "Fixed-Free": 2.0,
    "Fixed-Pinned": 0.7,
    "Fixed-Fixed": 0.5,
}


def calculate_euler_buckling_load(
    youngs_modulus,
    second_moment_area,
    column_length,
    effective_length_factor=1.0,
):
    validate_positive_number(
        youngs_modulus,
        "youngs_modulus",
    )
    validate_positive_number(
        second_moment_area,
        "second_moment_area",
    )
    validate_positive_number(
        column_length,
        "column_length",
    )
    validate_positive_number(
        effective_length_factor,
        "effective_length_factor",
    )

    effective_length = (
        effective_length_factor * column_length
    )

    return (
        np.pi**2
        * youngs_modulus
        * second_moment_area
        / effective_length**2
    )


def compare_end_conditions(
    youngs_modulus,
    second_moment_area,
    column_length,
):
    return {
        condition: calculate_euler_buckling_load(
            youngs_modulus=youngs_modulus,
            second_moment_area=second_moment_area,
            column_length=column_length,
            effective_length_factor=factor,
        )
        for condition, factor
        in END_CONDITION_FACTORS.items()
    }