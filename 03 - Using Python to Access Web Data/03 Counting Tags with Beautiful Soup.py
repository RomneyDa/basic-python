# Dallin Romney

import urllib.request, urllib.parse, urllib.error
import bs4 as bs

url = 'http://py4e-data.dr-chuck.net/comments_391310.html'
webPage = urllib.request.urlopen(url).read()

soup = bs.BeautifulSoup(webPage, 'html.parser')

tags = soup('span')

print(sum([int(tag.contents[0]) for tag in tags]))
