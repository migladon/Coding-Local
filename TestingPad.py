# word = 3
# print(type(float(word)))
# print(type(word))
# print(dir(word)) # list the methods available for an object
# print(type(2))
# print(dir(2))

# n = 10
# while True :
#     print(n,end=' ')
#     n = n - 1
# print("Done")

#python2 does not support end=' '
#in terminal, loop statement requires a empty line


while True :
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done" :
        break
    print(line)

print("done!!!")
