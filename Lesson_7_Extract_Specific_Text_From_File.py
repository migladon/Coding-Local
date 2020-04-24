# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

count = 0
spamTotal = 0

#filename = input("Please enter filename:")
filename = "mbox.txt"
handler = open(filename)

for line in handler :
    if line.find("X-DSPAM-Confidence:") == -1 :
            continue
    count = count + 1
    line = line.rstrip()
    score = line[line.find(":") +1:]
    spamTotal = spamTotal + float(score)
    print(score)
print("Count is %d") % count
print("Spam Average score is: %s" % (spamTotal/count))
