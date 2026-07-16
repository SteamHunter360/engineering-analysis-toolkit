from src.thermodynamics import (
    analyse_thermodynamic_cycle,
    calculate_boundary_work_constant_pressure,
    calculate_carnot_efficiency,
    calculate_ideal_gas_pressure,
    calculate_isentropic_exit_temperature,
    calculate_sensible_heat_transfer,
)


def main():
    ideal_gas_pressure = (
        calculate_ideal_gas_pressure(
            mass=1.0,
            specific_gas_constant=287.0,
            temperature_kelvin=300.0,
            volume=1.0,
        )
    )

    compressor_exit_temperature = (
        calculate_isentropic_exit_temperature(
            inlet_temperature_kelvin=300.0,
            pressure_ratio=5.0,
            heat_capacity_ratio=1.4,
        )
    )

    carnot_efficiency = (
        calculate_carnot_efficiency(
            hot_reservoir_temperature_kelvin=800.0,
            cold_reservoir_temperature_kelvin=300.0,
        )
    )

    boundary_work = (
        calculate_boundary_work_constant_pressure(
            pressure=200000.0,
            initial_volume=0.4,
            final_volume=0.9,
        )
    )

    sensible_heat = (
        calculate_sensible_heat_transfer(
            mass=2.0,
            specific_heat_capacity=1005.0,
            initial_temperature=300.0,
            final_temperature=450.0,
        )
    )

    cycle_results = (
        analyse_thermodynamic_cycle(
            heat_input=1500.0,
            heat_rejected=900.0,
        )
    )

    print("\nThermodynamics Analysis Demo")
    print(
        f"Ideal-gas pressure: "
        f"{ideal_gas_pressure:.2f} Pa"
    )
    print(
        f"Isentropic exit temperature: "
        f"{compressor_exit_temperature:.2f} K"
    )
    print(
        f"Carnot efficiency: "
        f"{carnot_efficiency * 100:.2f}%"
    )
    print(
        f"Constant-pressure boundary work: "
        f"{boundary_work:.2f} J"
    )
    print(
        f"Sensible heat transfer: "
        f"{sensible_heat:.2f} J"
    )
    print(
        f"Cycle net work output: "
        f"{cycle_results['net_work_output']:.2f} J"
    )
    print(
        f"Cycle thermal efficiency: "
        f"{cycle_results['thermal_efficiency'] * 100:.2f}%"
    )


if __name__ == "__main__":
    main()