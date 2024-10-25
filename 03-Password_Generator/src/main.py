import random
import string
from abc import ABC, abstractmethod


class PasswordGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass


class PinCodeGenerator(PasswordGenerator):
    """Class to generate a pin code
    """    
    def __init__(self, length: int=8) -> None:
        self.length = length

    def generate(self) -> str:
        """Method to generate a pin code

        :return: pin code
        """
        return ''.join(random.choice(string.digits) for i in range(self.length))
    

class RandomPasswordGenerator(PasswordGenerator):
    """Class to generate a random password
    """
    def __init__(
        self, 
        length: int=8, 
        include_numbers: bool=False, 
        include_symbols: bool=False
        ) -> None:
        
        self.length = length
        self.charcters = string.ascii_letters
        if include_numbers:
            self.charcters += string.digits
        if include_symbols:
            self.charcters += string.punctuation

    def generate(self) -> str:
        """Method to generate a password

        :return: random password
        """
        return ''.join(random.choice(self.charcters) for i in range(self.length))
    

if __name__ == '__main__':
    p1 = PinCodeGenerator(length=10)
    print(f'Your password is: {p1.generate()}')

    p2 = RandomPasswordGenerator(
        length=16, 
        include_numbers=True, 
        include_symbols=True
        )
    print(f'Your password is: {p2.generate()}')