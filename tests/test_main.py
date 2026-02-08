from unittest.mock import patch, MagicMock

import pytest

from src.main import main


@patch("src.main.parser")
def test_main_with_single_file(mock_parser):
    mock_args = MagicMock()
    mock_args.files = ["gdp.csv"]
    mock_args.avg = "avg_gdp"
    mock_parser.parse_args.return_value = mock_args

    with patch("src.main.read_csv") as mock_read:
        mock_read.return_value = [{"country": "Russia", "gdp": "2240"}]

        with patch("src.main.calc_avg") as mock_calc:
            mock_calc.return_value = {"Russia": 2240.0}

            with patch("src.main.merge_data") as mock_merge:
                mock_merge.return_value = {"Russia": 2240.0}

                with patch("src.main.output_table"):
                    with pytest.raises(SystemExit) as exc_info:
                        main()

                    assert exc_info.value.code == 0
                    mock_read.assert_called_once_with("data/gdp.csv")
                    mock_calc.assert_called_once()
                    mock_merge.assert_called_once()
