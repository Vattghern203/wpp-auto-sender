import re

class PhoneNumberCleaner:

    def __init__(self, phone_number: str) -> None:
        self.__phone_number = phone_number
        self.__DDD = '+55'
        self.__DESIRED_LEN = 11
    
    def remove_brackets(self, number: str) -> str:

        return re.sub(r"[\(\)]", "", number)
    
    def validate_number(self, number: str) -> bool:

        number_length = len(number)
        return number_length == self.__DESIRED_LEN
    
    def add_DDD(self, number: str) -> str:

        if self.__DDD not in number:

            return f'{self.__DDD}{number}'
        
        else:

            return number
        
    def clean_number(self) -> str:

        cleaned_number = self.remove_brackets(self.__phone_number)
        
        if self.validate_number(cleaned_number):

            cleaned_number_with_ddd = self.add_DDD(cleaned_number)

            return cleaned_number_with_ddd
        
        else:
            
            raise ValueError(f'The number [{self.__phone_number}] is not valid. Please check for errors.')

# Example usage
phone_number = "(35)998163510"
fake_number = "111111111111111111"

phone_cleaner = PhoneNumberCleaner(phone_number)
cleaned_number = phone_cleaner.clean_number()
print("Cleaned Number:", cleaned_number)

# This will raise an error
# phone_cleaner_fake = PhoneNumberCleaner(fake_number)
# cleaned_fake_number = phone_cleaner_fake.clean_number()
