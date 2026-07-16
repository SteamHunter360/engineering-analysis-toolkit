import pytest

from src.heat_transfer import (
    STEFAN_BOLTZMANN_CONSTANT,
    calculate_conduction_resistance,
    calculate_convection_heat_transfer,
    calculate_convection_resistance,
    calculate_heat_transfer_from_resistance,
    calculate_plane_wall_conduction,
    calculate_radiation_heat_transfer,
    calculate_series_thermal_resistance,
)


def test_plane_wall_conduction_known_value():
    result = calculate_plane_wall_conduction(
        thermal_conductivity=10.0,
        area=2.0,
        temperature_hot=100.0,
        temperature_cold=20.0,
        thickness=0.5,
    )

    assert result == pytest.approx(3200.0)


def test_convection_heat_transfer_known_value():
    result = calculate_convection_heat_transfer(
        convection_coefficient=25.0,
        area=2.0,
        surface_temperature=80.0,
        fluid_temperature=20.0,
    )

    assert result == pytest.approx(3000.0)


def test_radiation_heat_transfer_known_value():
    result = calculate_radiation_heat_transfer(
        emissivity=0.8,
        area=1.5,
        surface_temperature_kelvin=500.0,
        surroundings_temperature_kelvin=300.0,
    )

    expected = (
        0.8
        * STEFAN_BOLTZMANN_CONSTANT
        * 1.5
        * (
            500.0**4
            - 300.0**4
        )
    )

    assert result == pytest.approx(expected)


def test_conduction_resistance_known_value():
    result = calculate_conduction_resistance(
        thickness=0.2,
        thermal_conductivity=0.5,
        area=4.0,
    )

    assert result == pytest.approx(0.1)


def test_convection_resistance_known_value():
    result = calculate_convection_resistance(
        convection_coefficient=10.0,
        area=2.0,
    )

    assert result == pytest.approx(0.05)


def test_series_thermal_resistance_known_value():
    result = calculate_series_thermal_resistance(
        [0.1, 0.2, 0.3]
    )

    assert result == pytest.approx(0.6)


def test_heat_transfer_from_resistance_known_value():
    result = calculate_heat_transfer_from_resistance(
        temperature_hot=100.0,
        temperature_cold=20.0,
        total_resistance=0.4,
    )

    assert result == pytest.approx(200.0)


def test_radiation_rejects_emissivity_above_one():
    with pytest.raises(ValueError):
        calculate_radiation_heat_transfer(
            emissivity=1.2,
            area=1.0,
            surface_temperature_kelvin=500.0,
            surroundings_temperature_kelvin=300.0,
        )


def test_radiation_rejects_negative_emissivity():
    with pytest.raises(ValueError):
        calculate_radiation_heat_transfer(
            emissivity=-0.1,
            area=1.0,
            surface_temperature_kelvin=500.0,
            surroundings_temperature_kelvin=300.0,
        )


def test_series_resistance_rejects_empty_sequence():
    with pytest.raises(ValueError):
        calculate_series_thermal_resistance(
            []
        )


def test_plane_wall_conduction_rejects_zero_thickness():
    with pytest.raises(ValueError):
        calculate_plane_wall_conduction(
            thermal_conductivity=10.0,
            area=2.0,
            temperature_hot=100.0,
            temperature_cold=20.0,
            thickness=0.0,
        )