# Find the longest substring


def findLongest(text):
    last_seen = {}
    current_start = 0
    longest = ""

    for index,char in enumerate(text):

        if char in last_seen and last_seen[char] >= current_start:
            current_start = last_seen[char] + 1

        last_seen[char] = index





    