import numpy as np
import pytest

from src.fluid_mechanics import (
    STANDARD_GRAVITY,
    analyse_pipe_flow,
    calculate_bernoulli_downstream_pressure,
    calculate_darcy_weisbach_head_loss,
    calculate_darcy_weisbach_pressure_loss,
    calculate_hydraulic_power,
    calculate_pipe_cross_sectional_area,
    calculate_reynolds_number,
    calculate_volumetric_flow_rate,
    classify_pipe_flow,
)


def test_reynolds_number_known_value():
    result = calculate_reynolds_number(
        density=1000.0,
        velocity=2.0,
        characteristic_length=0.05,
        dynamic_viscosity=0.001,
    )

    assert result == pytest.approx(
        100000.0
    )


def test_classify_laminar_flow():
    assert classify_pipe_flow(
        1500.0
    ) == "Laminar"


def test_classify_transitional_flow():
    assert classify_pipe_flow(
        3000.0
    ) == "Transitional"


def test_classify_turbulent_flow():
    assert classify_pipe_flow(
        10000.0
    ) == "Turbulent"


def test_bernoulli_equal_velocities_and_elevations():
    result = calculate_bernoulli_downstream_pressure(
        upstream_pressure=200000.0,
        density=1000.0,
        upstream_velocity=2.0,
        downstream_velocity=2.0,
        upstream_elevation=0.0,
        downstream_elevation=0.0,
    )

    assert result == pytest.approx(
        200000.0
    )


def test_bernoulli_pressure_decreases_when_velocity_increases():
    result = calculate_bernoulli_downstream_pressure(
        upstream_pressure=200000.0,
        density=1000.0,
        upstream_velocity=2.0,
        downstream_velocity=4.0,
    )

    expected = (
        200000.0
        + 0.5
        * 1000.0
        * (
            2.0**2
            - 4.0**2
        )
    )

    assert result == pytest.approx(
        expected
    )


def test_darcy_weisbach_head_loss_known_value():
    result = calculate_darcy_weisbach_head_loss(
        friction_factor=0.02,
        pipe_length=10.0,
        pipe_diameter=0.1,
        velocity=2.0,
    )

    expected = (
        0.02
        * (
            10.0 / 0.1
        )
        * (
            2.0**2
            / (
                2.0
                * STANDARD_GRAVITY
            )
        )
    )

    assert result == pytest.approx(
        expected
    )


def test_pressure_loss_matches_head_loss_relation():
    head_loss = calculate_darcy_weisbach_head_loss(
        friction_factor=0.02,
        pipe_length=10.0,
        pipe_diameter=0.1,
        velocity=2.0,
    )

    pressure_loss = calculate_darcy_weisbach_pressure_loss(
        friction_factor=0.02,
        pipe_length=10.0,
        pipe_diameter=0.1,
        density=1000.0,
        velocity=2.0,
    )

    assert pressure_loss == pytest.approx(
        1000.0
        * STANDARD_GRAVITY
        * head_loss
    )


def test_pipe_cross_sectional_area_known_value():
    result = calculate_pipe_cross_sectional_area(
        pipe_diameter=0.1
    )

    expected = (
        np.pi
        * 0.1**2
        / 4.0
    )

    assert result == pytest.approx(
        expected
    )


def test_volumetric_flow_rate_known_value():
    result = calculate_volumetric_flow_rate(
        velocity=2.0,
        cross_sectional_area=0.01,
    )

    assert result == pytest.approx(
        0.02
    )


def test_hydraulic_power_known_value():
    result = calculate_hydraulic_power(
        pressure_difference=200000.0,
        volumetric_flow_rate=0.01,
        efficiency=0.8,
    )

    assert result == pytest.approx(
        2500.0
    )


def test_analyse_pipe_flow_returns_expected_keys():
    results = analyse_pipe_flow(
        density=1000.0,
        velocity=2.0,
        pipe_diameter=0.05,
        dynamic_viscosity=0.001,
        pipe_length=10.0,
        friction_factor=0.02,
    )

    expected_keys = {
        "reynolds_number",
        "flow_regime",
        "cross_sectional_area",
        "volumetric_flow_rate",
        "head_loss",
        "pressure_loss",
    }

    assert set(results.keys()) == expected_keys


def test_reynolds_number_rejects_zero_viscosity():
    with pytest.raises(ValueError):
        calculate_reynolds_number(
            density=1000.0,
            velocity=2.0,
            characteristic_length=0.05,
            dynamic_viscosity=0.0,
        )


def test_head_loss_rejects_zero_pipe_diameter():
    with pytest.raises(ValueError):
        calculate_darcy_weisbach_head_loss(
            friction_factor=0.02,
            pipe_length=10.0,
            pipe_diameter=0.0,
            velocity=2.0,
        )


def test_hydraulic_power_rejects_invalid_efficiency():
    with pytest.raises(ValueError):
        calculate_hydraulic_power(
            pressure_difference=200000.0,
            volumetric_flow_rate=0.01,
            efficiency=1.2,
        )