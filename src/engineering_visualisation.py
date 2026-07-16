import matplotlib.pyplot as plt


def _save_figure(
    figure,
    save_path,
):
    """
    Save a Matplotlib figure when a file path is provided.
    """
    if save_path is not None:
        figure.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )


def plot_beam_deflection(
    position_values,
    deflection_values,
    save_path=None,
):
    """
    Plot the deflection curve of a beam.

    Parameters
    ----------
    position_values : array-like
        Positions along the beam in metres.

    deflection_values : array-like
        Beam deflections in metres.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        position_values,
        deflection_values * 1000.0,
        linewidth=2,
        label="Beam Deflection",
    )

    ax.axhline(
        0.0,
        linewidth=1,
    )

    ax.set_title(
        "Simply Supported Beam Deflection"
    )
    ax.set_xlabel(
        "Beam Position (m)"
    )
    ax.set_ylabel(
        "Downward Deflection (mm)"
    )
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_shear_force_diagram(
    position_values,
    shear_force_values,
    save_path=None,
):
    """
    Plot a beam shear-force diagram.

    Parameters
    ----------
    position_values : array-like
        Positions along the beam in metres.

    shear_force_values : array-like
        Internal shear forces in newtons.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.plot(
        position_values,
        shear_force_values,
        linewidth=2,
        label="Shear Force",
    )

    ax.fill_between(
        position_values,
        shear_force_values,
        0.0,
        alpha=0.2,
    )

    ax.axhline(
        0.0,
        linewidth=1,
    )

    ax.set_title(
        "Shear Force Diagram"
    )
    ax.set_xlabel(
        "Beam Position (m)"
    )
    ax.set_ylabel(
        "Shear Force (N)"
    )
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_bending_moment_diagram(
    position_values,
    bending_moment_values,
    save_path=None,
):
    """
    Plot a beam bending-moment diagram.

    Parameters
    ----------
    position_values : array-like
        Positions along the beam in metres.

    bending_moment_values : array-like
        Internal bending moments in newton-metres.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.plot(
        position_values,
        bending_moment_values,
        linewidth=2,
        label="Bending Moment",
    )

    ax.fill_between(
        position_values,
        bending_moment_values,
        0.0,
        alpha=0.2,
    )

    ax.axhline(
        0.0,
        linewidth=1,
    )

    ax.set_title(
        "Bending Moment Diagram"
    )
    ax.set_xlabel(
        "Beam Position (m)"
    )
    ax.set_ylabel(
        "Bending Moment (N·m)"
    )
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_shaft_stress_distribution(
    radius_values,
    stress_values,
    save_path=None,
):
    """
    Plot torsional shear-stress distribution across a solid shaft.

    Parameters
    ----------
    radius_values : array-like
        Radial positions in metres.

    stress_values : array-like
        Shear stresses in pascals.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.plot(
        radius_values * 1000.0,
        stress_values / 1e6,
        linewidth=2,
        label="Torsional Shear Stress",
    )

    ax.set_title(
        "Shear Stress Distribution in a Solid Circular Shaft"
    )
    ax.set_xlabel(
        "Radius (mm)"
    )
    ax.set_ylabel(
        "Shear Stress (MPa)"
    )
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_buckling_comparison(
    results,
    save_path=None,
):
    """
    Plot Euler critical buckling loads for multiple end conditions.

    Parameters
    ----------
    results : dict
        Mapping of end-condition names to critical loads in newtons.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    condition_names = list(
        results.keys()
    )

    critical_loads_kn = [
        value / 1000.0
        for value in results.values()
    ]

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.bar(
        condition_names,
        critical_loads_kn,
        label="Critical Load",
    )

    ax.set_title(
        "Euler Buckling Critical Load by End Condition"
    )
    ax.set_xlabel(
        "Column End Condition"
    )
    ax.set_ylabel(
        "Critical Load (kN)"
    )
    ax.grid(
        axis="y"
    )

    ax.tick_params(
        axis="x",
        rotation=15,
    )

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_mohrs_circle(
    sigma_values,
    tau_values,
    save_path=None,
):
    """
    Plot Mohr's circle coordinates.

    Parameters
    ----------
    sigma_values : array-like
        Normal-stress coordinates.

    tau_values : array-like
        Shear-stress coordinates.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(7, 7)
    )

    ax.plot(
        sigma_values,
        tau_values,
        linewidth=2,
        label="Mohr's Circle",
    )

    ax.axhline(
        0.0,
        linewidth=1,
    )

    ax.axvline(
        0.0,
        linewidth=1,
    )

    ax.set_title(
        "Mohr's Circle for Plane Stress"
    )
    ax.set_xlabel(
        "Normal Stress (MPa)"
    )
    ax.set_ylabel(
        "Shear Stress (MPa)"
    )
    ax.grid(True)
    ax.axis("equal")
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_failure_criteria_comparison(
    results,
    yield_strength,
    save_path=None,
):
    """
    Compare von Mises and Tresca equivalent stresses against
    the material yield strength.

    Parameters
    ----------
    results : dict
        Results returned by analyse_plane_stress_failure().

    yield_strength : float
        Material yield strength in MPa.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    criteria_names = [
        "Von Mises",
        "Tresca",
    ]

    equivalent_stresses = [
        results["von_mises_stress"],
        results["tresca_equivalent_stress"],
    ]

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

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

    ax.set_title(
        "Ductile Failure Criteria Comparison"
    )
    ax.set_xlabel(
        "Failure Criterion"
    )
    ax.set_ylabel(
        "Stress (MPa)"
    )
    ax.grid(
        axis="y"
    )
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_thermal_resistance_network(
    resistance_names,
    resistance_values,
    save_path=None,
):
    """
    Plot the thermal resistances in a series resistance network.

    Parameters
    ----------
    resistance_names : sequence
        Names of the resistance components.

    resistance_values : sequence
        Resistance values in K/W.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.bar(
        resistance_names,
        resistance_values,
        label="Thermal Resistance",
    )

    ax.set_title(
        "Thermal Resistance Network"
    )
    ax.set_xlabel(
        "Resistance Component"
    )
    ax.set_ylabel(
        "Thermal Resistance (K/W)"
    )
    ax.grid(
        axis="y"
    )

    ax.tick_params(
        axis="x",
        rotation=15,
    )

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_pipe_flow_pressure_loss(
    velocities,
    pressure_losses,
    save_path=None,
):
    """
    Plot Darcy-Weisbach pressure loss against flow velocity.

    Parameters
    ----------
    velocities : array-like
        Flow velocities in m/s.

    pressure_losses : array-like
        Corresponding pressure losses in pascals.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.plot(
        velocities,
        pressure_losses,
        marker="o",
        linewidth=2,
        label="Pressure Loss",
    )

    ax.set_title(
        "Darcy-Weisbach Pressure Loss vs Flow Velocity"
    )
    ax.set_xlabel(
        "Flow Velocity (m/s)"
    )
    ax.set_ylabel(
        "Pressure Loss (Pa)"
    )
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig


def plot_carnot_efficiency_curve(
    hot_temperature_values,
    efficiency_values,
    cold_temperature,
    save_path=None,
):
    """
    Plot Carnot efficiency against hot-reservoir temperature.

    Parameters
    ----------
    hot_temperature_values : array-like
        Hot-reservoir temperatures in kelvin.

    efficiency_values : array-like
        Carnot efficiencies expressed as decimal fractions.

    cold_temperature : float
        Fixed cold-reservoir temperature in kelvin.

    save_path : str or None
        Optional output path for the generated image.

    Returns
    -------
    matplotlib.figure.Figure
        Generated figure.
    """
    efficiency_percentages = [
        efficiency * 100.0
        for efficiency in efficiency_values
    ]

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.plot(
        hot_temperature_values,
        efficiency_percentages,
        linewidth=2,
        label="Carnot Efficiency",
    )

    ax.set_title(
        "Carnot Efficiency vs Hot-Reservoir Temperature"
    )
    ax.set_xlabel(
        "Hot-Reservoir Temperature (K)"
    )
    ax.set_ylabel(
        "Carnot Efficiency (%)"
    )
    ax.grid(True)
    ax.legend()

    ax.text(
        0.02,
        0.95,
        (
            "Cold-reservoir temperature: "
            f"{cold_temperature:.0f} K"
        ),
        transform=ax.transAxes,
        verticalalignment="top",
    )

    fig.tight_layout()

    _save_figure(
        fig,
        save_path,
    )

    plt.show()

    return fig