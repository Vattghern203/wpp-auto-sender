import csv
import json

from typing import Union

class ListManager:

    def __init__(self, list_path: str) -> None:
        
        self.__list_path = list_path

    def read_file(self) -> Union[list, dict]:

        try:

            with open(self.__list_path, 'r') as file:

                file_extension = self.__list_path.split('.')[-1].lower()

                if file_extension == 'csv':

                    reader = csv.DictReader(file)

                    data = [row for row in reader]

                    return data
                
                elif file_extension == 'json':

                    data = json.load(file)

                    return data

                else:
                    
                    print(f'Unsuported file type: {file_extension}')

                print(type(data))

                print(data)

                return data

        except Exception as err:

            print(err)
print(ListManager('D:\Biblioteca\Documentos\Códigos\_bots\wpp-auto-sender\sample.csv').read_file())