'''
Write a program that prompts for a file name, 
then opens that file and reads through the file, looking for lines of the form:     X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values 
and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
'''

fname = input('File Name: ')
file = open(fname, 'r')
target = 'X-DSPAM-Confidence:'
count = 0
total =0 
for line in file:
    if not line.startswith(target): continue
    number = float(line[line.find('0'):])
    count += 1
    total += number
file.close()
print('Average spam confidence:', total / count)