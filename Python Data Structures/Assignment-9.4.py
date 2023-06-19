'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committe
'''


fname = input('File Name: ').strip()

try:
    file = open(fname, 'r')
    emails = []
    send_counter = {}
    for line in file:
        if not line.startswith('From'): continue
        if len(line.split()) > 2 :
            emails.append(line.split()[1])
        
        for i in emails :
            count = 0
            for j in emails:
                if i == j : count +=1
            send_counter[i] = count
    file.close()
    max_number = 1
    max_email = ''
    for email in send_counter:

       if send_counter[email] > max_number:
           max_number = send_counter[email]
           max_email = email
    
    print(max_email, max_number)
    

except FileNotFoundError:
    print(f'{fname} Not Found ):')