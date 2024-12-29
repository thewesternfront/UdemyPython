import Strings
import Lists
import Tuples
import Sets
import Dictionaries
import Loops
import Functions
import Recursion
import ArgsKwargs


def main():

    # simple string
    mystring = "Hello World!"
    print(mystring)

    # simple list
    people_list = ["Mario", "Luigi"]
    for x in people_list:
        print(x)

    # number in range type
    numbers = range(1, 100, 3)
    for x in numbers:
        print(x)
        print("*** NUMBERS TYPE ***")
        print(type(numbers))

    # simple dictionary
    dict_users = {"User1": "Mario123", "User2": "Luigi2024"}
    print(dict_users)
    for x in dict_users:
        print(dict_users[x])

    # set
    set1 = {"User1", "User2", "User3", "User2", "User4", "User1"}
    print("printing set1: % ", set1)
    # frozen set
    set2 = frozenset({"User1", "User2", "User3", "User2", "User4", "User1"})
    print("printing set2: %",  set2)

    print("printing set 1:{0}, printing set 2: {1}".format(set1, set2))

    #type casting, type hinting
    myname: str = "Troy West"
    myage: int = 57
    myfloat: float = 3.1415926538

    print(myname, myage, myfloat)

    addative: float = 100.123
    # type casting inline
    print(myname + " " + str(myage) + " " + str(myfloat + addative))


    # walk bacward through a loop
    dataset = [1, 2, 3, 4, 5]
    for x in reversed(dataset):
        print(x)

    # Comparison operators
    a = 10
    b = 10
    print(a != b)
    print(a == b)
    print(a <= b)
    print(a >= b | a <= b)
    print(a >= b & a <= b)
    print(not(a >= b and a <= b))
    print(not(a >= b or a <= b))


if __name__ == '__main__':
    # main()
    Strings.stringTest1()
    Strings.fStringsTest1()
    Lists.listTests1()
    Tuples.tupleTests1()
    Sets.setTests()
    Dictionaries.dictionaryTests1()
    Loops.loopTests1()
    Functions.greet('Troy')
    tem: float = Functions.greet_and_return(200, 300)
    print(tem)
    Recursion.recursion(5)
    ArgsKwargs.ArgsKwargs('Troy', 'Anna', 'Sherri', 'Kevin', 'Pop', 'Mom')





