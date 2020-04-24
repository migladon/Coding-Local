grade = input("Please enter your score.\n")
try :
    grade = float(grade)
except:
    print("Please enter a numeric score between 0.0 and 1.0")
    quit()
if grade > 1.0 or grade < 0:
    print("Please ensure score is between 0.0 and 1.0")
    quit()


if grade >= 0.9 :
    print("A")
elif grade >= 0.8 :
    print("B")
elif grade >= 0.7 :
    print("C")
elif grade >= 0.6 :
    print("D")
elif grade < 0.6 :
    print("F")
