def dateConv(date:str):
    day,month,year = date.split("-")
    # day = date[0]
    # month = date[1]
    # year = date[2]

    updated = f"Date is: {year}-{month}-{day}"
    return updated




print(dateConv("24-12-2025"))

    