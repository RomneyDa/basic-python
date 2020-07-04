# Dallin Romney
# Twitter API Notes

import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    
    # Take username input from user (loop until blank name entered)
    acct = input('Enter Twitter Account: ')
    if(len(acct) < 1): break

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    
    # Open connection and retrieve data
    print('Retreiving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    
    # Check connection headers to see how many requests we have left from Twitter
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    
    # Convert data to list/dict format and # print it nicely
    js = json.loads(data)
    #print(json.dumps(js, indent = 4))
    
    # For each user, print their screen name and the first 50 chars of their status
    for user in js['users']:
        print(user['screen_name'])
        if 'status' not in user: continue
        status = user['status']['text']
        print('  ', status[:])