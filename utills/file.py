import os
from pathlib import Path
import json 


class File:
    @staticmethod
    def create_file_path(file_path: str):
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

    @staticmethod
    def create_json_if_not_exists(file_path):
        file_path = Path(file_path)

        # tạo folder nếu chưa có
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # tạo file nếu chưa tồn tại
        if not file_path.exists():
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=4)

        return file_path
    

    @staticmethod
    def save_json(file_path: str, data):
        """
        ghi đè toàn bộ file json
        """
        file_path = File.create_json_if_not_exists(file_path)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
        )
    @staticmethod
    def read_json(file_path: str, default=None):
        """
        Đọc file json.
        Nếu file chưa có -> tạo file và trả về default.
        Nếu file rỗng / lỗi json -> trả về default.
        """
        if default is None:
            default = {}
        file_path = File.create_json_if_not_exists(file_path)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return default
                return json.loads(content)
        except json.JSONDecodeError:
            return default
        
        
    @staticmethod
    def create_folder(folder_path: str | Path) -> Path:
        """
        Tạo folder nếu chưa tồn tại
        """
        folder_path = Path(folder_path)

        folder_path.mkdir(parents=True, exist_ok=True)

        return folder_path

    @staticmethod
    def exists(path: str | Path) -> bool:
        """
        Kiểm tra path có tồn tại hay không
        """
        return Path(path).exists()