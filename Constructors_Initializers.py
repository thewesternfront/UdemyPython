from typing import override


class Car:
    def __init__(self, make: str, model: str, year: str):
        self.make = make
        self.model = model
        self.year = year
    #@override
    #def __init__(self, make: str, model: str):
    #    self.make = make
    #    self.model = model

    def drive(self):
        print(f'Now driving {self.make} {self.model} {self.year}')

    def __eq__(self, other):
        #return self.make == other.make and self.model == other.model and self.year == other.year
        # this will compare the dictionary (key value) pair which is a
        # quicker way of doing the above individual comparisons
        return self.__dict__ == other.__dict__


