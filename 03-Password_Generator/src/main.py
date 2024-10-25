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
    

if __name__ == '__main__':
    p1 = PinCodeGenerator(length=10)
    print(f'Your password is: {p1.generate()}')