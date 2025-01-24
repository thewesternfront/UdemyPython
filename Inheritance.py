from pydoc import describe
from typing import override


# Base Class
class Animal:
    # class level variable
    version: str

    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping in base')

    @staticmethod
    def greeting():
        print('Hello, from a static method')

    @classmethod
    def printversion(cls):
        cls.version = '2.1.3a'
        print(f'Version: {cls.version}')
        return cls.version


# Sub Class
class Cat(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        #self.name = name
        self.weight = weight

    def meow(self):
        print(f'{self.name} says "meow"')

class Dog(Animal):
    def __init__(self, name: str, job: str):
        super().__init__(name)
        self.job = job

    def dogjob(self):
        print(f'{self.name} performs the job: "{self.job}"')

    @override
    def sleep(self):
        print(f'{self.name} is sleeping in derived class')
        super().sleep()