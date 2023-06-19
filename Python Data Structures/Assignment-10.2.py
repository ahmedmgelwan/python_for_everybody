'''
Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time 
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below
'''


fname = input('File Name: ').strip()

try:
    file = open(fname, 'r')
    hours = []
    hours_counter = {}
    for line in file:
        if not line.startswith('From'): continue
        if len(line.split()) > 2 : 
            time = line.split()[-2]
            hour = time.split(':')[0]
            hours.append(hour)
    
    file.close()
    hours.sort()
    for hour in hours:
        hours_counter[hour] = hours.count(hour)
    
    for hour in hours_counter:
        print(hour, hours_counter[hour])

            

except FileNotFoundError:
    print(f'{fname} Not Found ):')