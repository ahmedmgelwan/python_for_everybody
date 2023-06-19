'''
The program will prompt for a URL, 
read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
compute the sum of the numbers in the file and enter the sum below:
'''

import json
from urllib .request import urlopen

url = input('URL: ')
html = urlopen(url).read()
data = json.loads(html)
comments = data['comments']
sum = 0
for i in range(len(comments)):
    sum += comments[i]['count']

print(sum)

