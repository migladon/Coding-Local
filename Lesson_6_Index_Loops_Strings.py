# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.


fruit  = "Apple"
index = len(fruit) - 1

while index >= 0 :
    letter = fruit[index]
    print(letter)
    index = index - 1

#Different Way

fruit = "Banana"
index = - 1

while index >= len(fruit) * -1 :
    print(fruit[index])
    index = index - 1

#Different Way
for char in fruit :
    print(char)

print(fruit[:])
print(fruit[:3])
print(fruit[3:])
print(fruit[0:2])

fruit = fruit[0:3]
print(fruit)
