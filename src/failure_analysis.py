import numpy as np

from src.validation import (
    validate_positive_number,
    validate_real_number,
)


def calculate_principal_stresses(
    sigma_x,
    sigma_y,
    tau_xy,
):
    validate_real_number(sigma_x, "sigma_x")
    validate_real_number(sigma_y, "sigma_y")
    validate_real_number(tau_xy, "tau_xy")

    centre = (sigma_x + sigma_y) / 2.0

    radius = np.sqrt(
        ((sigma_x - sigma_y) / 2.0) ** 2
        + tau_xy**2
    )

    sigma_1 = centre + radius
    sigma_2 = centre - radius

    return float(sigma_1), float(sigma_2)


def calculate_von_mises_stress(
    sigma_x,
    sigma_y,
    tau_xy,
):
    validate_real_number(sigma_x, "sigma_x")
    validate_real_number(sigma_y, "sigma_y")
    validate_real_number(tau_xy, "tau_xy")

    return float(
        np.sqrt(
            sigma_x**2
            - sigma_x * sigma_y
            + sigma_y**2
            + 3.0 * tau_xy**2
        )
    )


def calculate_tresca_equivalent_stress(
    sigma_x,
    sigma_y,
    tau_xy,
):
    sigma_1, sigma_2 = calculate_principal_stresses(
        sigma_x,
        sigma_y,
        tau_xy,
    )

    sigma_3 = 0.0

    principal_stresses = [
        sigma_1,
        sigma_2,
        sigma_3,
    ]

    return float(
        max(principal_stresses)
        - min(principal_stresses)
    )


def calculate_factor_of_safety(
    yield_strength,
    equivalent_stress,
):
    validate_positive_number(
        yield_strength,
        "yield_strength",
    )

    validate_positive_number(
        equivalent_stress,
        "equivalent_stress",
    )

    return float(
        yield_strength / equivalent_stress
    )


def analyse_plane_stress_failure(
    sigma_x,
    sigma_y,
    tau_xy,
    yield_strength,
):
    sigma_1, sigma_2 = calculate_principal_stresses(
        sigma_x,
        sigma_y,
        tau_xy,
    )

    von_mises_stress = calculate_von_mises_stress(
        sigma_x,
        sigma_y,
        tau_xy,
    )

    tresca_stress = calculate_tresca_equivalent_stress(
        sigma_x,
        sigma_y,
        tau_xy,
    )

    return {
        "principal_stress_1": sigma_1,
        "principal_stress_2": sigma_2,
        "von_mises_stress": von_mises_stress,
        "tresca_equivalent_stress": tresca_stress,
        "von_mises_factor_of_safety": calculate_factor_of_safety(
            yield_strength,
            von_mises_stress,
        ),
        "tresca_factor_of_safety": calculate_factor_of_safety(
            yield_strength,
            tresca_stress,
        ),
        "von_mises_yielding": von_mises_stress >= yield_strength,
        "tresca_yielding": tresca_stress >= yield_strength,
    }