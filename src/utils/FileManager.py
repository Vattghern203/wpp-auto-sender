import os

from werkzeug.datastructures import FileStorage

class FileManager:

    def __init__(self, file: FileStorage) -> None:
        self.__file = file
        self.__upload_folder = 'src/uploads'
        self.__file_path = os.path.join(self.__upload_folder, self.__file.filename)


    def verify_existance_on_uploads(self) -> bool:

        return os.path.exists(self.__file_path)
    
    def remove_file(self) -> None:
        
        os.remove(self.__file_path)