def listTests1():
    list1: list[str] = ['Troy', 'Sherri', 'Kevin', 300]
    list2: list[str] =  ['Troy', 'Troy', 'Kevin2']
    #print(list1)

    print(list1[len(list1)-1] + 20)
    print(list1[0:4])

    print('Kevin' in list1)

    list1[0] = 'testing 123'
    print(list1)
    list1[1:2] = ['also testing', '123']
    print(list1)
    print(len(list1))

    list1.insert(2, '!!! test !!!')
    list1.append('end of list')
    list1.append('new end of list')

    list1.extend(list2)

    mylist1: list[str] = ['kevin', 'troy', 'sherri']
    mylist2: list[str] = ['troy', 'troy', 'anna']
    mylist3: list[str] = mylist1 + mylist2
    print(mylist3)
    mylist3.remove(mylist2[2])
    print(mylist3)
    mylist3.pop(2)
    print(mylist3)
