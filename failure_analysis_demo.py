from src.failure_analysis import analyse_plane_stress_failure


def main():
    sigma_x = 120.0
    sigma_y = 40.0
    tau_xy = 30.0
    yield_strength = 250.0

    results = analyse_plane_stress_failure(
        sigma_x=sigma_x,
        sigma_y=sigma_y,
        tau_xy=tau_xy,
        yield_strength=yield_strength,
    )

    print("\nPlane Stress Failure Analysis")
    print(f"Principal stress 1: {results['principal_stress_1']:.4f} MPa")
    print(f"Principal stress 2: {results['principal_stress_2']:.4f} MPa")
    print(f"Von Mises stress: {results['von_mises_stress']:.4f} MPa")
    print(
        f"Tresca equivalent stress: "
        f"{results['tresca_equivalent_stress']:.4f} MPa"
    )
    print(
        f"Von Mises factor of safety: "
        f"{results['von_mises_factor_of_safety']:.4f}"
    )
    print(
        f"Tresca factor of safety: "
        f"{results['tresca_factor_of_safety']:.4f}"
    )
    print(
        f"Von Mises yielding: "
        f"{results['von_mises_yielding']}"
    )
    print(
        f"Tresca yielding: "
        f"{results['tresca_yielding']}"
    )


if __name__ == "__main__":
    main()