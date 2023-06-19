'''
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
'''

fname = input('File Name: ')

try:
    file = open(fname, 'r')
    words = []
    for line in file:
        line_list = line.split()
        for word in line_list:
            if word in words : continue
            words.append(word)
    file.close()
    words.sort()
    print(words)
except:
    print(f'{fname} not founded ):')

