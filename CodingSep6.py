def checkAna(text , tex):
    first = {}
    second = {}

    for char in text:
        if char not in first:
            first[char] = 1

        else:
            first[char] += 1


    for char in tex:
            if char not in second:
                second[char] = 1
    
            else:
                second[char] += 1


    if first == second:
         return True
    else:
         return False




print(checkAna("sahil" , "lhas"))
    


    