def convert(number):
    r = ""
    if number % 3 == 0:
        r += "Pling"
    if number % 5 == 0:
        r += "Plang"
    if number % 7 == 0:
        r += "Plong"

    if len(r) != 0:
        return r
    else:
        return str(number)
