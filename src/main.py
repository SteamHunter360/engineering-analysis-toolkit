from src.beam_deflection import (
    calculate_beam_deflection_curve,
    calculate_maximum_bending_moment,
    calculate_maximum_centre_point_load_deflection,
    calculate_shear_force_and_bending_moment_curves,
)
from src.buckling_analysis import compare_end_conditions
from src.engineering_visualisation import (
    plot_beam_deflection,
    plot_bending_moment_diagram,
    plot_buckling_comparison,
    plot_carnot_efficiency_curve,
    plot_failure_criteria_comparison,
    plot_mohrs_circle,
    plot_pipe_flow_pressure_loss,
    plot_shaft_stress_distribution,
    plot_shear_force_diagram,
    plot_thermal_resistance_network,
)
from src.failure_analysis import analyse_plane_stress_failure
from src.fluid_mechanics import (
    analyse_pipe_flow,
    calculate_darcy_weisbach_pressure_loss,
)
from src.heat_transfer import (
    calculate_conduction_resistance,
    calculate_convection_heat_transfer,
    calculate_convection_resistance,
    calculate_heat_transfer_from_resistance,
    calculate_plane_wall_conduction,
    calculate_radiation_heat_transfer,
    calculate_series_thermal_resistance,
)
from src.mohrs_circle import generate_mohrs_circle_points
from src.shaft_stress_analysis import (
    calculate_maximum_torsional_shear_stress,
    calculate_shaft_stress_distribution,
)
from src.thermodynamics import (
    analyse_thermodynamic_cycle,
    calculate_carnot_efficiency,
    calculate_ideal_gas_pressure,
    calculate_isentropic_exit_temperature,
)

import numpy as np


def run_beam_analysis():
    beam_length = float(input("Beam length, L (m): "))
    point_load = float(input("Centre point load, P (N): "))
    youngs_modulus = float(input("Young's modulus, E (Pa): "))
    second_moment_area = float(
        input("Second moment of area, I (m^4): ")
    )

    position_values, deflection_values = (
        calculate_beam_deflection_curve(
            beam_length=beam_length,
            point_load=point_load,
            youngs_modulus=youngs_modulus,
            second_moment_area=second_moment_area,
            number_of_points=201,
        )
    )

    maximum_deflection = (
        calculate_maximum_centre_point_load_deflection(
            beam_length=beam_length,
            point_load=point_load,
            youngs_modulus=youngs_modulus,
            second_moment_area=second_moment_area,
        )
    )

    (
        force_positions,
        shear_force_values,
        bending_moment_values,
    ) = calculate_shear_force_and_bending_moment_curves(
        beam_length=beam_length,
        point_load=point_load,
        number_of_points=201,
    )

    maximum_moment = calculate_maximum_bending_moment(
        beam_length,
        point_load,
    )

    print(
        f"\nMaximum deflection: "
        f"{maximum_deflection * 1000:.6f} mm"
    )
    print(
        f"Maximum bending moment: "
        f"{maximum_moment:.6f} N·m"
    )

    plot_beam_deflection(
        position_values,
        deflection_values,
        save_path="images/beam_deflection.png",
    )

    plot_shear_force_diagram(
        force_positions,
        shear_force_values,
        save_path="images/shear_force_diagram.png",
    )

    plot_bending_moment_diagram(
        force_positions,
        bending_moment_values,
        save_path="images/bending_moment_diagram.png",
    )


def run_shaft_analysis():
    diameter = float(input("Shaft diameter (m): "))
    torque = float(input("Applied torque (N·m): "))

    radius_values, stress_values = (
        calculate_shaft_stress_distribution(
            torque=torque,
            diameter=diameter,
            number_of_points=200,
        )
    )

    maximum_stress = (
        calculate_maximum_torsional_shear_stress(
            torque=torque,
            diameter=diameter,
        )
    )

    print(
        f"\nMaximum shear stress: "
        f"{maximum_stress / 1e6:.6f} MPa"
    )

    plot_shaft_stress_distribution(
        radius_values,
        stress_values,
        save_path="images/shaft_stress_distribution.png",
    )


def run_mohrs_circle_analysis():
    sigma_x = float(input("Normal stress σx (MPa): "))
    sigma_y = float(input("Normal stress σy (MPa): "))
    tau_xy = float(input("Shear stress τxy (MPa): "))

    sigma_values, tau_values, results = (
        generate_mohrs_circle_points(
            sigma_x=sigma_x,
            sigma_y=sigma_y,
            tau_xy=tau_xy,
            number_of_points=300,
        )
    )

    print(
        f"\nPrincipal stress 1: "
        f"{results['principal_stress_1']:.6f} MPa"
    )
    print(
        f"Principal stress 2: "
        f"{results['principal_stress_2']:.6f} MPa"
    )
    print(
        f"Maximum shear stress: "
        f"{results['maximum_shear_stress']:.6f} MPa"
    )
    print(
        f"Principal angle: "
        f"{results['principal_angle_degrees']:.6f}°"
    )

    plot_mohrs_circle(
        sigma_values,
        tau_values,
        save_path="images/mohrs_circle.png",
    )


