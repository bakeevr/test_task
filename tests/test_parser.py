import sys
import pytest
from unittest.mock import patch
from src.utils.parser import parser


def test_parser():
    test_args = ["main.py", "--files", "file.csv", "--report", "column"]

    with patch.object(sys, "argv", test_args):
        args = parser.parse_args()
        assert args.files == ["file.csv"]
        assert args.avg == "column"


def test_error_no_args():
    with patch.object(sys, "argv", ["main.py"]):
        with pytest.raises(SystemExit):
            parser.parse_args()


def test_many_files():
    test_args = ["main.py", "--files", "f1.csv", "f2.csv", "f3.csv", "--report", "gdp"]

    with patch.object(sys, "argv", test_args):
        args = parser.parse_args()
        assert len(args.files) == 3
        assert "f2.csv" in args.files
