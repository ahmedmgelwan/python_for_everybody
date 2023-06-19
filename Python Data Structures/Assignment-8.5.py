'''
Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.
'''

fname = input('File Name: ').strip()
count = 0
try:
    file = open(fname, 'r')
    for line in file:
        if not line.startswith('From'): continue
        if len(line.split()) > 2 :
            print(line.split()[1])
            count += 1

    file.close()
    print(f'There were {count} lines in the file with From as the first word')

except:
    print(f'{fname} Not Found ):')