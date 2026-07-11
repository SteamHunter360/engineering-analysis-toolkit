import numpy as np
import pytest

from src.shaft_stress_analysis import (
    calculate_maximum_torsional_shear_stress,
    calculate_polar_second_moment,
    calculate_shaft_stress_distribution,
    calculate_torsional_shear_stress,
)


def test_calculate_polar_second_moment_known_value():
    diameter = 0.05

    result = calculate_polar_second_moment(
        diameter
    )

    expected = (
        np.pi
        * diameter**4
        / 32.0
    )

    assert result == pytest.approx(expected)


def test_shear_stress_is_zero_at_shaft_centre():
    stress = calculate_torsional_shear_stress(
        torque=500.0,
        radius=0.0,
        diameter=0.05,
    )

    assert stress == pytest.approx(0.0)


def test_maximum_shear_stress_known_value():
    torque = 500.0
    diameter = 0.05

    result = calculate_maximum_torsional_shear_stress(
        torque,
        diameter,
    )

    expected = (
        16.0
        * torque
        / (
            np.pi
            * diameter**3
        )
    )

    assert result == pytest.approx(expected)


def test_stress_distribution_returns_matching_lengths():
    radius_values, stress_values = (
        calculate_shaft_stress_distribution(
            torque=500.0,
            diameter=0.05,
            number_of_points=100,
        )
    )

    assert len(radius_values) == 100
    assert len(stress_values) == 100


def test_stress_distribution_increases_with_radius():
    _, stress_values = (
        calculate_shaft_stress_distribution(
            torque=500.0,
            diameter=0.05,
        )
    )

    assert stress_values[-1] > stress_values[0]


def test_rejects_radius_outside_shaft():
    with pytest.raises(ValueError):
        calculate_torsional_shear_stress(
            torque=500.0,
            radius=0.03,
            diameter=0.05,
        )


def test_rejects_zero_diameter():
    with pytest.raises(ValueError):
        calculate_polar_second_moment(
            0.0
        )