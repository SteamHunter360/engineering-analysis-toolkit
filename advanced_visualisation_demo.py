import numpy as np

from src.engineering_visualisation import (
    plot_carnot_efficiency_curve,
    plot_failure_criteria_comparison,
    plot_pipe_flow_pressure_loss,
    plot_thermal_resistance_network,
)
from src.failure_analysis import analyse_plane_stress_failure
from src.fluid_mechanics import (
    calculate_darcy_weisbach_pressure_loss,
)
from src.heat_transfer import (
    calculate_conduction_resistance,
    calculate_convection_resistance,
)
from src.thermodynamics import calculate_carnot_efficiency


def main():
    # --------------------------------
    # Failure criteria visualisation
    # --------------------------------
    yield_strength = 250.0

    failure_results = analyse_plane_stress_failure(
        sigma_x=120.0,
        sigma_y=40.0,
        tau_xy=30.0,
        yield_strength=yield_strength,
    )

    plot_failure_criteria_comparison(
        failure_results,
        yield_strength=yield_strength,
        save_path="images/failure_criteria_comparison.png",
    )

    # --------------------------------
    # Thermal resistance visualisation
    # --------------------------------
    hot_convection_resistance = (
        calculate_convection_resistance(
            convection_coefficient=30.0,
            area=10.0,
        )
    )

    wall_resistance = calculate_conduction_resistance(
        thickness=0.2,
        thermal_conductivity=1.5,
        area=10.0,
    )

    cold_convection_resistance = (
        calculate_convection_resistance(
            convection_coefficient=15.0,
            area=10.0,
        )
    )

    plot_thermal_resistance_network(
        resistance_names=[
            "Hot Convection",
            "Wall Conduction",
            "Cold Convection",
        ],
        resistance_values=[
            hot_convection_resistance,
            wall_resistance,
            cold_convection_resistance,
        ],
        save_path="images/thermal_resistance_network.png",
    )

    # --------------------------------
    # Fluid pressure-loss visualisation
    # --------------------------------
    velocities = np.linspace(
        0.5,
        5.0,
        20,
    )

    pressure_losses = [
        calculate_darcy_weisbach_pressure_loss(
            friction_factor=0.022,
            pipe_length=12.0,
            pipe_diameter=0.05,
            density=998.0,
            velocity=velocity,
        )
        for velocity in velocities
    ]

    plot_pipe_flow_pressure_loss(
        velocities,
        pressure_losses,
        save_path="images/pipe_pressure_loss.png",
    )

    # --------------------------------
    # Thermodynamic efficiency plot
    # --------------------------------
    cold_temperature = 300.0

    hot_temperature_values = np.linspace(
        350.0,
        1000.0,
        100,
    )

    efficiency_values = [
        calculate_carnot_efficiency(
            hot_reservoir_temperature_kelvin=temperature,
            cold_reservoir_temperature_kelvin=cold_temperature,
        )
        for temperature in hot_temperature_values
    ]

    plot_carnot_efficiency_curve(
        hot_temperature_values,
        efficiency_values,
        cold_temperature=cold_temperature,
        save_path="images/carnot_efficiency_curve.png",
    )


if __name__ == "__main__":
    main()