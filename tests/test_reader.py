from unittest.mock import patch

import pytest

from src.utils.reader import read_csv


def test_read_empty(tmp_path: str):
    csv_file = tmp_path / "test.csv"
    csv_content = "country,gdp"
    csv_file.write_text(csv_content)

    result = read_csv(str(csv_file))

    assert result == []


def test_read_content(tmp_path: str):
    csv_file = tmp_path / "test.csv"
    csv_content = "country,gdp\nRussia,2240"
    csv_file.write_text(csv_content)

    result = read_csv(str(csv_file))

    assert result == [{"country": "Russia", "gdp": "2240"}]


def test_read_csv_permission_error():
    with patch("builtins.open", side_effect=PermissionError("Доступ запрещен")):
        with pytest.raises(SystemExit) as exc_info:
            read_csv("test.csv")
        assert exc_info.value.code == -5
