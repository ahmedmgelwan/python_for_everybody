'''
he program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
'''

import json
from urllib import request, parse

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter location: ')
if len(address) < 1: quit()

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + parse.urlencode(parms)

print('Retrieving', url)
uh = request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')


try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    quit()

place_id = js["results"][0]["place_id"]
print('Place ID: ',place_id)
