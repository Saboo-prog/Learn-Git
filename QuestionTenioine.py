def findSeco(numbers):
    largest = 0
    second_largest = 0

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num !=largest:
            second_largest = num


    return second_largest


print(findSeco([5,6,7,8,9,10]))



    