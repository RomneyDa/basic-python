# Dallin Romney

import xml.etree.ElementTree as ET                # XML Parsing library
import urllib.request, urllib.parse, urllib.error # Webpage accessing library

# Ask for URL from user # http://py4e-data.dr-chuck.net/comments_391312.xml
url   = input('Enter location: ') 
print('Retrieving', url);

data = urllib.request.urlopen(url).read() # Open webpage, read in as string
print('Retrieved', len(data), 'characters')

# Convert xml to data tree
tree = ET.fromstring(data) 

# Add all the text values of each count element in the tree
print( sum( [int(count.text) for count in tree.findall('.//count')] ) )
