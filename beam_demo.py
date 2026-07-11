from src.beam_deflection import (
    calculate_beam_deflection_curve,
    calculate_maximum_centre_point_load_deflection,
)
from src.engineering_visualisation import plot_beam_deflection


def main():
    beam_length = 2.0
    point_load = 1000.0
    youngs_modulus = 200e9
    second_moment_area = 8e-6

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

    print("\nBeam Deflection Demo")
    print(f"Beam length: {beam_length:.2f} m")
    print(f"Centre point load: {point_load:.2f} N")
    print(f"Maximum deflection: {maximum_deflection * 1000:.6f} mm")

    plot_beam_deflection(
        position_values,
        deflection_values,
        save_path="images/beam_deflection.png",
    )


if __name__ == "__main__":
    main()