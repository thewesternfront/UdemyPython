from abc import ABC, abstractmethod

from fontTools.cffLib import TopDict
from numpy.ma.core import equal


class Phone(ABC):

    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def phone_power(self, power: int):
        ...

    @abstractmethod
    def call_target(self, person: str):
        ...


class TroyPhone(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    def phone_power(self, power: int):
        print(f'Power is at {power}')
        return power

    def call_target(self, person: str):
        print(f'Now calling {person}')
        return person

    def description(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        print(self.model[0])

        if self.model[0] in vowels:
            print(f'This is an {self.model}')
        else:
            print(f'This is a {self.model}')


# TODO:
""" 
https://www.machinelearningplus.com/python/python-property/
Using a @property can help with:

    def description(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        print(self.model[0])

        if self.model[0] in vowels:
            print(f'This is an {self.model}')
        else:
            print(f'This is a {self.model}')

because the description() method can only show info for the 
"model" because that is passed into the base class
but description() cannot access the power and target to be 
called because they exist in methods in the class and would 
not be accessible to the description() method unless their 
values are stored from the other methods into a class variable ....
but with @property, it seems that these would be accessible
as if they are getters and setters ... so I will need to
code a separate project and example using hte link above as
a guide to understanding how this works
"""





