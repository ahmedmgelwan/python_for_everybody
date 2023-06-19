'''
The program will use urllib to read the HTML from the data files below, and parse the data, 
extracting numbers and compute the sum of the numbers in the file.
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
url = input('URL: ')
html = urlopen(url,).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
numbers = []
for tag in tags :
    numbers.append(int(tag.text))

print(sum(numbers))