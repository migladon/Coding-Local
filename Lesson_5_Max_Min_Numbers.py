minimumNumber = None
maxNumber = None


while True :
    x = input("enter a number")
    try :
        if x == "done" :
            print("Minimum Number: " + str(minimumNumber))
            print("Maximum Number: " + str(maxNumber))
            break

        elif minimumNumber == None :
                minimumNumber = float(x)
                maxNumber = float(x)

        elif float(x) < minimumNumber :
            print("x is less than min")
            minimumNumber = float(x)

        elif float(x) > maxNumber :
            print("x is greater than min")
            maxNumber = float(x)

    except :
            print("Please enter a number")
            continue
