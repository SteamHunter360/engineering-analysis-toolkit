from src.validation import (
    validate_positive_number,
    validate_real_number,
)


UNIVERSAL_GAS_CONSTANT = 8.314462618


def calculate_ideal_gas_pressure(
    mass,
    specific_gas_constant,
    temperature_kelvin,
    volume,
):
    """
    Calculate ideal-gas pressure using pV = mRT.

    Returns
    -------
    float
        Pressure in pascals.
    """
    validate_positive_number(mass, "mass")
    validate_positive_number(
        specific_gas_constant,
        "specific_gas_constant",
    )
    validate_positive_number(
        temperature_kelvin,
        "temperature_kelvin",
    )
    validate_positive_number(volume, "volume")

    return float(
        mass
        * specific_gas_constant
        * temperature_kelvin
        / volume
    )


def calculate_ideal_gas_volume(
    mass,
    specific_gas_constant,
    temperature_kelvin,
    pressure,
):
    """
    Calculate ideal-gas volume using pV = mRT.
    """
    validate_positive_number(mass, "mass")
    validate_positive_number(
        specific_gas_constant,
        "specific_gas_constant",
    )
    validate_positive_number(
        temperature_kelvin,
        "temperature_kelvin",
    )
    validate_positive_number(pressure, "pressure")

    return float(
        mass
        * specific_gas_constant
        * temperature_kelvin
        / pressure
    )


def calculate_specific_gas_constant(
    molar_mass,
):
    """
    Calculate specific gas constant from molar mass.

    Parameters
    ----------
    molar_mass : float
        Molar mass in kg/mol.
    """
    validate_positive_number(
        molar_mass,
        "molar_mass",
    )

    return float(
        UNIVERSAL_GAS_CONSTANT
        / molar_mass
    )


def calculate_isentropic_temperature_ratio(
    pressure_ratio,
    heat_capacity_ratio,
):
    """
    Calculate T2/T1 for an ideal-gas isentropic process.

    T2/T1 = (p2/p1)^((gamma - 1)/gamma)
    """
    validate_positive_number(
        pressure_ratio,
        "pressure_ratio",
    )
    validate_positive_number(
        heat_capacity_ratio,
        "heat_capacity_ratio",
    )

    if heat_capacity_ratio <= 1.0:
        raise ValueError(
            "heat_capacity_ratio must be greater than 1."
        )

    exponent = (
        heat_capacity_ratio - 1.0
    ) / heat_capacity_ratio

    return float(
        pressure_ratio**exponent
    )


def calculate_isentropic_exit_temperature(
    inlet_temperature_kelvin,
    pressure_ratio,
    heat_capacity_ratio,
):
    """
    Calculate outlet temperature for an ideal isentropic process.
    """
    validate_positive_number(
        inlet_temperature_kelvin,
        "inlet_temperature_kelvin",
    )

    temperature_ratio = (
        calculate_isentropic_temperature_ratio(
            pressure_ratio,
            heat_capacity_ratio,
        )
    )

    return float(
        inlet_temperature_kelvin
        * temperature_ratio
    )


def calculate_carnot_efficiency(
    hot_reservoir_temperature_kelvin,
    cold_reservoir_temperature_kelvin,
):
    """
    Calculate maximum theoretical Carnot efficiency.
    """
    validate_positive_number(
        hot_reservoir_temperature_kelvin,
        "hot_reservoir_temperature_kelvin",
    )
    validate_positive_number(
        cold_reservoir_temperature_kelvin,
        "cold_reservoir_temperature_kelvin",
    )

    if (
        cold_reservoir_temperature_kelvin
        >= hot_reservoir_temperature_kelvin
    ):
        raise ValueError(
            "cold reservoir temperature must be lower than "
            "hot reservoir temperature."
        )

    return float(
        1.0
        - (
            cold_reservoir_temperature_kelvin
            / hot_reservoir_temperature_kelvin
        )
    )


def calculate_thermal_efficiency(
    net_work_output,
    heat_input,
):
    """
    Calculate thermal efficiency from work output and heat input.
    """
    validate_real_number(
        net_work_output,
        "net_work_output",
    )
    validate_positive_number(
        heat_input,
        "heat_input",
    )

    if net_work_output < 0.0:
        raise ValueError(
            "net_work_output cannot be negative."
        )

    if net_work_output > heat_input:
        raise ValueError(
            "net_work_output cannot exceed heat_input."
        )

    return float(
        net_work_output
        / heat_input
    )


def calculate_boundary_work_constant_pressure(
    pressure,
    initial_volume,
    final_volume,
):
    """
    Calculate constant-pressure boundary work.

    Positive work represents expansion.
    """
    validate_positive_number(
        pressure,
        "pressure",
    )
    validate_positive_number(
        initial_volume,
        "initial_volume",
    )
    validate_positive_number(
        final_volume,
        "final_volume",
    )

    return float(
        pressure
        * (
            final_volume
            - initial_volume
        )
    )


def calculate_sensible_heat_transfer(
    mass,
    specific_heat_capacity,
    initial_temperature,
    final_temperature,
):
    """
    Calculate sensible heat transfer: Q = mcΔT.
    """
    validate_positive_number(mass, "mass")
    validate_positive_number(
        specific_heat_capacity,
        "specific_heat_capacity",
    )
    validate_real_number(
        initial_temperature,
        "initial_temperature",
    )
    validate_real_number(
        final_temperature,
        "final_temperature",
    )

    return float(
        mass
        * specific_heat_capacity
        * (
            final_temperature
            - initial_temperature
        )
    )


def analyse_thermodynamic_cycle(
    heat_input,
    heat_rejected,
):
    """
    Perform a compact heat-engine energy analysis.
    """
    validate_positive_number(
        heat_input,
        "heat_input",
    )
    validate_positive_number(
        heat_rejected,
        "heat_rejected",
    )

    if heat_rejected >= heat_input:
        raise ValueError(
            "heat_rejected must be lower than heat_input."
        )

    net_work_output = (
        heat_input
        - heat_rejected
    )

    efficiency = calculate_thermal_efficiency(
        net_work_output,
        heat_input,
    )

    return {
        "heat_input": float(heat_input),
        "heat_rejected": float(
            heat_rejected
        ),
        "net_work_output": float(
            net_work_output
        ),
        "thermal_efficiency": efficiency,
    }