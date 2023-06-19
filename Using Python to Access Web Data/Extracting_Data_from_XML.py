'''
The program will prompt for a URL, 
read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
compute the sum of the numbers in the file.
'''

from urllib.request import urlopen
from xml.etree import ElementTree as ET

url = input('URL: ')
html = urlopen(url).read()
tree = ET.fromstring(html)
comments_list = tree.findall('comments/comment')
sum = 0
for comment in comments_list:
    sum += int(comment.find('count').text)
print(sum)