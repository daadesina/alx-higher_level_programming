def myFunc(*arg, **kwarg):
    myList = []
    for i in arg:
        myList = myList + [i, ]

    #print (myList)

    kwaList = []
    for i, j in kwarg.items():
        kwaList = kwaList + [i, j, ]
    return kwaList

mymy = myFunc(1, 2, 3, 4, 5, 6, 7, name="ade", age=23)

print (mymy)

for i in range(len(mymy)):
    if mymy[i - 1] == "name":
        mymy[i] = "akanji"

print (mymy)
