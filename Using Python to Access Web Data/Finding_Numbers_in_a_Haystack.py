'''
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers and summing up the integers.
'''

import re

fname = input("File: ")
file = open(fname, 'r')
numbers = []
for line in file:
    extract = re.findall('[0-9]+',line)
    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = int(extract[i])
        numbers.append(num)

file.close()
print(sum(numbers))
