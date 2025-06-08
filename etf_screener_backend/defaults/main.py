import os
import etf_screener_backend

data_root = os.path.join(os.path.dirname(etf_screener_backend.__file__), "../data")

ALL_FILES = {
    "DGRO": os.path.join(data_root, "DGRO.csv"),
    "SCHD": os.path.join(data_root, "SCHD.csv"),
    "SOXX": os.path.join(data_root, "SOXX.csv"),
    "XLK": os.path.join(data_root, "XLK.csv"),
    "FLCOX": os.path.join(data_root, "FLCOX.csv"),
    "FSPGX": os.path.join(data_root, "FSPGX.csv"),
    "SPMO": os.path.join(data_root, "SPMO.csv"),
}


REQUIRED_COLUMNS = ["Name", "Ticker", "Weight(%)"]
