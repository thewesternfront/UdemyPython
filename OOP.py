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
