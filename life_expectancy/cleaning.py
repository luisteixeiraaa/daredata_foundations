import pandas as pd


def clean_data_tsv(life_expectancy: pd.DataFrame) -> pd.DataFrame:
    """ETL process and select data by country tsv specific.

    :return pd.DataFrame: processed dataframe by country.
    """
    life_expectancy = pd.melt(
        life_expectancy,
        id_vars=life_expectancy.columns[0],
        value_vars=life_expectancy.columns[1:],
        var_name="year",
    )
    heads = ["unit", "sex", "age", "region"]
    life_expectancy[heads] = life_expectancy.iloc[:, 0].str.split(
        r"[,\s]+", expand=True
    )
    life_expectancy.drop(columns=life_expectancy.columns[0], axis=1, inplace=True)
    life_expectancy["year"] = life_expectancy["year"].str.extract(r"(\d+)").astype(int)
    life_expectancy["value"] = (
        life_expectancy["value"].str.extract(r"(\d+.\d+)").astype(float)
    )
    life_expectancy = life_expectancy[life_expectancy["value"].notna()]
    life_expectancy = life_expectancy[heads + ["year", "value"]]

    return life_expectancy


def clean_data_json(life_expectancy: pd.DataFrame) -> pd.DataFrame:
    """ETL process and select data by country json specific.

    :return pd.DataFrame: processed dataframe by country.
    """

    heads = ["unit", "sex", "age", "country", "year", "life_expectancy"]
    life_expectancy = life_expectancy[heads].rename(
        columns={"country": "region", "life_expectancy": "value"}
    )
    return life_expectancy
