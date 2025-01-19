from typing import List

from etf_screener_backend.defaults.main import REQUIRED_COLUMNS
from etf_screener_backend.defaults.company_tickers import COMPANY_TICKERS


def all_columns_present(columns: List[str]) -> bool:
    """
    Checks if all required columns are present in the given list.
    """
    for col in REQUIRED_COLUMNS:
        if col not in columns:
            return False
    return True


def get_all_tickers() -> dict:
    """
    Returns a dictionary where the keys are tickers and the values are titles of the companies.
    """
    tickers = {}
    for _, item in COMPANY_TICKERS.items():
        tickers[item["ticker"]] = item["title"]
    return tickers
