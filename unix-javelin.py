import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Javelin
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of students.
N = 0

# D contains the distances. Note that the list starts from 0, and so the values
# are D[0] to D[N-1].
D = []

# Open the input and output files.
input_file = open("javelin.txt", "r")
output_file = open("javelout.txt", "w")

# Read the value of N and the distances from the input file.
N = int(input_file.readline().strip())
input_line = input_file.readline().strip()
D = list(map(int, input_line.split()))

# TODO: This is where you should compute your solution. Store the number of
# current leaders that there were during the competition into the variable
# answer.

answer = 0

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
