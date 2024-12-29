
def greet(name: str):
    tem: str = name.capitalize()
    print(f'Hello, {name}')


def greet_and_return(num1: int, num2: int) -> float:
    print(f'Sum of, {num1} and {num2}' + " = " + str(num1+num2))
    return num1 + num2
