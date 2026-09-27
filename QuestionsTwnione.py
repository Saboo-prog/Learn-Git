# Input:  [1, 2, 3, 2, 4, 3, 5]


def dupFin(list):
    dict = {}
    apt = []
    for item in list:
        if item in dict:
            dict[item] += 1

        else:
            dict[item] = 1


    for item , count in dict.items():
        if count >=2:
            apt.append(item)

    return apt



print(dupFin([1, 2, 3, 2, 4,6,7,7,7,7,3, 5]))

