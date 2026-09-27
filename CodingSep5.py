def strRev(text:str):
    result = []

    for i in range(len(text) -1 , -1 , -1):
        result.append(text[i])

    return "".join(result)


print(strRev("ash"))