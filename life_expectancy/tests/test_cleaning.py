"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import clean_data, load_data, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    country_life_expectancy = load_data()
    country_life_expectancy = clean_data("PT", country_life_expectancy)
    save_data("PT", country_life_expectancy)

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