def run_buckling_analysis():
    youngs_modulus = float(input("Young's modulus, E (Pa): "))
    second_moment_area = float(
        input("Second moment of area, I (m^4): ")
    )
    column_length = float(input("Column length, L (m): "))

    results = compare_end_conditions(
        youngs_modulus=youngs_modulus,
        second_moment_area=second_moment_area,
        column_length=column_length,
    )

    print("\nEuler buckling critical loads:")

    for condition, load in results.items():
        print(f"{condition}: {load / 1000:.6f} kN")

    plot_buckling_comparison(
        results,
        save_path="images/buckling_analysis.png",
    )


def run_failure_analysis():
    sigma_x = float(input("Normal stress σx (MPa): "))
    sigma_y = float(input("Normal stress σy (MPa): "))
    tau_xy = float(input("Shear stress τxy (MPa): "))
    yield_strength = float(
        input("Material yield strength (MPa): ")
    )

    results = analyse_plane_stress_failure(
        sigma_x=sigma_x,
        sigma_y=sigma_y,
        tau_xy=tau_xy,
        yield_strength=yield_strength,
    )

    print(
        f"\nVon Mises stress: "
        f"{results['von_mises_stress']:.6f} MPa"
    )
    print(
        f"Tresca equivalent stress: "
        f"{results['tresca_equivalent_stress']:.6f} MPa"
    )
    print(
        f"Von Mises factor of safety: "
        f"{results['von_mises_factor_of_safety']:.6f}"
    )
    print(
        f"Tresca factor of safety: "
        f"{results['tresca_factor_of_safety']:.6f}"
    )

    plot_failure_criteria_comparison(
        results,
        yield_strength=yield_strength,
        save_path="images/failure_criteria_comparison.png",
    )


def run_heat_transfer_analysis():
    area = float(input("Heat-transfer area (m²): "))
    thickness = float(input("Wall thickness (m): "))
    thermal_conductivity = float(
        input("Thermal conductivity (W/m·K): ")
    )
    convection_hot = float(
        input("Hot-side convection coefficient (W/m²·K): ")
    )
    convection_cold = float(
        input("Cold-side convection coefficient (W/m²·K): ")
    )
    temperature_hot = float(
        input("Hot-side temperature (°C): ")
    )
    temperature_cold = float(
        input("Cold-side temperature (°C): ")
    )

    conduction_rate = calculate_plane_wall_conduction(
        thermal_conductivity=thermal_conductivity,
        area=area,
        temperature_hot=temperature_hot,
        temperature_cold=temperature_cold,
        thickness=thickness,
    )

    hot_convection_rate = calculate_convection_heat_transfer(
        convection_coefficient=convection_hot,
        area=area,
        surface_temperature=temperature_hot,
        fluid_temperature=temperature_cold,
    )

    radiation_rate = calculate_radiation_heat_transfer(
        emissivity=0.85,
        area=area,
        surface_temperature_kelvin=temperature_hot + 273.15,
        surroundings_temperature_kelvin=temperature_cold + 273.15,
    )

    hot_resistance = calculate_convection_resistance(
        convection_hot,
        area,
    )
    wall_resistance = calculate_conduction_resistance(
        thickness,
        thermal_conductivity,
        area,
    )
    cold_resistance = calculate_convection_resistance(
        convection_cold,
        area,
    )

    total_resistance = calculate_series_thermal_resistance(
        [
            hot_resistance,
            wall_resistance,
            cold_resistance,
        ]
    )

    resistance_heat_rate = (
        calculate_heat_transfer_from_resistance(
            temperature_hot=temperature_hot,
            temperature_cold=temperature_cold,
            total_resistance=total_resistance,
        )
    )

    print(
        f"\nPlane-wall conduction rate: "
        f"{conduction_rate:.6f} W"
    )
    print(
        f"Hot-side convection rate: "
        f"{hot_convection_rate:.6f} W"
    )
    print(
        f"Radiation heat-transfer rate: "
        f"{radiation_rate:.6f} W"
    )
    print(
        f"Total thermal resistance: "
        f"{total_resistance:.6f} K/W"
    )
    print(
        f"Heat rate through resistance network: "
        f"{resistance_heat_rate:.6f} W"
    )

    plot_thermal_resistance_network(
        resistance_names=[
            "Hot Convection",
            "Wall Conduction",
            "Cold Convection",
        ],
        resistance_values=[
            hot_resistance,
            wall_resistance,
            cold_resistance,
        ],
        save_path="images/thermal_resistance_network.png",
    )


