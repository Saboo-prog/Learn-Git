
# nums = [12, 21, 3, 40, 13, 22, 111, 5]
def group_by_digit_sum(nums):
    groups = {}

    for num in nums:
        digit_sum = 0

        # Calculate the sum of all digits in the current number.
        for digit in str(num):
            digit_sum += int(digit)

        # Add the number to its digit-sum group.
        if digit_sum not in groups:
            groups[digit_sum] = []

        groups[digit_sum].append(num)

    return groups


nums = [12, 21, 3, 40, 13, 22]

print(group_by_digit_sum(nums))