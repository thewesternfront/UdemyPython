
def ArgsKwargs(age: int, *people: str):
    print(people)
    print(age)
    for i in people:
        print(f"Hello {i}")

    print(type(people))


# use keyword arguments

def do_something(*args,**kwargs):
    print(kwargs)
    print(type(kwargs))

    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['phone'])

    for i in args:
        print(i)