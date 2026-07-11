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