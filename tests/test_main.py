from src.main import display_menu


def test_display_menu_runs_without_error(capsys):
    display_menu()

    captured = capsys.readouterr()

    expected_items = {
        "Engineering Analysis Toolkit",
        "Beam Analysis",
        "Shaft Torsional Stress",
        "Mohr's Circle",
        "Euler Buckling",
        "Failure Criteria",
        "Heat Transfer",
        "Fluid Mechanics",
        "Thermodynamics",
        "Exit",
    }

    for item in expected_items:
        assert item in captured.out