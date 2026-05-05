import os
class File:
    @staticmethod
    def create_file_path(file_path: str):
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()