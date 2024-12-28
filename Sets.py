
def setTests():
    print('testing sets')

    myset1 = {'apple', 'banana', 'cherry', 'cherry', 15, True, 'cherry'}
    print(myset1)
    myset1.remove('cherry')
    print(myset1)

    """
    print("from the for loop")
    for x in myset1:
        print(myset1[x]) # Error, is not subscriptable
    """

    print("convert set to a list so it can be iterable")
    mylist1: [str] = list(myset1)
    print(mylist1)

    for x in range(0, len(mylist1)):
        print(mylist1[x])


