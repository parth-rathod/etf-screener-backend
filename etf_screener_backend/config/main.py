from typing import Dict
from pydantic import BaseModel, FilePath


class Config(BaseModel):
    ALL_FILES: Dict[str, FilePath]
