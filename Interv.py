def constCounter(text):
    vowels = "aeiou"
    count = 0


    for char in text:
        if char.isalpha() and char not in vowels:
            count +=1

    return count


print(constCounter("Sahil"))
