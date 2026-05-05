import os
import json
from typing import Any


class FileSystemWriter():
    def _ensure_directory(self, file_path: str):
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    def write_text(self, file_path: str, data: str, encoding: str = "utf-8"):
        self._ensure_directory(file_path)
        with open(file_path, "w", encoding=encoding) as f:
            f.write(data)


    def write_json(self, file_path: str, data: Any, indent: int = 4):
        self._ensure_directory(file_path)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)


