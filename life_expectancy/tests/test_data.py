from unittest.mock import patch, Mock
import pandas as pd

from life_expectancy.data import load_data, save_data

from . import FIXTURES_DIR


def test_load_life_expectancy_data(eu_life_expectancy_raw):
    """Run the `load_data` function and compare the output to the expected output"""

    loaded_data = load_data(FIXTURES_DIR)
    pd.testing.assert_frame_equal(loaded_data, eu_life_expectancy_raw)


@patch("life_expectancy.data.pd.DataFrame.to_csv")
def test_save_pt_life_expectancy_data(to_csv: Mock, pt_life_expectancy_expected):
    """Test the save_data PT function"""
    to_csv.side_effect = lambda *args, **kwargs: print("saving data to CSV")
    save_data(FIXTURES_DIR, "PT", pt_life_expectancy_expected)
    to_csv.assert_called_once_with(FIXTURES_DIR / "pt_life_expectancy.csv", index=False)


@patch("life_expectancy.data.pd.DataFrame.to_csv")
def test_save_eu_life_expectancy_data(to_csv: Mock, eu_life_expectancy_expected):
    """Test the save_data EU function"""
    to_csv.side_effect = lambda *args, **kwargs: print("saving data to CSV")
    save_data(FIXTURES_DIR, "EU", eu_life_expectancy_expected)
    to_csv.assert_called_once_with(FIXTURES_DIR / "eu_life_expectancy.csv", index=False)
