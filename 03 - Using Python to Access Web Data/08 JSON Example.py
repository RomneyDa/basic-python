# Dallin Romney
# JSON Example

import json                                       # JSON Parsing library
import urllib.request, urllib.parse, urllib.error # Webpage accessing library

# Ask for URL from user # http://py4e-data.dr-chuck.net/comments_391313.json
url = input('Enter location: ') 
print('Retrieving', url)

data = urllib.request.urlopen(url).read() # Open webpage, read in as string
print('Retrieved', len(data), 'characters')

# Convert JSON data to list/dict structure
JData = json.loads(data)

# Print the sum of the count key values from all the dictionaries in the comments list
print(sum([item['count'] for item in JData['comments']]))
