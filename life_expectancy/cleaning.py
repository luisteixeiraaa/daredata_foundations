import pandas as pd
import click

def load_data() -> pd.DataFrame:
    """Load raw data from eu_life_expectancy_raw.tsv file.

    :return pd.DataFrame: return data as dataframe.
    """
    life_expectancy = pd.read_csv('./life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')
    return life_expectancy

def clean_data(country: str, life_expectancy: pd.DataFrame) -> pd.DataFrame:
    """ETL process and select data by country.

    :return pd.DataFrame: processed dataframe by country.
    """
    life_expectancy = pd.melt(life_expectancy, id_vars=life_expectancy.columns[0],
                              value_vars=life_expectancy.columns[1:],
                              var_name="year")
    heads = ['unit', 'sex', 'age', 'region']
    life_expectancy[heads] = life_expectancy.iloc[:, 0].str.split(r'[,\s]+', expand=True)
    life_expectancy.drop(columns=life_expectancy.columns[0], axis=1, inplace=True)
    life_expectancy["year"] = life_expectancy["year"].str.extract(r'(\d+)').astype(int)
    life_expectancy["value"] = life_expectancy["value"].str.extract(r'(\d+.\d+)').astype(float)
    life_expectancy = life_expectancy[life_expectancy["value"].notna()]
    life_expectancy = life_expectancy[heads + ["year", "value"]]

    life_expectancy_country = life_expectancy[life_expectancy["region"] == country]

    return life_expectancy_country


def save_data(country: str, life_expectancy_country: pd.DataFrame) -> None:
    """Save cleaned life expectancy data by country.

    :param str country: cli selected country
    :param pd.DataFrame life_expectancy_country: tranformed dataframe by country.
    """
    life_expectancy_country.to_csv(f"./life_expectancy/data/{country.lower()}_life_expectancy.csv",  # pylint: disable=line-too-long
                                   index=False)


@click.command()
@click.option('--country', '-c', default="PT")
def main(country):
    '''
    Clean data and export country_life_expectancy.
    '''

    country_life_expectancy = load_data()
    country_life_expectancy = clean_data(country, country_life_expectancy)
    save_data(country, country_life_expectancy)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
