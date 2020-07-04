# Dallin Romney

import urllib.request, urllib.parse, urllib.error
import bs4 as bs
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use 'http://py4e-data.dr-chuck.net/known_by_Breogan.html'
url   = input('Enter URL: ')        # Starting URL
count = int(input('Enter count: ')) # How many pages to look through
pos   = int(input('Enter pos: '))   # Position of link to follow in page

# For count # of times
for k in range(count):
    webPage = urllib.request.urlopen(url).read()    # Open webpage
    soup = bs.BeautifulSoup(webPage, 'html.parser') # Beautify with bs4
    
    tags = soup('a')                                # Pull out all link tags
    links = [tag.get('href', None) for tag in tags] # Make a list of their vals
    url = links[pos - 1]                            # Take link at pos
    print(url)                                      # Print that link