import numpy as np

from src.validation import (
    validate_positive_number,
    validate_real_number,
)


STANDARD_GRAVITY = 9.80665


def _validate_non_negative_number(
    value,
    parameter_name,
):
    validate_real_number(
        value,
        parameter_name,
    )

    if value < 0:
        raise ValueError(
            f"{parameter_name} cannot be negative."
        )


def calculate_reynolds_number(
    density,
    velocity,
    characteristic_length,
    dynamic_viscosity,
):
    """
    Calculate Reynolds number.

    Parameters
    ----------
    density : float
        Fluid density in kg/m^3.

    velocity : float
        Mean flow velocity in m/s.

    characteristic_length : float
        Characteristic length, such as pipe diameter, in metres.

    dynamic_viscosity : float
        Dynamic viscosity in Pa s.

    Returns
    -------
    float
        Dimensionless Reynolds number.
    """
    validate_positive_number(
        density,
        "density",
    )
    _validate_non_negative_number(
        velocity,
        "velocity",
    )
    validate_positive_number(
        characteristic_length,
        "characteristic_length",
    )
    validate_positive_number(
        dynamic_viscosity,
        "dynamic_viscosity",
    )

    return float(
        density
        * velocity
        * characteristic_length
        / dynamic_viscosity
    )


def classify_pipe_flow(
    reynolds_number,
):
    """
    Classify internal pipe flow using Reynolds number.

    Returns
    -------
    str
        'Laminar', 'Transitional', or 'Turbulent'.
    """
    _validate_non_negative_number(
        reynolds_number,
        "reynolds_number",
    )

    if reynolds_number < 2300:
        return "Laminar"

    if reynolds_number <= 4000:
        return "Transitional"

    return "Turbulent"


def calculate_bernoulli_downstream_pressure(
    upstream_pressure,
    density,
    upstream_velocity,
    downstream_velocity,
    upstream_elevation=0.0,
    downstream_elevation=0.0,
    gravitational_acceleration=STANDARD_GRAVITY,
):
    """
    Calculate downstream pressure using the ideal Bernoulli equation.

    The calculation assumes steady, incompressible and inviscid flow
    with no pump work, turbine work or head loss.

    Parameters
    ----------
    upstream_pressure : float
        Upstream static pressure in pascals.

    density : float
        Fluid density in kg/m^3.

    upstream_velocity : float
        Upstream mean velocity in m/s.

    downstream_velocity : float
        Downstream mean velocity in m/s.

    upstream_elevation : float
        Upstream elevation in metres.

    downstream_elevation : float
        Downstream elevation in metres.

    gravitational_acceleration : float
        Gravitational acceleration in m/s^2.

    Returns
    -------
    float
        Downstream static pressure in pascals.
    """
    validate_real_number(
        upstream_pressure,
        "upstream_pressure",
    )
    validate_positive_number(
        density,
        "density",
    )
    _validate_non_negative_number(
        upstream_velocity,
        "upstream_velocity",
    )
    _validate_non_negative_number(
        downstream_velocity,
        "downstream_velocity",
    )
    validate_real_number(
        upstream_elevation,
        "upstream_elevation",
    )
    validate_real_number(
        downstream_elevation,
        "downstream_elevation",
    )
    validate_positive_number(
        gravitational_acceleration,
        "gravitational_acceleration",
    )

    dynamic_pressure_change = (
        0.5
        * density
        * (
            upstream_velocity**2
            - downstream_velocity**2
        )
    )

    hydrostatic_pressure_change = (
        density
        * gravitational_acceleration
        * (
            upstream_elevation
            - downstream_elevation
        )
    )

    return float(
        upstream_pressure
        + dynamic_pressure_change
        + hydrostatic_pressure_change
    )


def calculate_darcy_weisbach_head_loss(
    friction_factor,
    pipe_length,
    pipe_diameter,
    velocity,
    gravitational_acceleration=STANDARD_GRAVITY,
):
    """
    Calculate Darcy-Weisbach head loss.

    Returns
    -------
    float
        Head loss in metres of fluid.
    """
    validate_positive_number(
        friction_factor,
        "friction_factor",
    )
    validate_positive_number(
        pipe_length,
        "pipe_length",
    )
    validate_positive_number(
        pipe_diameter,
        "pipe_diameter",
    )
    _validate_non_negative_number(
        velocity,
        "velocity",
    )
    validate_positive_number(
        gravitational_acceleration,
        "gravitational_acceleration",
    )

    return float(
        friction_factor
        * (
            pipe_length
            / pipe_diameter
        )
        * (
            velocity**2
            / (
                2.0
                * gravitational_acceleration
            )
        )
    )


