def moveZero(numbers):
    result = []
    for num in numbers:
        if num != 0:
            result.append(num)

    for num in numbers:
        if num == 0:
            result.append(num)


    return result


print(moveZero([0,5,6,0,0,7,8,9,10]))

            


