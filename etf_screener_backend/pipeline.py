import os
from typing import List, Dict

import pandas as pd

import etf_screener_backend
from etf_screener_backend.utils.main import get_all_tickers


class Pipeline:
    """
    A class responsible for preprocessing ETF data and generating ETF lists.

    Attributes:
        all_tickers (Dict): A dictionary containing all available ETF tickers and names.
    """

    def __init__(self):
        self.all_tickers = get_all_tickers()

    def _preprocess_incoming_data(self, df: pd.DataFrame) -> dict:
        """
        Preprocesses incoming ETF data by extracting relevant columns and formatting the weight percentages.

        Args:
            df (pd.DataFrame): Input DataFrame containing ETF data.

        Returns:
            dict: Processed dictionary containing ETF tickers and their corresponding weight percentages.
        """
        final_dict = {}
        keep_columns = ["Ticker", "Weight(%)"]
        new_df = df[keep_columns]
        new_dict = new_df.to_dict(orient="split", index=False)
        for key, value in new_dict.items():
            if key == "data":
                for row in value:
                    final_dict[row[0]] = f"{row[1]:.2f}"

        return final_dict

    def get_percentage_weights(self, df: pd.DataFrame) -> List:
        """
        Generates a list of percentage weights for all ETFs based on the preprocessed data.

        Args:
            df (pd.DataFrame): Input DataFrame containing ETF data.

        Returns:
            List: A list of percentage weights for all ETFs.
        """
        ans = []
        preprocessed_dict = self._preprocess_incoming_data(df)

        for ticker, _ in self.all_tickers.items():
            ans.append(preprocessed_dict.get(ticker, f"{0:.2f}"))

        return ans

    def generate_df(self, weights: Dict) -> pd.DataFrame:
        """
        Creates a DataFrame from the generated weights and saves it as a CSV file.

        Args:
            weights (Dict): A dictionary containing ETF tickers, names, and weights.

        Returns:
            pd.DataFrame: A DataFrame containing ETF information.
        """

        weights["Ticker"] = self.all_tickers.keys()
        weights["Name"] = self.all_tickers.values()

        final_df = pd.DataFrame(weights)

        columns_to_rearange = ["Ticker", "Name"]
        all_columns = final_df.columns.tolist()
        remaining_columns = [
            col for col in all_columns if col not in columns_to_rearange
        ]
        new_order = columns_to_rearange + remaining_columns

        reordered_df = final_df.reindex(columns=new_order)

        data_root = os.path.join(
            os.path.dirname(etf_screener_backend.__file__), "../docs"
        )

        reordered_df.to_csv(os.path.join(data_root, "etfs.csv"), index=False)

        return reordered_df
