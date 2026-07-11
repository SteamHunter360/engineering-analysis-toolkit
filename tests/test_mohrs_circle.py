import numpy as np
import pytest

from src.mohrs_circle import (
    calculate_mohrs_circle_parameters,
    generate_mohrs_circle_points,
)


def test_mohrs_circle_known_stress_state():
    results = calculate_mohrs_circle_parameters(
        sigma_x=100.0,
        sigma_y=40.0,
        tau_xy=30.0,
    )

    expected_centre = 70.0
    expected_radius = np.sqrt(
        30.0**2
        + 30.0**2
    )

    assert results["centre"] == pytest.approx(
        expected_centre
    )

    assert results["radius"] == pytest.approx(
        expected_radius
    )

    assert results["principal_stress_1"] == pytest.approx(
        expected_centre + expected_radius
    )

    assert results["principal_stress_2"] == pytest.approx(
        expected_centre - expected_radius
    )


def test_maximum_shear_stress_equals_circle_radius():
    results = calculate_mohrs_circle_parameters(
        sigma_x=80.0,
        sigma_y=20.0,
        tau_xy=25.0,
    )

    assert results["maximum_shear_stress"] == pytest.approx(
        results["radius"]
    )


def test_equal_normal_stresses_with_zero_shear():
    results = calculate_mohrs_circle_parameters(
        sigma_x=50.0,
        sigma_y=50.0,
        tau_xy=0.0,
    )

    assert results["centre"] == pytest.approx(50.0)
    assert results["radius"] == pytest.approx(0.0)
    assert results["principal_stress_1"] == pytest.approx(50.0)
    assert results["principal_stress_2"] == pytest.approx(50.0)


def test_negative_stresses_are_supported():
    results = calculate_mohrs_circle_parameters(
        sigma_x=-100.0,
        sigma_y=-40.0,
        tau_xy=20.0,
    )

    assert results["principal_stress_1"] <= 0.0
    assert results["principal_stress_2"] <= 0.0


def test_generated_circle_has_expected_number_of_points():
    sigma_values, tau_values, _ = (
        generate_mohrs_circle_points(
            sigma_x=100.0,
            sigma_y=40.0,
            tau_xy=30.0,
            number_of_points=200,
        )
    )

    assert len(sigma_values) == 200
    assert len(tau_values) == 200


def test_generated_circle_starts_and_ends_at_same_point():
    sigma_values, tau_values, _ = (
        generate_mohrs_circle_points(
            sigma_x=100.0,
            sigma_y=40.0,
            tau_xy=30.0,
        )
    )

    assert sigma_values[0] == pytest.approx(
        sigma_values[-1]
    )

    assert tau_values[0] == pytest.approx(
        tau_values[-1]
    )


def test_rejects_too_few_circle_points():
    with pytest.raises(ValueError):
        generate_mohrs_circle_points(
            sigma_x=100.0,
            sigma_y=40.0,
            tau_xy=30.0,
            number_of_points=2,
        )


def test_rejects_non_integer_number_of_points():
    with pytest.raises(TypeError):
        generate_mohrs_circle_points(
            sigma_x=100.0,
            sigma_y=40.0,
            tau_xy=30.0,
            number_of_points=100.5,
        )