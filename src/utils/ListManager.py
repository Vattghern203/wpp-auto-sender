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

                    print(type(data))

                    print(data)

                    return data
                
                elif file_extension == 'json':

                    data = json.load(file)

                    print(type(data))

                    print(data)

                    return data


                else:
                    
                    print(f'Unsuported file type: {file_extension}')

                print(type(data))

                print(data)

                return data

        except Exception as err:

            print(err)
            

list_manager = ListManager('D:/Biblioteca/Downloads/annual-enterprise-survey-2021-financial-year-provisional-csv.csv').read_file()

print('JSON')

manager = ListManager('D:/Biblioteca/Downloads/sample1.json').read_file()