def calculate_darcy_weisbach_pressure_loss(
    friction_factor,
    pipe_length,
    pipe_diameter,
    density,
    velocity,
):
    """
    Calculate Darcy-Weisbach pressure loss.

    Returns
    -------
    float
        Pressure loss in pascals.
    """
    validate_positive_number(
        density,
        "density",
    )

    head_loss = calculate_darcy_weisbach_head_loss(
        friction_factor=friction_factor,
        pipe_length=pipe_length,
        pipe_diameter=pipe_diameter,
        velocity=velocity,
    )

    return float(
        density
        * STANDARD_GRAVITY
        * head_loss
    )


def calculate_volumetric_flow_rate(
    velocity,
    cross_sectional_area,
):
    """
    Calculate volumetric flow rate.

    Returns
    -------
    float
        Volumetric flow rate in m^3/s.
    """
    _validate_non_negative_number(
        velocity,
        "velocity",
    )
    validate_positive_number(
        cross_sectional_area,
        "cross_sectional_area",
    )

    return float(
        velocity
        * cross_sectional_area
    )


def calculate_pipe_cross_sectional_area(
    pipe_diameter,
):
    """
    Calculate circular pipe cross-sectional area.

    Returns
    -------
    float
        Cross-sectional area in m^2.
    """
    validate_positive_number(
        pipe_diameter,
        "pipe_diameter",
    )

    return float(
        np.pi
        * pipe_diameter**2
        / 4.0
    )


def calculate_hydraulic_power(
    pressure_difference,
    volumetric_flow_rate,
    efficiency=1.0,
):
    """
    Calculate required hydraulic input power.

    Parameters
    ----------
    pressure_difference : float
        Pressure rise or pressure requirement in pascals.

    volumetric_flow_rate : float
        Volumetric flow rate in m^3/s.

    efficiency : float
        Pump or system efficiency as a decimal between 0 and 1.

    Returns
    -------
    float
        Required input power in watts.
    """
    _validate_non_negative_number(
        pressure_difference,
        "pressure_difference",
    )
    _validate_non_negative_number(
        volumetric_flow_rate,
        "volumetric_flow_rate",
    )
    validate_real_number(
        efficiency,
        "efficiency",
    )

    if efficiency <= 0.0 or efficiency > 1.0:
        raise ValueError(
            "efficiency must be greater than 0 and no greater than 1."
        )

    return float(
        pressure_difference
        * volumetric_flow_rate
        / efficiency
    )


def analyse_pipe_flow(
    density,
    velocity,
    pipe_diameter,
    dynamic_viscosity,
    pipe_length,
    friction_factor,
):
    """
    Perform a compact pipe-flow analysis.

    Returns
    -------
    dict
        Reynolds number, flow regime, area, flow rate,
        head loss and pressure loss.
    """
    reynolds_number = calculate_reynolds_number(
        density=density,
        velocity=velocity,
        characteristic_length=pipe_diameter,
        dynamic_viscosity=dynamic_viscosity,
    )

    cross_sectional_area = (
        calculate_pipe_cross_sectional_area(
            pipe_diameter
        )
    )

    volumetric_flow_rate = (
        calculate_volumetric_flow_rate(
            velocity=velocity,
            cross_sectional_area=cross_sectional_area,
        )
    )

    head_loss = calculate_darcy_weisbach_head_loss(
        friction_factor=friction_factor,
        pipe_length=pipe_length,
        pipe_diameter=pipe_diameter,
        velocity=velocity,
    )

    pressure_loss = calculate_darcy_weisbach_pressure_loss(
        friction_factor=friction_factor,
        pipe_length=pipe_length,
        pipe_diameter=pipe_diameter,
        density=density,
        velocity=velocity,
    )

    return {
        "reynolds_number": reynolds_number,
        "flow_regime": classify_pipe_flow(
            reynolds_number
        ),
        "cross_sectional_area": cross_sectional_area,
        "volumetric_flow_rate": volumetric_flow_rate,
        "head_loss": head_loss,
        "pressure_loss": pressure_loss,
    }