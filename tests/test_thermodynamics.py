import pytest

from src.thermodynamics import (
    UNIVERSAL_GAS_CONSTANT,
    analyse_thermodynamic_cycle,
    calculate_boundary_work_constant_pressure,
    calculate_carnot_efficiency,
    calculate_ideal_gas_pressure,
    calculate_ideal_gas_volume,
    calculate_isentropic_exit_temperature,
    calculate_isentropic_temperature_ratio,
    calculate_sensible_heat_transfer,
    calculate_specific_gas_constant,
    calculate_thermal_efficiency,
)


def test_ideal_gas_pressure_known_value():
    result = calculate_ideal_gas_pressure(
        mass=1.0,
        specific_gas_constant=287.0,
        temperature_kelvin=300.0,
        volume=1.0,
    )

    assert result == pytest.approx(
        86100.0
    )


def test_ideal_gas_volume_known_value():
    result = calculate_ideal_gas_volume(
        mass=1.0,
        specific_gas_constant=287.0,
        temperature_kelvin=300.0,
        pressure=86100.0,
    )

    assert result == pytest.approx(1.0)


def test_specific_gas_constant_known_value():
    result = calculate_specific_gas_constant(
        molar_mass=0.02897
    )

    expected = (
        UNIVERSAL_GAS_CONSTANT
        / 0.02897
    )

    assert result == pytest.approx(
        expected
    )


def test_isentropic_temperature_ratio_known_value():
    result = calculate_isentropic_temperature_ratio(
        pressure_ratio=4.0,
        heat_capacity_ratio=1.4,
    )

    expected = 4.0 ** (
        (1.4 - 1.0) / 1.4
    )

    assert result == pytest.approx(
        expected
    )


def test_isentropic_exit_temperature_known_value():
    result = calculate_isentropic_exit_temperature(
        inlet_temperature_kelvin=300.0,
        pressure_ratio=4.0,
        heat_capacity_ratio=1.4,
    )

    expected = (
        300.0
        * 4.0 ** (
            (1.4 - 1.0) / 1.4
        )
    )

    assert result == pytest.approx(
        expected
    )


def test_carnot_efficiency_known_value():
    result = calculate_carnot_efficiency(
        hot_reservoir_temperature_kelvin=600.0,
        cold_reservoir_temperature_kelvin=300.0,
    )

    assert result == pytest.approx(0.5)


def test_thermal_efficiency_known_value():
    result = calculate_thermal_efficiency(
        net_work_output=400.0,
        heat_input=1000.0,
    )

    assert result == pytest.approx(0.4)


def test_constant_pressure_boundary_work_expansion():
    result = (
        calculate_boundary_work_constant_pressure(
            pressure=200000.0,
            initial_volume=0.5,
            final_volume=1.0,
        )
    )

    assert result == pytest.approx(
        100000.0
    )


def test_constant_pressure_boundary_work_compression():
    result = (
        calculate_boundary_work_constant_pressure(
            pressure=200000.0,
            initial_volume=1.0,
            final_volume=0.5,
        )
    )

    assert result == pytest.approx(
        -100000.0
    )


def test_sensible_heat_transfer_known_value():
    result = calculate_sensible_heat_transfer(
        mass=2.0,
        specific_heat_capacity=1000.0,
        initial_temperature=20.0,
        final_temperature=70.0,
    )

    assert result == pytest.approx(
        100000.0
    )


def test_thermodynamic_cycle_known_values():
    results = analyse_thermodynamic_cycle(
        heat_input=1000.0,
        heat_rejected=600.0,
    )

    assert results["net_work_output"] == pytest.approx(
        400.0
    )

    assert results["thermal_efficiency"] == pytest.approx(
        0.4
    )


def test_thermodynamic_cycle_returns_expected_keys():
    results = analyse_thermodynamic_cycle(
        heat_input=1000.0,
        heat_rejected=600.0,
    )

    expected_keys = {
        "heat_input",
        "heat_rejected",
        "net_work_output",
        "thermal_efficiency",
    }

    assert set(results.keys()) == expected_keys


def test_carnot_rejects_cold_temperature_above_hot():
    with pytest.raises(ValueError):
        calculate_carnot_efficiency(
            hot_reservoir_temperature_kelvin=300.0,
            cold_reservoir_temperature_kelvin=400.0,
        )


def test_isentropic_relation_rejects_invalid_gamma():
    with pytest.raises(ValueError):
        calculate_isentropic_temperature_ratio(
            pressure_ratio=4.0,
            heat_capacity_ratio=1.0,
        )


def test_thermal_efficiency_rejects_work_above_heat_input():
    with pytest.raises(ValueError):
        calculate_thermal_efficiency(
            net_work_output=1200.0,
            heat_input=1000.0,
        )


def test_cycle_rejects_heat_rejection_above_input():
    with pytest.raises(ValueError):
        analyse_thermodynamic_cycle(
            heat_input=1000.0,
            heat_rejected=1200.0,
        )