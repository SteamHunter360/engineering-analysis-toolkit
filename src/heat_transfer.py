import numpy as np

from src.validation import (
    validate_positive_number,
    validate_real_number,
)


STEFAN_BOLTZMANN_CONSTANT = 5.670374419e-8


def calculate_plane_wall_conduction(
    thermal_conductivity,
    area,
    temperature_hot,
    temperature_cold,
    thickness,
):
    """
    Calculate steady-state heat-transfer rate through a plane wall.

    Parameters
    ----------
    thermal_conductivity : float
        Thermal conductivity in W/(m K).
    area : float
        Heat-transfer area in m^2.
    temperature_hot : float
        Hot-side temperature in degrees Celsius or Kelvin.
    temperature_cold : float
        Cold-side temperature in the same temperature unit.
    thickness : float
        Wall thickness in metres.

    Returns
    -------
    float
        Heat-transfer rate in watts.
    """
    validate_positive_number(
        thermal_conductivity,
        "thermal_conductivity",
    )
    validate_positive_number(
        area,
        "area",
    )
    validate_positive_number(
        thickness,
        "thickness",
    )
    validate_real_number(
        temperature_hot,
        "temperature_hot",
    )
    validate_real_number(
        temperature_cold,
        "temperature_cold",
    )

    return (
        thermal_conductivity
        * area
        * (temperature_hot - temperature_cold)
        / thickness
    )


def calculate_convection_heat_transfer(
    convection_coefficient,
    area,
    surface_temperature,
    fluid_temperature,
):
    """
    Calculate convective heat-transfer rate.

    Returns
    -------
    float
        Heat-transfer rate in watts.
    """
    validate_positive_number(
        convection_coefficient,
        "convection_coefficient",
    )
    validate_positive_number(
        area,
        "area",
    )
    validate_real_number(
        surface_temperature,
        "surface_temperature",
    )
    validate_real_number(
        fluid_temperature,
        "fluid_temperature",
    )

    return (
        convection_coefficient
        * area
        * (surface_temperature - fluid_temperature)
    )


def calculate_radiation_heat_transfer(
    emissivity,
    area,
    surface_temperature_kelvin,
    surroundings_temperature_kelvin,
):
    """
    Calculate net radiative heat-transfer rate.

    Temperatures must be supplied in kelvin.
    """
    validate_positive_number(
        area,
        "area",
    )
    validate_positive_number(
        surface_temperature_kelvin,
        "surface_temperature_kelvin",
    )
    validate_positive_number(
        surroundings_temperature_kelvin,
        "surroundings_temperature_kelvin",
    )
    validate_real_number(
        emissivity,
        "emissivity",
    )

    if emissivity < 0.0 or emissivity > 1.0:
        raise ValueError(
            "emissivity must lie between 0 and 1."
        )

    return (
        emissivity
        * STEFAN_BOLTZMANN_CONSTANT
        * area
        * (
            surface_temperature_kelvin**4
            - surroundings_temperature_kelvin**4
        )
    )


def calculate_conduction_resistance(
    thickness,
    thermal_conductivity,
    area,
):
    """
    Calculate plane-wall conduction thermal resistance in K/W.
    """
    validate_positive_number(
        thickness,
        "thickness",
    )
    validate_positive_number(
        thermal_conductivity,
        "thermal_conductivity",
    )
    validate_positive_number(
        area,
        "area",
    )

    return (
        thickness
        / (
            thermal_conductivity
            * area
        )
    )


def calculate_convection_resistance(
    convection_coefficient,
    area,
):
    """
    Calculate convection thermal resistance in K/W.
    """
    validate_positive_number(
        convection_coefficient,
        "convection_coefficient",
    )
    validate_positive_number(
        area,
        "area",
    )

    return (
        1.0
        / (
            convection_coefficient
            * area
        )
    )


def calculate_series_thermal_resistance(
    resistances,
):
    """
    Calculate total thermal resistance for resistances in series.
    """
    if not isinstance(resistances, (list, tuple, np.ndarray)):
        raise TypeError(
            "resistances must be a sequence."
        )

    if len(resistances) == 0:
        raise ValueError(
            "resistances must not be empty."
        )

    for resistance in resistances:
        validate_positive_number(
            resistance,
            "resistance",
        )

    return float(
        np.sum(resistances)
    )


def calculate_heat_transfer_from_resistance(
    temperature_hot,
    temperature_cold,
    total_resistance,
):
    """
    Calculate heat-transfer rate from a total thermal resistance.
    """
    validate_real_number(
        temperature_hot,
        "temperature_hot",
    )
    validate_real_number(
        temperature_cold,
        "temperature_cold",
    )
    validate_positive_number(
        total_resistance,
        "total_resistance",
    )

    return (
        temperature_hot
        - temperature_cold
    ) / total_resistance