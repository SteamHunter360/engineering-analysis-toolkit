import numpy as np
import pytest

from src.buckling_analysis import (
    calculate_euler_buckling_load,
    compare_end_conditions,
)


def test_calculate_euler_buckling_load_known_value():
    load = calculate_euler_buckling_load(
        youngs_modulus=200e9,
        second_moment_area=8e-6,
        column_length=2.0,
        effective_length_factor=1.0,
    )

    expected = (
        np.pi**2
        * 200e9
        * 8e-6
        / 2.0**2
    )

    assert load == pytest.approx(expected)


def test_fixed_fixed_has_highest_critical_load():
    results = compare_end_conditions(
        youngs_modulus=200e9,
        second_moment_area=8e-6,
        column_length=2.0,
    )

    assert results["Fixed-Fixed"] == max(
        results.values()
    )


def test_fixed_free_has_lowest_critical_load():
    results = compare_end_conditions(
        youngs_modulus=200e9,
        second_moment_area=8e-6,
        column_length=2.0,
    )

    assert results["Fixed-Free"] == min(
        results.values()
    )


def test_rejects_zero_column_length():
    with pytest.raises(ValueError):
        calculate_euler_buckling_load(
            youngs_modulus=200e9,
            second_moment_area=8e-6,
            column_length=0,
        )