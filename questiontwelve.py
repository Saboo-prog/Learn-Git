def findMissing(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum




print(findMissing([0,1,2,3,5,6,7,8,9,10]))