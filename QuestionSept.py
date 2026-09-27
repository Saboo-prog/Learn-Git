def findNon(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] +=1
        else:
            dict[char] = 1


    for char,count in dict.items():
        if count == 1:
            return char

print(findNon("sahilll"))


