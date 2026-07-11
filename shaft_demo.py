from src.engineering_visualisation import (
    plot_shaft_stress_distribution,
)
from src.shaft_stress_analysis import (
    calculate_maximum_torsional_shear_stress,
    calculate_shaft_stress_distribution,
)


def main():
    torque = 500.0
    diameter = 0.05

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

    print("\nShaft Torsional Stress Demo")
    print(f"Torque: {torque:.2f} N·m")
    print(f"Diameter: {diameter * 1000:.2f} mm")
    print(f"Maximum shear stress: {maximum_stress / 1e6:.6f} MPa")

    plot_shaft_stress_distribution(
        radius_values,
        stress_values,
        save_path="images/shaft_stress_distribution.png",
    )


if __name__ == "__main__":
    main()