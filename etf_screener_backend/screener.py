import logging

import pandas as pd

from etf_screener_backend.config.main import Config
from etf_screener_backend.defaults.main import ALL_FILES
from etf_screener_backend.pipeline import Pipeline
from etf_screener_backend.utils.main import all_columns_present


def screener() -> pd.DataFrame:
    """
    Main screening function that processes ETF data from multiple CSV files.

    Returns:
        pd.DataFrame: A pandas DataFrame containing weighted ETF data.
    """

    config = Config(ALL_FILES=ALL_FILES)
    pipeline = Pipeline()

    data = {}
    for file_name, file_path in config.ALL_FILES.items():
        df = pd.read_csv(file_path, index_col=None)
        if all_columns_present(df.columns):
            weights = pipeline.get_percentage_weights(df)
            data[file_name] = weights
        else:
            logging.warning(
                f"Skipping file {file_name} due to missing required columns."
            )
    final_df = pipeline.generate_df(data)

    return final_df
