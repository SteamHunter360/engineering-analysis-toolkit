import numpy as np

from src.validation import validate_positive_number


def calculate_centre_point_load_deflection(
    position,
    beam_length,
    point_load,
    youngs_modulus,
    second_moment_area,
):
    """
    Calculate deflection of a simply supported beam carrying
    a point load at midspan.

    Positive values represent downward deflection.

    Parameters
    ----------
    position : float
        Position along the beam in metres.

    beam_length : float
        Beam span in metres.

    point_load : float
        Midspan point load in newtons.

    youngs_modulus : float
        Young's modulus in pascals.

    second_moment_area : float
        Second moment of area in m^4.

    Returns
    -------
    float
        Beam deflection in metres.
    """
    validate_positive_number(
        beam_length,
        "beam_length",
    )
    validate_positive_number(
        point_load,
        "point_load",
    )
    validate_positive_number(
        youngs_modulus,
        "youngs_modulus",
    )
    validate_positive_number(
        second_moment_area,
        "second_moment_area",
    )

    if not isinstance(position, (int, float, np.number)):
        raise TypeError(
            "position must be a real number."
        )

    if position < 0 or position > beam_length:
        raise ValueError(
            "position must lie between 0 and beam_length."
        )

    if position <= beam_length / 2.0:
        distance_from_support = position
    else:
        distance_from_support = (
            beam_length - position
        )

    return (
        point_load
        * distance_from_support
        * (
            3.0 * beam_length**2
            - 4.0 * distance_from_support**2
        )
        / (
            48.0
            * youngs_modulus
            * second_moment_area
        )
    )


def calculate_maximum_centre_point_load_deflection(
    beam_length,
    point_load,
    youngs_modulus,
    second_moment_area,
):
    """
    Calculate maximum midspan deflection.

    Returns
    -------
    float
        Maximum beam deflection in metres.
    """
    validate_positive_number(
        beam_length,
        "beam_length",
    )
    validate_positive_number(
        point_load,
        "point_load",
    )
    validate_positive_number(
        youngs_modulus,
        "youngs_modulus",
    )
    validate_positive_number(
        second_moment_area,
        "second_moment_area",
    )

    return (
        point_load
        * beam_length**3
        / (
            48.0
            * youngs_modulus
            * second_moment_area
        )
    )


def calculate_beam_deflection_curve(
    beam_length,
    point_load,
    youngs_modulus,
    second_moment_area,
    number_of_points=200,
):
    """
    Generate a complete deflection curve for a simply supported
    beam with a centre point load.

    Returns
    -------
    tuple
        Position values in metres and deflection values in metres.
    """
    validate_positive_number(
        beam_length,
        "beam_length",
    )
    validate_positive_number(
        point_load,
        "point_load",
    )
    validate_positive_number(
        youngs_modulus,
        "youngs_modulus",
    )
    validate_positive_number(
        second_moment_area,
        "second_moment_area",
    )

    if not isinstance(number_of_points, int):
        raise TypeError(
            "number_of_points must be an integer."
        )

    if number_of_points < 2:
        raise ValueError(
            "number_of_points must be at least 2."
        )

    position_values = np.linspace(
        0.0,
        beam_length,
        number_of_points,
    )

    deflection_values = np.array(
        [
            calculate_centre_point_load_deflection(
                position=position,
                beam_length=beam_length,
                point_load=point_load,
                youngs_modulus=youngs_modulus,
                second_moment_area=second_moment_area,
            )
            for position in position_values
        ]
    )

    return position_values, deflection_values