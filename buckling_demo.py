from src.buckling_analysis import compare_end_conditions
from src.engineering_visualisation import plot_buckling_comparison


def main():
    youngs_modulus = 200e9
    second_moment_area = 8e-6
    column_length = 2.0

    results = compare_end_conditions(
        youngs_modulus=youngs_modulus,
        second_moment_area=second_moment_area,
        column_length=column_length,
    )

    print("\nEuler Buckling Demo")

    for condition, load in results.items():
        print(f"{condition}: {load / 1000:.6f} kN")

    plot_buckling_comparison(
        results,
        save_path="images/buckling_analysis.png",
    )


if __name__ == "__main__":
    main()