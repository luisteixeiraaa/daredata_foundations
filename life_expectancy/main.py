from pathlib import Path
import click

from life_expectancy.data import load_data, save_data
from life_expectancy.cleaning import clean_data
from life_expectancy.region import Region

DATA_DIR = Path(__file__).parent / "data"


@click.command()
@click.option("--country", "-c", default="EU", type=lambda x: Region[x])
def main(country):
    """
    Clean data and export country_life_expectancy.
    """

    country_life_expectancy = load_data(DATA_DIR)
    country_life_expectancy = clean_data(country_life_expectancy)
    save_data(DATA_DIR, country, country_life_expectancy)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
