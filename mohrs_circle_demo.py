from src.engineering_visualisation import plot_mohrs_circle
from src.mohrs_circle import generate_mohrs_circle_points


def main():
    sigma_x = 100.0
    sigma_y = 40.0
    tau_xy = 30.0

    sigma_values, tau_values, results = (
        generate_mohrs_circle_points(
            sigma_x=sigma_x,
            sigma_y=sigma_y,
            tau_xy=tau_xy,
            number_of_points=300,
        )
    )

    print("\nMohr's Circle Demo")
    print(f"Principal stress 1: {results['principal_stress_1']:.6f} MPa")
    print(f"Principal stress 2: {results['principal_stress_2']:.6f} MPa")
    print(f"Maximum shear stress: {results['maximum_shear_stress']:.6f} MPa")
    print(f"Principal angle: {results['principal_angle_degrees']:.6f}°")

    plot_mohrs_circle(
        sigma_values,
        tau_values,
        save_path="images/mohrs_circle.png",
    )


if __name__ == "__main__":
    main()