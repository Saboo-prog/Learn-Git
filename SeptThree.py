def anaCheck(text, texttwo):
    dict = {}
    dictOne = {}
    for char in text:
        if char in dict:
            dict[char] +=1
        else:
            dict[char] =1

    for char in texttwo:
            if char in dictOne:
                dict[char] +=1
            else:
                dict[char] =1

    if dict == dictOne:
        return True
    else:
         return False



print((anaCheck("silent","leisnt")))
    

    