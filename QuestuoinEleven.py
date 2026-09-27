# Second Largest Number without using sort().

def findSeco(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num


    return second_largest




print(findSeco([5,6,7,8,9]))