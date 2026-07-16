import matplotlib.pyplot as plt


def plot_beam_deflection(
    position_values,
    deflection_values,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        position_values,
        deflection_values * 1000,
        linewidth=2,
    )

    ax.set_title(
        "Beam Deflection"
    )

    ax.set_xlabel(
        "Beam Length (m)"
    )

    ax.set_ylabel(
        "Deflection (mm)"
    )

    ax.grid(True)

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig


def plot_shaft_stress_distribution(
    radius_values,
    stress_values,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        radius_values * 1000,
        stress_values / 1e6,
        linewidth=2,
    )

    ax.set_title(
        "Shaft Shear Stress Distribution"
    )

    ax.set_xlabel(
        "Radius (mm)"
    )

    ax.set_ylabel(
        "Shear Stress (MPa)"
    )

    ax.grid(True)

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig


def plot_buckling_comparison(
    results,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        results.keys(),
        [
            value / 1000
            for value in results.values()
        ],
    )

    ax.set_title(
        "Euler Buckling Critical Loads"
    )

    ax.set_ylabel(
        "Critical Load (kN)"
    )

    ax.grid(axis="y")

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig


def plot_mohrs_circle(
    sigma_values,
    tau_values,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.plot(
        sigma_values,
        tau_values,
        linewidth=2,
    )

    ax.axhline(
        0,
        color="black",
    )

    ax.axvline(
        0,
        color="black",
    )

    ax.set_title(
        "Mohr's Circle"
    )

    ax.set_xlabel(
        "Normal Stress"
    )

    ax.set_ylabel(
        "Shear Stress"
    )

    ax.grid(True)

    ax.axis("equal")

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig

def plot_failure_criteria_comparison(
    results,
    yield_strength,
    save_path=None,
):
    criteria_names = [
        "Von Mises",
        "Tresca",
    ]

    equivalent_stresses = [
        results["von_mises_stress"],
        results["tresca_equivalent_stress"],
    ]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        criteria_names,
        equivalent_stresses,
        label="Equivalent Stress",
    )

    ax.axhline(
        yield_strength,
        linestyle="--",
        linewidth=2,
        label="Yield Strength",
    )

    ax.set_title("Failure Criteria Comparison")
    ax.set_ylabel("Stress (MPa)")
    ax.grid(axis="y")
    ax.legend()

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig


def plot_thermal_resistance_network(
    resistance_names,
    resistance_values,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(
        resistance_names,
        resistance_values,
    )

    ax.set_title("Thermal Resistance Network")
    ax.set_xlabel("Resistance Component")
    ax.set_ylabel("Thermal Resistance (K/W)")
    ax.grid(axis="y")

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig


def plot_pipe_flow_pressure_loss(
    velocities,
    pressure_losses,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        velocities,
        pressure_losses,
        marker="o",
        linewidth=2,
    )

    ax.set_title("Pipe Pressure Loss vs Flow Velocity")
    ax.set_xlabel("Flow Velocity (m/s)")
    ax.set_ylabel("Pressure Loss (Pa)")
    ax.grid(True)

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig


def plot_carnot_efficiency_curve(
    hot_temperature_values,
    efficiency_values,
    cold_temperature,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        hot_temperature_values,
        [
            efficiency * 100.0
            for efficiency in efficiency_values
        ],
        linewidth=2,
    )

    ax.set_title(
        "Carnot Efficiency vs Hot Reservoir Temperature"
    )
    ax.set_xlabel("Hot Reservoir Temperature (K)")
    ax.set_ylabel("Carnot Efficiency (%)")
    ax.grid(True)

    ax.text(
        0.02,
        0.95,
        f"Cold reservoir: {cold_temperature:.0f} K",
        transform=ax.transAxes,
        verticalalignment="top",
    )

    fig.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()

    return fig