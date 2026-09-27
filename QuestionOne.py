# 1. Character Frequency — Medium

# Write a Python function that takes a string and returns the frequency of every character without using collections.Counter.




def charCounter(text):
    result = {}

    for char in text:
        if char in result:
            result[char] +=1
        else:
            result[char] = 1


    return result




print(charCounter("automations"))



def nonRep(result):
    arr = []
    for char , count in result.items():
        if count ==1 :
            arr.append(char)


    return arr



print(nonRep(charCounter("automations")))















