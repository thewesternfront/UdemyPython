from abc import ABC, abstractmethod

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
