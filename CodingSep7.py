def maxMin(list):
    max = 0
    min = list[0]

    for num in list:
        if num > max:
            max = num

        elif num <=min:
            min = num


    return max , min

















print(maxMin([6,7,5,4,3,10,18,9]))

    