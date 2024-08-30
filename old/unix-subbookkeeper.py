import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Subbookkeeper
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of letters in the word.
N = 0

# word is the word with one missing letter
word = ""

# Open the input and output files.
input_file = open("bookin.txt", "r")
output_file = open("bookout.txt", "w")

# Read the value of N and the word from the input file.
N = int(input_file.readline().strip())
word = input_file.readline().strip()

splitWord = word.split('?')
print(splitWord)

wordA = splitWord[0]
wordB = splitWord[1]

def timesLastLetterInWordARepeatedConsecutively():
    try:
        lastLetter = wordA[-1]
    except:
        lastLetter = ""
    count = 0
    for letter in wordA[::-1]:
        if letter == lastLetter:
            count += 1
        else:
            break
    return count

def timesFirstLetterInWordBRepeatedConsecutively():
    try:
        firstLetter = wordB[0]
    except:
        firstLetter = ""
    count = 0
    for letter in wordB:
        if letter == firstLetter:
            count += 1
        else:
            break
    return count

lettersA = timesLastLetterInWordARepeatedConsecutively()
lettersB = timesFirstLetterInWordBRepeatedConsecutively()

if lettersA > lettersB:
    missingLetter = wordA[-1]
else:
    missingLetter = wordB[0]

word = word.replace('?', missingLetter)
print(word)

def timesTwoConsecutiveLettersAreTheSame():
    count = 0
    lastchar = ""
    for char in word:
        if char == lastchar:
            count += 1
        lastchar = char
    print(count)
    return count


answer = timesTwoConsecutiveLettersAreTheSame()

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
