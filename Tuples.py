

def tupleTests1():
    print("testing tuples")

    people: tuple[str] = 'troy', 'kevin', 'sherri', 'troy', 'troy'
    print(people)
    print(type(people))

    # convert a tuple into a list
    tup_list: list[str] = list(people)
    print("this is the list created from the tuple:")
    print(tup_list)

    print("my name appears " + str(tup_list.count('troy')) + " times in the tuple")

    # unpacking a tuple
    print(people[1])

    # assigning people elements to individual variables
    a, b, c, d, e = people
    print(a)

    # Using count() for tuples to see how many instances of a duplicate entry exist
    print("there are " + str(people.count('troy')) + " " + "occurances of \'troy\'")

    # unpack tuple and get teh rest of everything
    a, b, c, *d = people
    print(d)
