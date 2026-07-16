from src.fluid_mechanics import (
    analyse_pipe_flow,
    calculate_bernoulli_downstream_pressure,
    calculate_hydraulic_power,
)


def main():
    density = 998.0
    velocity = 2.5
    pipe_diameter = 0.05
    dynamic_viscosity = 0.001
    pipe_length = 12.0
    friction_factor = 0.022

    results = analyse_pipe_flow(
        density=density,
        velocity=velocity,
        pipe_diameter=pipe_diameter,
        dynamic_viscosity=dynamic_viscosity,
        pipe_length=pipe_length,
        friction_factor=friction_factor,
    )

    downstream_pressure = (
        calculate_bernoulli_downstream_pressure(
            upstream_pressure=250000.0,
            density=density,
            upstream_velocity=2.0,
            downstream_velocity=3.5,
            upstream_elevation=4.0,
            downstream_elevation=1.0,
        )
    )

    hydraulic_power = calculate_hydraulic_power(
        pressure_difference=results["pressure_loss"],
        volumetric_flow_rate=results[
            "volumetric_flow_rate"
        ],
        efficiency=0.8,
    )

    print("\nFluid Mechanics Analysis Demo")
    print(
        f"Reynolds number: "
        f"{results['reynolds_number']:.2f}"
    )
    print(
        f"Flow regime: "
        f"{results['flow_regime']}"
    )
    print(
        f"Pipe cross-sectional area: "
        f"{results['cross_sectional_area']:.6f} m²"
    )
    print(
        f"Volumetric flow rate: "
        f"{results['volumetric_flow_rate']:.6f} m³/s"
    )
    print(
        f"Darcy-Weisbach head loss: "
        f"{results['head_loss']:.6f} m"
    )
    print(
        f"Darcy-Weisbach pressure loss: "
        f"{results['pressure_loss']:.2f} Pa"
    )
    print(
        f"Bernoulli downstream pressure: "
        f"{downstream_pressure:.2f} Pa"
    )
    print(
        f"Hydraulic power required: "
        f"{hydraulic_power:.2f} W"
    )


if __name__ == "__main__":
    main()