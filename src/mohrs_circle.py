import numpy as np

from src.validation import validate_real_number


def calculate_mohrs_circle_parameters(
    sigma_x,
    sigma_y,
    tau_xy,
):
    """
    Calculate the key parameters of Mohr's circle for plane stress.

    Parameters
    ----------
    sigma_x : float
        Normal stress in the x-direction.

    sigma_y : float
        Normal stress in the y-direction.

    tau_xy : float
        In-plane shear stress.

    Returns
    -------
    dict
        Mohr's circle centre, radius, principal stresses,
        maximum in-plane shear stress and principal angle.
    """
    validate_real_number(
        sigma_x,
        "sigma_x",
    )
    validate_real_number(
        sigma_y,
        "sigma_y",
    )
    validate_real_number(
        tau_xy,
        "tau_xy",
    )

    centre = (
        sigma_x
        + sigma_y
    ) / 2.0

    radius = np.sqrt(
        (
            (
                sigma_x
                - sigma_y
            ) / 2.0
        ) ** 2
        + tau_xy**2
    )

    principal_stress_1 = centre + radius
    principal_stress_2 = centre - radius

    principal_angle_radians = 0.5 * np.arctan2(
        2.0 * tau_xy,
        sigma_x - sigma_y,
    )

    principal_angle_degrees = np.degrees(
        principal_angle_radians
    )

    return {
        "centre": float(centre),
        "radius": float(radius),
        "principal_stress_1": float(
            principal_stress_1
        ),
        "principal_stress_2": float(
            principal_stress_2
        ),
        "maximum_shear_stress": float(radius),
        "principal_angle_degrees": float(
            principal_angle_degrees
        ),
    }


def generate_mohrs_circle_points(
    sigma_x,
    sigma_y,
    tau_xy,
    number_of_points=300,
):
    """
    Generate normal and shear-stress coordinates for Mohr's circle.

    Returns
    -------
    tuple
        Normal-stress coordinates, shear-stress coordinates,
        and calculated circle parameters.
    """
    if not isinstance(number_of_points, int):
        raise TypeError(
            "number_of_points must be an integer."
        )

    if number_of_points < 3:
        raise ValueError(
            "number_of_points must be at least 3."
        )

    parameters = calculate_mohrs_circle_parameters(
        sigma_x,
        sigma_y,
        tau_xy,
    )

    theta = np.linspace(
        0.0,
        2.0 * np.pi,
        number_of_points,
    )

    normal_stress_values = (
        parameters["centre"]
        + parameters["radius"]
        * np.cos(theta)
    )

    shear_stress_values = (
        parameters["radius"]
        * np.sin(theta)
    )

    return (
        normal_stress_values,
        shear_stress_values,
        parameters,
    )