grade = input("Please enter your score.\n")
try :
    grade = float(grade)
except:
    print("Please enter a numeric score between 0.0 and 1.0")
    quit()
if grade > 1.0 or grade < 0:
    print("Please ensure score is between 0.0 and 1.0")
    quit()


def computeGrade(score) :
    if score >= 0.9 :
        return("A")
    elif score >= 0.8 :
        return("B")
    elif score >= 0.7 :
        return("C")
    elif score >= 0.6 :
        return("D")
    elif score < 0.6 :
        return("F")

print(computeGrade(grade))
