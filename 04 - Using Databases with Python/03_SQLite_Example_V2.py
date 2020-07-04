# Dallin Romney

import sqlite3, re

conn = sqlite3.connect('03_SQLite_Example_V2.sqlite') # Check/open access to DB
cur = conn.cursor()                                             # Like a handle to send commands

cur.execute('DROP TABLE IF EXISTS Counts')                   # Ensures file is clear
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)') # Create table called "count"

fname = input('Enter file name: ')      # Take file name from user
if (len(fname) < 1): fname = 'mbox.txt' # Default file name (no user input)
data = open(fname).read()               # Read data

org = re.findall('\nFrom:.*?@(.*?)\s', data) # Return list of all org names in text file

hist = dict()
for key in org:
    hist[key] = hist.get(key, 0) + 1

for key, val in hist.items():
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (key, val))

conn.commit() # Write to disk
cur.close()   # Close connection
