import os

from werkzeug.datastructures import FileStorage

class FileManager:

    def __init__(self, file: FileStorage) -> None:
        self.__file = file
        self.__upload_folder = 'src/uploads'


    def verify_existance_on_uploads(self) -> bool:

        file_path = os.path.join(self.__upload_folder, self.__file.filename)

        return os.path.exists(file_path)