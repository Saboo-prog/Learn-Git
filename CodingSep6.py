def checkAna(text , tex):
    first = {}
    second = {}

    if len(text) != len(tex):
         return False

    
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



    return first == second





print(checkAna("sahil" , "lhas"))
    


    