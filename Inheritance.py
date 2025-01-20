from pydoc import describe

# Base Class
class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


# Sub Class
class Cat(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        #self.name = name
        self.weight = weight

    def meow(self):
        print(f'{self.name} says "meow"')
