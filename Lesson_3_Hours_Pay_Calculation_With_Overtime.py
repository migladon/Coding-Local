
hours = input("Enter Your Total Hours Worked\n")
try :
     hours = float(hours)
except :
    print("Please enter numeric value.")
    quit()

payrate = input("Enter Your Payrate\n")
try :
    payrate = float(payrate)
except :
    print("Please enter numeric value." + variable)
    quit()

if float(hours) > 40 :
    overtimeHours = hours - 40
    overtimePay = overtimeHours * payrate * 1.5
else :
    overtimeHours = 0
    overtimePay = 0

grossPay = (hours - overtimeHours) * (payrate) + (overtimePay)
print(round(grossPay,2))
