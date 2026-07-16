from src.heat_transfer import (
    calculate_conduction_resistance,
    calculate_convection_heat_transfer,
    calculate_convection_resistance,
    calculate_heat_transfer_from_resistance,
    calculate_plane_wall_conduction,
    calculate_radiation_heat_transfer,
    calculate_series_thermal_resistance,
)


def main():
    conduction_rate = calculate_plane_wall_conduction(
        thermal_conductivity=1.5,
        area=10.0,
        temperature_hot=80.0,
        temperature_cold=20.0,
        thickness=0.2,
    )

    convection_rate = calculate_convection_heat_transfer(
        convection_coefficient=25.0,
        area=10.0,
        surface_temperature=80.0,
        fluid_temperature=20.0,
    )

    radiation_rate = calculate_radiation_heat_transfer(
        emissivity=0.85,
        area=10.0,
        surface_temperature_kelvin=353.15,
        surroundings_temperature_kelvin=293.15,
    )

    hot_side_convection_resistance = (
        calculate_convection_resistance(
            convection_coefficient=30.0,
            area=10.0,
        )
    )

    wall_resistance = calculate_conduction_resistance(
        thickness=0.2,
        thermal_conductivity=1.5,
        area=10.0,
    )

    cold_side_convection_resistance = (
        calculate_convection_resistance(
            convection_coefficient=15.0,
            area=10.0,
        )
    )

    total_resistance = calculate_series_thermal_resistance(
        [
            hot_side_convection_resistance,
            wall_resistance,
            cold_side_convection_resistance,
        ]
    )

    resistance_heat_rate = (
        calculate_heat_transfer_from_resistance(
            temperature_hot=100.0,
            temperature_cold=20.0,
            total_resistance=total_resistance,
        )
    )

    print("\nHeat Transfer Analysis Demo")
    print(
        f"Plane-wall conduction rate: "
        f"{conduction_rate:.4f} W"
    )
    print(
        f"Convection heat-transfer rate: "
        f"{convection_rate:.4f} W"
    )
    print(
        f"Radiation heat-transfer rate: "
        f"{radiation_rate:.4f} W"
    )
    print(
        f"Total thermal resistance: "
        f"{total_resistance:.6f} K/W"
    )
    print(
        f"Heat rate through resistance network: "
        f"{resistance_heat_rate:.4f} W"
    )


if __name__ == "__main__":
    main()