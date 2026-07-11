from src.main import display_menu


def test_display_menu_runs_without_error(capsys):
    display_menu()

    captured = capsys.readouterr()

    assert "Engineering Analysis Toolkit" in captured.out
    assert "Beam Deflection" in captured.out
    assert "Shaft Torsional Stress" in captured.out
    assert "Mohr's Circle" in captured.out
    assert "Euler Buckling" in captured.out