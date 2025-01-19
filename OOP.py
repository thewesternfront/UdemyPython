# For OOP, Classes, etc.
class Lamp:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def turn_on(self):
        print(self.model + " is turned on")

    def turn_off(self):
        print(self.model + " is turned off")

    def describe(self):
        print(f'Lamp: {self.model} {self.color}')


class Fruits:
    def __init__(self):
        print("Fruits Class")

    # getters and setters for name of fruit
    def set_name(self, name: str):
        self.name = name
    def get_name(self):
        return self.name

    # getters and setters for colour of fruit
    def set_color(self, color: str):
        self.color = color
    def get_color(self) -> str:
        return self.color

    def describe(self):
        print(f'Fruits: {self.name} {self.color}')


class Fruit:
    def __init__(self, name: str, color: str):
        # This indicates private variables that can only be accessed
        # through 'getters' and 'setters'
        self._name = name
        self._color = color
        print(f'Fruit Class Initializer {self._name}, of color {self._color}')

        # getter
        @property
        def name(self):
            print(f'Accessing the Fruit Class {self._name} is {self._color}')
            return self._name

        #setter
        @name.setter
        def name(self, value: str):
            self._name = value
            print(f'Fruit name is now set to {self._name}')


