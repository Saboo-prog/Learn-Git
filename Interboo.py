# Find unique and duplicate characters in your name
def uniqCounter(text):
    unique = set()
    duplicate = []

    for char in text:
        if char not in unique:
            unique.add(char)
        else:
            duplicate.append(char)


    return unique , duplicate


print(uniqCounter("Jinnniieee"))





    