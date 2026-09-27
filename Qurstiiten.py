def listFilter(list):
    lists = []

    for l in list:
        if l not in lists:
            lists.append(l)

    return lists


print(listFilter([5,6,7,8,8,9,10,11]))


