from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd


class LoadStrategy(ABC):
    @abstractmethod
    def load(self, file_path: Path) -> pd.DataFrame:
        """Load data from the given file path."""
        pass


class LoadTSV(LoadStrategy):
    def load(self, file_path: Path) -> pd.DataFrame:
        return pd.read_csv(file_path / "eu_life_expectancy_raw.tsv", sep="\t")


class LoadJSON(LoadStrategy):
    def load(self, file_path: Path) -> pd.DataFrame:
        return pd.read_json(file_path / "eurostat_life_expect.json")
