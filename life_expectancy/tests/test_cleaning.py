"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.cleaning import clean_data


def test_pt_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    country_life_expectancy = clean_data(eu_life_expectancy_raw)
    pt_life_expectancy = country_life_expectancy[
        country_life_expectancy["region"] == "PT"
    ].reset_index(
        drop=True
    )  # pylint: disable=line-too-long

    pd.testing.assert_frame_equal(
        pt_life_expectancy.reset_index(drop=True), pt_life_expectancy_expected
    )
