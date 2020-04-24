
#Conditional / Sequental Logic

x = -5

if x == 10 :
    print ("CONDITIONAL")
print("SEQUENTAL")
if x < 10 :
    print("CONDITIONAL\n")
print("SEQUENTIAL\n")


#ranges


for i in range (5) :
    x = x + 1
    print (x)
print("Done Incrementing x using range")


#elif


if x < 2 :
    print("SMALL")
elif x < 10 : #elif will exit the logic block if true
    print("MEDIUM")
elif x < 15 :
    print("LARGE")
else : #else is not required to use elif
    print ("EXTRA LARGE")
print("DONE JUDGING SIZE")

#try / except (used for accepting errors, often used with any user input)

astr = ("I'm a string!")
try :
    astr = int(astr) #cant convert a string to an integer
    print("All good, astr is string so the conversion is fine")
except : #catch `the error
    astr = -1
    print("Exception, error converting value to string. Still able to proceed because we caught it.")

print ("Done with try block")
print ("astr is " + str(type(astr)))

#math / type statement examples
calculationOne = 17//2
calculationTwo = 17/2.0
calculationThree = 12/3
calculationFour= 1 + 2 * 5
calculationFive = round(23.5662,2)

if x%2 == 0 :
    print ("x is " + str(x) + " which is even")
else :
    print ("x is " + str(x) + " which is not even")

print (str(calculationOne), str(type(calculationOne)))
print (str(calculationTwo), str(type(calculationTwo)))
print (str(calculationThree), str(type(calculationThree)))
print (str(calculationFour), str(type(calculationFour)))
print (str(calculationFive), str(type(calculationFive)))

import math
print(math)

import random
print(random)
for i in range(10) :
    x = random.random()
    print(x)

def myFunction(param1,param2):
    return str(param1+param2)

print("The Result of " + (str(type(myFunction))) + " is " + myFunction(2,3))
print(myFunction)
print ("Multiplying a string 3 times \n" * 3)

# while True:
#     print("Enter 'done' to stop this while true loop")
#     line = input('> ')
#     if line == 'done':
#         break

print('Done!')


# String Manipulation

word = "Corn @22 Man dog"

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

print(str(type(word)))
print(str(dir(word))) # list the methods available for an object
print(str(type(2)))
print(str(dir(2)))
help(str.capitalize)
help(int.numerator)
upperWord = word.upper()
print(word.upper())
print(word.lower()) #important for standardizing word for comparison
print(upperWord)
print(str.upper(word))
print(word.find("rn")) #returns the index of
print(word[0:3])
print(word.find("rn",3)) # returns the index of, second argument starts search at index besides 0
print(word.strip()) # strips whitespace from back and front
print(word.lower().startswith("c"))
print(word.startswith("b"))
atpos = word.find("@")
print(atpos)
sppos = word.find(' ',atpos)
print(sppos)
print(word.find(" ",word.find("@")))
print(word[word.find("@") + 1:word.find(" ",word.find("@"))])
print(word[atpos+1:sppos])
penguins = 34.332
lions = 1.41212
print("I have spotted %d penguins and %g lions and %d seals %s dollars") % (penguins,lions,2,"hi")
print(word.title())
print(word.replace("Dog".lower(),"Cat"))
print(word.find("@",2,7)) # find the substring in after / before an index


#FILES
fhand = open('mbox.txt')
print(str(fhand))

count = 0
for line in fhand : #fhand is called a sequence
    count = count + 1
print("Line Count:", count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print inp[:20]

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith("From:") :
        print(line)

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip() #pyton automatically will add the new line character on the for loop so we can remove it from file handler
    if not line.startswith("From:") :
        continue

print(line)

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1 :
        continue
    print(line)

fout = open('output.txt', 'w')
fout.write("Writing a line to the file.\n")
print(fout)
fout.close()

whiteSpaceString = "1\n 2\t 3 4"
print(whiteSpaceString)
print repr(whiteSpaceString) # print white space representation of strings
