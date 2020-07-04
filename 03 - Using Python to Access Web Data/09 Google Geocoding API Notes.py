# Dallin Romney
# Google Geocoding API Notes

import urllib.request, urllib.parse, urllib.error
import json

# Google's geocoding API url
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    # Take in address from user, repeat loop until empty address entered
    address = input('Enter location: ')
    if len(address) < 1: break
    
    # Creates url by concatenating service URL and user input converted to URL format
    url = serviceurl + urllib.parse.urlencode({'address':address})
    
    print('Retreiving', url)
    data = urllib.request.urlopen(url).read().decode()
    print('Retreived", len(data)', 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrieve ====')
        print(data)
        continue
    
    # Print it (so that it looks nice)
    print(json.dumps(js, indent = 3))
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    
    print('lat', lat, 'lng', lng)
    
    location = js["results"][0]["formatted_address"]
    print(location)