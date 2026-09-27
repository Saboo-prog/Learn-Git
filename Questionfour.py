# 1. First Non-Repeating Character — Medium


# def firstNon(text):
#     results = {}

#     for char in text:
#         if char in results:
#             results[char] +=1
#             break
#         else:
#             results[char]= 1 

#     for char,value in results.items():
#         if value >= 1:
#             return char



# print(firstNon("SWISIS"))

# First Repeating Character — Medium

def firstRep(text):
    results = {}

    for char in text:
        if char in results:
            results[char] +=1
        else:
            results[char]= 1 

    for char,value in results.items():
        if value == 1:
            return char


