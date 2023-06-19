import re
# import os
# print(os.getcwd())
# mail = ' From ahmed@google.com 88'
# name = '(+)@+.+\s'
# org = 'From [A-z]+@([a-z]+.com)\s'
# print(re.findall(org, line))

fh = open('mbox.txt', 'r')
pattern = 'From +@(+.+)\s'
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line = line.split()
        org_name = line[1].split('@')[1]
        print(org_name)
