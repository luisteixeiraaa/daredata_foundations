from pathlib import Path
import pandas as pd
from life_expectancy.region import Region
from life_expectancy.load_strategy import LoadStrategy


class DataLoader:
    def __init__(self, strategy: LoadStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: LoadStrategy):
        """Set a different loading strategy as an option."""
        self.strategy = strategy

    def load(self, file_path: Path) -> pd.DataFrame:
        """Delegate loading to the strategy."""
        return self.strategy.load(file_path)


def load_data(
    dir: Path, strategy: LoadStrategy
) -> pd.DataFrame:  # pylint: disable=W0622
    """Set the loading strategy

    :param Path dir: load directory
    :return pd.DataFrame: return data as dataframe.
    """

    loader = DataLoader(strategy)
    return loader.load(dir)


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
