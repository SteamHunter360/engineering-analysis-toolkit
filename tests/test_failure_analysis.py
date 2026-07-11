import numpy as np
import pytest

from src.failure_analysis import (
    analyse_plane_stress_failure,
    calculate_factor_of_safety,
    calculate_principal_stresses,
    calculate_tresca_equivalent_stress,
    calculate_von_mises_stress,
)


def test_principal_stresses_for_uniaxial_stress():
    sigma_1, sigma_2 = calculate_principal_stresses(
        sigma_x=100.0,
        sigma_y=0.0,
        tau_xy=0.0,
    )

    assert sigma_1 == pytest.approx(100.0)
    assert sigma_2 == pytest.approx(0.0)


def test_von_mises_for_uniaxial_stress():
    result = calculate_von_mises_stress(
        sigma_x=100.0,
        sigma_y=0.0,
        tau_xy=0.0,
    )

    assert result == pytest.approx(100.0)


def test_von_mises_for_pure_shear():
    result = calculate_von_mises_stress(
        sigma_x=0.0,
        sigma_y=0.0,
        tau_xy=50.0,
    )

    assert result == pytest.approx(
        np.sqrt(3.0) * 50.0
    )


def test_tresca_for_pure_shear():
    result = calculate_tresca_equivalent_stress(
        sigma_x=0.0,
        sigma_y=0.0,
        tau_xy=50.0,
    )

    assert result == pytest.approx(100.0)


def test_factor_of_safety_known_value():
    result = calculate_factor_of_safety(
        yield_strength=250.0,
        equivalent_stress=100.0,
    )

    assert result == pytest.approx(2.5)


def test_failure_analysis_returns_expected_keys():
    results = analyse_plane_stress_failure(
        sigma_x=120.0,
        sigma_y=40.0,
        tau_xy=30.0,
        yield_strength=250.0,
    )

    expected_keys = {
        "principal_stress_1",
        "principal_stress_2",
        "von_mises_stress",
        "tresca_equivalent_stress",
        "von_mises_factor_of_safety",
        "tresca_factor_of_safety",
        "von_mises_yielding",
        "tresca_yielding",
    }

    assert set(results.keys()) == expected_keys


def test_failure_flags_when_stress_exceeds_yield_strength():
    results = analyse_plane_stress_failure(
        sigma_x=300.0,
        sigma_y=0.0,
        tau_xy=0.0,
        yield_strength=250.0,
    )

    assert results["von_mises_yielding"] is True
    assert results["tresca_yielding"] is True


def test_factor_of_safety_rejects_zero_equivalent_stress():
    with pytest.raises(ValueError):
        calculate_factor_of_safety(
            yield_strength=250.0,
            equivalent_stress=0.0,
        )