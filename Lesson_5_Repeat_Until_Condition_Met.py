# Exercise 1: Write a program which repeatedly reads numbers until the user enters done". Once done is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

numberTotal = 0
numberCount = 0
numberAverage = 0

while True :
    try :
        x = input("Input a number.")

        if x == "done" :
            print("Total: " + str(numberTotal))
            print("Count: " + str(numberCount))
            print("Average: " + str(numberAverage))
            break
        else :
            numberTotal = numberTotal + int(x)
            numberCount = numberCount + 1
            numberAverage = numberTotal / numberCount

    except :
        print("Enter a number or done to stop.")
        continue
