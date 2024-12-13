from pathlib import Path
import pandas as pd
from life_expectancy.region import Region


def load_data(dir: Path) -> pd.DataFrame:  # pylint: disable=W0622
    """Load raw data from eu_life_expectancy_raw.tsv file.

    :param Path dir: load directory
    :return pd.DataFrame: return data as dataframe.
    """
    life_expectancy = pd.read_csv(dir / "eu_life_expectancy_raw.tsv", sep="\t")
    return life_expectancy


def save_data(
    dir: Path, country: Region, life_expectancy: pd.DataFrame
) -> None:  # pylint: disable=W0622
    """Save cleaned life expectancy data by country.

    :param Path dir: save directory
    :param Region country: cli selected country
    :param pd.DataFrame life_expectancy_country: tranformed dataframe by country.
    """
    if country.value == "EU":
        life_expectancy_country = life_expectancy.reset_index(drop=True)
    else:
        life_expectancy_country = life_expectancy[
            life_expectancy["region"] == country.value
        ].reset_index(drop=True)
    life_expectancy_country.to_csv(
        dir
        / f"{country.value.lower()}_life_expectancy.csv",  # pylint: disable=line-too-long
        index=False,
    )
