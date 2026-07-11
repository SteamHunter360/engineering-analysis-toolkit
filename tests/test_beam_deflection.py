import pytest

from src.beam_deflection import (
    calculate_beam_deflection_curve,
    calculate_centre_point_load_deflection,
    calculate_maximum_centre_point_load_deflection,
    calculate_bending_moment_at_position,
    calculate_centre_point_load_reactions,
    calculate_maximum_bending_moment,
    calculate_shear_force_and_bending_moment_curves,
    calculate_shear_force_at_position,
)


def test_deflection_is_zero_at_left_support():
    deflection = calculate_centre_point_load_deflection(
        position=0.0,
        beam_length=2.0,
        point_load=1000.0,
        youngs_modulus=200e9,
        second_moment_area=8e-6,
    )

    assert deflection == pytest.approx(0.0)


def test_deflection_is_zero_at_right_support():
    deflection = calculate_centre_point_load_deflection(
        position=2.0,
        beam_length=2.0,
        point_load=1000.0,
        youngs_modulus=200e9,
        second_moment_area=8e-6,
    )

    assert deflection == pytest.approx(0.0)


def test_midspan_deflection_matches_closed_form_solution():
    beam_length = 2.0
    point_load = 1000.0
    youngs_modulus = 200e9
    second_moment_area = 8e-6

    result = calculate_centre_point_load_deflection(
        position=beam_length / 2.0,
        beam_length=beam_length,
        point_load=point_load,
        youngs_modulus=youngs_modulus,
        second_moment_area=second_moment_area,
    )

    expected = (
        point_load
        * beam_length**3
        / (
            48.0
            * youngs_modulus
            * second_moment_area
        )
    )

    assert result == pytest.approx(expected)


def test_deflection_curve_is_symmetric():
    position_values, deflection_values = (
        calculate_beam_deflection_curve(
            beam_length=2.0,
            point_load=1000.0,
            youngs_modulus=200e9,
            second_moment_area=8e-6,
            number_of_points=201,
        )
    )

    assert len(position_values) == 201

    for left_value, right_value in zip(
        deflection_values,
        reversed(deflection_values),
    ):
        assert left_value == pytest.approx(
            right_value
        )


def test_maximum_deflection_occurs_at_midspan():
    beam_length = 2.0

    _, deflection_values = (
        calculate_beam_deflection_curve(
            beam_length=beam_length,
            point_load=1000.0,
            youngs_modulus=200e9,
            second_moment_area=8e-6,
            number_of_points=201,
        )
    )

    analytical_maximum = (
        calculate_maximum_centre_point_load_deflection(
            beam_length=beam_length,
            point_load=1000.0,
            youngs_modulus=200e9,
            second_moment_area=8e-6,
        )
    )

    assert max(deflection_values) == pytest.approx(
        analytical_maximum
    )


def test_deflection_curve_returns_matching_lengths():
    position_values, deflection_values = (
        calculate_beam_deflection_curve(
            beam_length=2.0,
            point_load=1000.0,
            youngs_modulus=200e9,
            second_moment_area=8e-6,
            number_of_points=150,
        )
    )

    assert len(position_values) == 150
    assert len(deflection_values) == 150


def test_rejects_position_outside_beam():
    with pytest.raises(ValueError):
        calculate_centre_point_load_deflection(
            position=2.5,
            beam_length=2.0,
            point_load=1000.0,
            youngs_modulus=200e9,
            second_moment_area=8e-6,
        )


def test_rejects_zero_youngs_modulus():
    with pytest.raises(ValueError):
        calculate_beam_deflection_curve(
            beam_length=2.0,
            point_load=1000.0,
            youngs_modulus=0.0,
            second_moment_area=8e-6,
        )


def test_rejects_invalid_number_of_points():
    with pytest.raises(ValueError):
        calculate_beam_deflection_curve(
            beam_length=2.0,
            point_load=1000.0,
            youngs_modulus=200e9,
            second_moment_area=8e-6,
            number_of_points=1,
        )


def test_centre_point_load_reactions_are_equal():
    reaction_left, reaction_right = (
        calculate_centre_point_load_reactions(
            point_load=1000.0
        )
    )

    assert reaction_left == pytest.approx(500.0)
    assert reaction_right == pytest.approx(500.0)


def test_shear_force_changes_sign_across_midspan():
    left_shear = calculate_shear_force_at_position(
        position=0.5,
        beam_length=2.0,
        point_load=1000.0,
    )

    right_shear = calculate_shear_force_at_position(
        position=1.5,
        beam_length=2.0,
        point_load=1000.0,
    )

    assert left_shear == pytest.approx(500.0)
    assert right_shear == pytest.approx(-500.0)


def test_bending_moment_is_zero_at_supports():
    left_moment = calculate_bending_moment_at_position(
        position=0.0,
        beam_length=2.0,
        point_load=1000.0,
    )

    right_moment = calculate_bending_moment_at_position(
        position=2.0,
        beam_length=2.0,
        point_load=1000.0,
    )

    assert left_moment == pytest.approx(0.0)
    assert right_moment == pytest.approx(0.0)


def test_maximum_bending_moment_known_value():
    maximum_moment = calculate_maximum_bending_moment(
        beam_length=2.0,
        point_load=1000.0,
    )

    assert maximum_moment == pytest.approx(500.0)


def test_midspan_bending_moment_matches_maximum():
    midspan_moment = calculate_bending_moment_at_position(
        position=1.0,
        beam_length=2.0,
        point_load=1000.0,
    )

    maximum_moment = calculate_maximum_bending_moment(
        beam_length=2.0,
        point_load=1000.0,
    )

    assert midspan_moment == pytest.approx(
        maximum_moment
    )


def test_force_and_moment_curves_have_matching_lengths():
    (
        position_values,
        shear_force_values,
        bending_moment_values,
    ) = calculate_shear_force_and_bending_moment_curves(
        beam_length=2.0,
        point_load=1000.0,
        number_of_points=201,
    )

    assert len(position_values) == 201
    assert len(shear_force_values) == 201
    assert len(bending_moment_values) == 201