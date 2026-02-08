from unittest.mock import patch

import pytest

from src.utils.avg_calculator import calc_avg


def test_calc_avg_empty():
    data = []
    result = calc_avg(data, "gdp")
    assert result == {}


def test_calc_avg():
    data = [
        {"country": "Russia", "gdp": "2240", "population": "144"},
        {"country": "Russia", "gdp": "2300", "population": "144"},
    ]

    result = calc_avg(data, "gdp")

    assert result == {"Russia": 2270.0}
    assert isinstance(result["Russia"], float)
    assert round(result["Russia"], 2) == 2270.0


def test_calc_avg_key_error():
    data = [
        {"country": "Russia", "gdp": "2240", "population": "144"},
        {"country": "Russia", "gdp": "2300", "population": "144"},
    ]

    with patch("builtins.open", side_effect=KeyError("Неверный ключ")):
        with pytest.raises(SystemExit) as exc_info:
            calc_avg(data, "gd")
        assert exc_info.value.code == -1


def test_calc_avg_value_error():
    data = [
        {"country": "Russia", "gdp": "2240f", "population": "144"},
        {"country": "Russia", "gdp": "2300", "population": "144"},
    ]

    with patch("builtins.open", side_effect=KeyError("Неверные данные")):
        with pytest.raises(SystemExit) as exc_info:
            calc_avg(data, "gdp")
        assert exc_info.value.code == -2
