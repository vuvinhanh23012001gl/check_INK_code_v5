from dataclasses import dataclass
from .path_file_config import PATH_FOLDER_DATA_PRODUCT
@dataclass(frozen=True)
class ProductConfig:
    path:str = PATH_FOLDER_DATA_PRODUCT