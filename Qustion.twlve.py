# Given an array containing numbers from 0 to n, with one number missing, return the missing number.

def findMissing(nums):

    missing = float('-inf')

    for i in range(len(nums)-1):
        if (nums[i]+1) not in nums:
            missing = nums[i]+1



    return missing


print(findMissing([1,3,4,5,6,7,8,9]))







    


