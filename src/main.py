from src.beam_deflection import (
    calculate_beam_deflection_curve,
    calculate_maximum_centre_point_load_deflection,
)
from src.buckling_analysis import compare_end_conditions
from src.engineering_visualisation import (
    plot_beam_deflection,
    plot_buckling_comparison,
    plot_mohrs_circle,
    plot_shaft_stress_distribution,
)
from src.mohrs_circle import generate_mohrs_circle_points
from src.shaft_stress_analysis import (
    calculate_maximum_torsional_shear_stress,
    calculate_shaft_stress_distribution,
)


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

    print(
        f"\nMaximum deflection: "
        f"{maximum_deflection * 1000:.6f} mm"
    )

    plot_beam_deflection(
        position_values,
        deflection_values,
        save_path="images/beam_deflection.png",
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


def display_menu():
    print("\n================================")
    print(" Engineering Analysis Toolkit")
    print("================================")
    print("1. Beam Deflection")
    print("2. Shaft Torsional Stress")
    print("3. Mohr's Circle")
    print("4. Euler Buckling")
    print("5. Exit")


def main():
    analysis_functions = {
        "1": run_beam_analysis,
        "2": run_shaft_analysis,
        "3": run_mohrs_circle_analysis,
        "4": run_buckling_analysis,
    }

    while True:
        display_menu()

        choice = input("\nSelect module: ").strip()

        if choice == "5":
            print("\nExiting Engineering Analysis Toolkit.")
            break

        selected_function = analysis_functions.get(choice)

        if selected_function is None:
            print("\nInvalid selection. Enter a number from 1 to 5.")
            continue

        try:
            selected_function()
        except (TypeError, ValueError) as error:
            print(f"\nInput error: {error}")


if __name__ == "__main__":
    main()