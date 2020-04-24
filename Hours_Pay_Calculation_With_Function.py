
userHours = input("Enter Your Total Hours Worked\n")
try :
     userHours = float(userHours)
except :
    print("Please enter numeric value.")
    quit()

payRate = input("Enter Your Payrate\n")
try :
    payRate = float(payRate)
except :
    print("Please enter numeric value." + variable)
    quit()



def computePay(hours,rate) :
    if float(hours) > 40 :
        overtimeHours = hours - 40
        overtimePay = overtimeHours * payRate * 1.5
    else :
        overtimeHours = 0
        overtimePay = 0

    grossPay = (hours - overtimeHours) * (payRate) + (overtimePay)
    return (round(grossPay,2))

print(computePay(userHours,payRate))
