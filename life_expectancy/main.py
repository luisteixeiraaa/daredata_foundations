from pathlib import Path
import click

from life_expectancy.data import load_data, save_data
from life_expectancy.cleaning import clean_data_json, clean_data_tsv
from life_expectancy.region import Region
from life_expectancy.load_strategy import LoadTSV, LoadJSON

DATA_DIR = Path(__file__).parent / "data"


@click.command()
@click.option("--country", "-c", default="EU", type=lambda x: Region[x])
@click.option("--data_format", "-df", default="json")
def main(country, data_format):
    """
    Clean data and export country_life_expectancy.
    """
    if data_format == "json":
        country_life_expectancy = load_data(DATA_DIR, LoadJSON())
        country_life_expectancy = clean_data_json(country_life_expectancy)

    if data_format == "tsv":
        country_life_expectancy = load_data(DATA_DIR, LoadTSV())
        country_life_expectancy = clean_data_tsv(country_life_expectancy)

    save_data(DATA_DIR, country, country_life_expectancy)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
