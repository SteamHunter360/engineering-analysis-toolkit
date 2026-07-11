import numpy as np

from src.validation import validate_positive_number


def calculate_polar_second_moment(diameter):
    """
    Calculate the polar second moment of area for a solid circular shaft.

    Parameters
    ----------
    diameter : float
        Shaft diameter in metres.

    Returns
    -------
    float
        Polar second moment of area in m^4.
    """
    validate_positive_number(
        diameter,
        "diameter",
    )

    return np.pi * diameter**4 / 32.0


def calculate_torsional_shear_stress(
    torque,
    radius,
    diameter,
):
    """
    Calculate torsional shear stress at a given shaft radius.

    Parameters
    ----------
    torque : float
        Applied torque in N m.

    radius : float
        Radial location from the shaft centre in metres.

    diameter : float
        Shaft diameter in metres.

    Returns
    -------
    float
        Shear stress in Pa.
    """
    validate_positive_number(
        torque,
        "torque",
    )
    validate_positive_number(
        diameter,
        "diameter",
    )

    if radius < 0:
        raise ValueError(
            "radius cannot be negative."
        )

    outer_radius = diameter / 2.0

    if radius > outer_radius:
        raise ValueError(
            "radius cannot exceed the shaft outer radius."
        )

    polar_second_moment = calculate_polar_second_moment(
        diameter
    )

    return (
        torque
        * radius
        / polar_second_moment
    )


def calculate_maximum_torsional_shear_stress(
    torque,
    diameter,
):
    """
    Calculate maximum shear stress at the shaft outer surface.
    """
    validate_positive_number(
        torque,
        "torque",
    )
    validate_positive_number(
        diameter,
        "diameter",
    )

    outer_radius = diameter / 2.0

    return calculate_torsional_shear_stress(
        torque=torque,
        radius=outer_radius,
        diameter=diameter,
    )


def calculate_shaft_stress_distribution(
    torque,
    diameter,
    number_of_points=200,
):
    """
    Calculate radial shear-stress distribution through a solid shaft.

    Returns
    -------
    tuple
        radius values in metres and shear stress values in Pa.
    """
    validate_positive_number(
        torque,
        "torque",
    )
    validate_positive_number(
        diameter,
        "diameter",
    )
    validate_positive_number(
        number_of_points,
        "number_of_points",
    )

    if not isinstance(number_of_points, int):
        raise TypeError(
            "number_of_points must be an integer."
        )

    radius_values = np.linspace(
        0.0,
        diameter / 2.0,
        number_of_points,
    )

    polar_second_moment = calculate_polar_second_moment(
        diameter
    )

    stress_values = (
        torque
        * radius_values
        / polar_second_moment
    )

    return radius_values, stress_values