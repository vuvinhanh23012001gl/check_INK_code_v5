# infrastructure/adapters/file_system/file_system_reader.py
import os
import json
import csv
from typing import Any, Dict, List, Optional


class FileSystemReader():
    def read_text(self, file_path: str, encoding: str = 'utf-8') -> Optional[str]:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except Exception:
            return None

    def read_json(self, file_path: str, encoding: str = 'utf-8') -> Optional[Any]:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return json.load(f)
        except Exception:
            return None


    def read_csv(
        self,
        file_path: str,
        has_header: bool = True,
        encoding: str = 'utf-8'
    ) -> Optional[List[Dict[str, Any]]]:
        try:
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                reader = csv.reader(f)
                rows = list(reader)
                if not rows:
                    return []
                data = []
                if has_header:
                    header = rows[0]
                    for row in rows[1:]:
                        data.append(dict(zip(header, row)))
                else:
                    for row in rows:
                        data.append({str(i): value for i, value in enumerate(row)})
                return data
        except Exception:
            return None


    def read_lines(self, file_path: str, encoding: str = 'utf-8') -> Optional[List[str]]:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return [line.rstrip('\n') for line in f.readlines()]
        except Exception:
            return None

    def exists(self, file_path: str) -> bool:
        return os.path.exists(file_path)


    def get_size(self, file_path: str) -> int:
        try:
            return os.path.getsize(file_path)
        except Exception:
            return -1

    def is_empty(self, file_path: str) -> bool:
        size = self.get_size(file_path)
        return size == 0

    def get_extension(self, file_path: str) -> str:
        _, ext = os.path.splitext(file_path)
        return ext