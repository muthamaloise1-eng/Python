def ageclassifier(age):

    if age < 0:
        print("Invalid age")
    elif age >= 0 and age < 18:
        print("0 - 17 years")
    elif age >= 18 and age <= 25:
        print("18 - 25")
    elif age <= 25 and age <= 30:
        print("26 - 30")
    else:
        print(">30")

ageclassifier(20)