def dupChars(text:str):
    char_counter = {}
    rep = []

    for char in text:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] +=1


    for char , value in char_counter.items():
        if value >= 2:
            rep.append(char)

    return rep



print(dupChars("saahhiillkapp"))
