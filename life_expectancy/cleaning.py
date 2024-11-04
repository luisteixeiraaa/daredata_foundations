import pandas as pd
import click



def clean_data(country) -> None:
    '''
    Clean data function and export pt_life_expectancy data.
    '''

    life_expectancy = pd.read_csv('./life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')
    life_expectancy = pd.melt(life_expectancy, id_vars=life_expectancy.columns[0],
                              value_vars=life_expectancy.columns[1:-1],
                              var_name="year")
    heads = ['unit', 'sex', 'age', 'region']
    life_expectancy[heads] = life_expectancy.iloc[:, 0].str.split(r'[,\s]+', expand=True)
    life_expectancy.drop(columns=life_expectancy.columns[0], axis=1, inplace=True)
    life_expectancy["year"] = pd.to_numeric(life_expectancy["year"]).astype(int)
    life_expectancy["value"] = life_expectancy["value"].str.extract(r'(\d+.\d+)').astype('float')
    life_expectancy_pt = life_expectancy[life_expectancy["region"] == country]
    life_expectancy_pt.to_csv("./life_expectancy/data/pt_life_expectancy.csv", index=False)


@click.command()
@click.option('--country', '-r', default="PT")
def main(country):
    clean_data(country)


if __name__ == "__main__":  # pragma: no cover
    main()
