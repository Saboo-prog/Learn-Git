def charCount(text:str):
    char_count = {}

    for char in text:
        if char not in char_count:
            char_count[char] = 1

        else:
            char_count[char] +=1

    return char_count




print(charCount("Sahilll"))