def run_fluid_mechanics_analysis():
    density = float(input("Fluid density (kg/m³): "))
    velocity = float(input("Flow velocity (m/s): "))
    pipe_diameter = float(input("Pipe diameter (m): "))
    dynamic_viscosity = float(
        input("Dynamic viscosity (Pa·s): ")
    )
    pipe_length = float(input("Pipe length (m): "))
    friction_factor = float(
        input("Darcy friction factor: ")
    )

    results = analyse_pipe_flow(
        density=density,
        velocity=velocity,
        pipe_diameter=pipe_diameter,
        dynamic_viscosity=dynamic_viscosity,
        pipe_length=pipe_length,
        friction_factor=friction_factor,
    )

    print(
        f"\nReynolds number: "
        f"{results['reynolds_number']:.6f}"
    )
    print(
        f"Flow regime: "
        f"{results['flow_regime']}"
    )
    print(
        f"Volumetric flow rate: "
        f"{results['volumetric_flow_rate']:.6f} m³/s"
    )
    print(
        f"Head loss: "
        f"{results['head_loss']:.6f} m"
    )
    print(
        f"Pressure loss: "
        f"{results['pressure_loss']:.6f} Pa"
    )

    velocity_values = np.linspace(
        0.5,
        max(velocity * 2.0, 1.0),
        20,
    )

    pressure_losses = [
        calculate_darcy_weisbach_pressure_loss(
            friction_factor=friction_factor,
            pipe_length=pipe_length,
            pipe_diameter=pipe_diameter,
            density=density,
            velocity=current_velocity,
        )
        for current_velocity in velocity_values
    ]

    plot_pipe_flow_pressure_loss(
        velocity_values,
        pressure_losses,
        save_path="images/pipe_pressure_loss.png",
    )


def run_thermodynamics_analysis():
    mass = float(input("Gas mass (kg): "))
    gas_constant = float(
        input("Specific gas constant (J/kg·K): ")
    )
    temperature = float(
        input("Gas temperature (K): ")
    )
    volume = float(input("Gas volume (m³): "))

    pressure = calculate_ideal_gas_pressure(
        mass=mass,
        specific_gas_constant=gas_constant,
        temperature_kelvin=temperature,
        volume=volume,
    )

    pressure_ratio = float(
        input("Isentropic pressure ratio p2/p1: ")
    )
    heat_capacity_ratio = float(
        input("Heat-capacity ratio γ: ")
    )

    exit_temperature = (
        calculate_isentropic_exit_temperature(
            inlet_temperature_kelvin=temperature,
            pressure_ratio=pressure_ratio,
            heat_capacity_ratio=heat_capacity_ratio,
        )
    )

    heat_input = float(input("Cycle heat input (J): "))
    heat_rejected = float(
        input("Cycle heat rejected (J): ")
    )

    cycle_results = analyse_thermodynamic_cycle(
        heat_input=heat_input,
        heat_rejected=heat_rejected,
    )

    print(
        f"\nIdeal-gas pressure: "
        f"{pressure:.6f} Pa"
    )
    print(
        f"Isentropic exit temperature: "
        f"{exit_temperature:.6f} K"
    )
    print(
        f"Net work output: "
        f"{cycle_results['net_work_output']:.6f} J"
    )
    print(
        f"Thermal efficiency: "
        f"{cycle_results['thermal_efficiency'] * 100:.6f}%"
    )

    cold_temperature = 300.0

    hot_temperature_values = np.linspace(
        max(cold_temperature + 1.0, 350.0),
        1000.0,
        100,
    )

    efficiency_values = [
        calculate_carnot_efficiency(
            hot_reservoir_temperature_kelvin=value,
            cold_reservoir_temperature_kelvin=cold_temperature,
        )
        for value in hot_temperature_values
    ]

    plot_carnot_efficiency_curve(
        hot_temperature_values,
        efficiency_values,
        cold_temperature=cold_temperature,
        save_path="images/carnot_efficiency_curve.png",
    )


def display_menu():
    print("\n================================")
    print(" Engineering Analysis Toolkit")
    print("================================")
    print("1. Beam Analysis")
    print("2. Shaft Torsional Stress")
    print("3. Mohr's Circle")
    print("4. Euler Buckling")
    print("5. Failure Criteria")
    print("6. Heat Transfer")
    print("7. Fluid Mechanics")
    print("8. Thermodynamics")
    print("9. Exit")


def main():
    analysis_functions = {
        "1": run_beam_analysis,
        "2": run_shaft_analysis,
        "3": run_mohrs_circle_analysis,
        "4": run_buckling_analysis,
        "5": run_failure_analysis,
        "6": run_heat_transfer_analysis,
        "7": run_fluid_mechanics_analysis,
        "8": run_thermodynamics_analysis,
    }

    while True:
        display_menu()

        choice = input("\nSelect module: ").strip()

        if choice == "9":
            print("\nExiting Engineering Analysis Toolkit.")
            break

        selected_function = analysis_functions.get(choice)

        if selected_function is None:
            print("\nInvalid selection. Enter a number from 1 to 9.")
            continue

        try:
            selected_function()
        except (TypeError, ValueError) as error:
            print(f"\nInput error: {error}")


if __name__ == "__main__":
    main()