def dictionaryTests1():
    print("Dictionary Tests")

    users: [dict] = {'Troy': 100,
                     'Sherri': 200,
                     'Kevin': 300}

    print(users)
    print(users.keys())
    print(users.values())
    print(users.items())

    users['Kevin'] = 777
    print(users)

    users.update({'Eugene': 99})
    print(users)
    x = users.pop('Troy')
    print(users)
    print(x)


