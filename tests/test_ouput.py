import pytest

from src.utils.output import output_table


def test_output_table_data(capsys):
    test_data = [(1, "Russia", 2222), (2, "China", 1111)]

    headers = ["", "country", "gdp"]

    output_table(test_data, headers)

    captured = capsys.readouterr()
    output = captured.out

    assert "Russia" in output
    assert "China" in output


def test_output_table_empty(capsys):
    with pytest.raises(SystemExit) as exc_info:
        output_table([], ["H1", "H2"])

    assert exc_info.value.code == -4
