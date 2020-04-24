# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)


def lettercount(word,letterChoice) :
    count = 0
    for letter in word: # so this variable will override the function if we use the same word 'letter'
        if letter == letterChoice :
            count = count + 1
    print(count)

lettercount("banana","b")

# str.count(sub[, start[, end]])
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
word = "banana"
print(word.count("a"))
