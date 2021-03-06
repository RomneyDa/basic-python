# Dallin Romney
# XML to SQLite Notes

import xml.etree.ElementTree as ET
import sqlite3
#from prettytable import PrettyTable

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Build music track tables: Delete any existing conflicting tables, then create
# Artist, Album, Track table

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    
    CREATE TABLE ARTIST (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
    );

    CREATE TABLE Album (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id INTEGER,
            title TEXT UNIQUE
    );
    
    CREATE TABLE Track (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            album_id INTEGER,
            title TEXT UNIQUE,
            len INTEGER, rating INTEGER, count INTEGER
    );
''')

# Obtain XML file name (where Apple music library data is)
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'Library.xml' # default file name

# This function looks through a dictionary (converted from xml) and checks each
# key to see if it matches a given key. 
def lookup(d, key):
    found = False
    for child in d:                                  # For each key in the dict
        if found : return child.text                 # Return following tag value if found 
        if child.tag == 'key' and child.text == key: # If current tag is a key and matches given key
            found = True                             # Mark as found
    return None                                      # Return None if not found

# Convert xml data to more useful format and extract all dict tags
stuff = ET.parse(fname)
allDicts = stuff.findall('dict/dict/dict')
print('Dict count:', len(allDicts))

# Create a table for visualizationfrom prettytable import PrettyTable
#headers = ['Title', 'Artist', 'Album', 'Count', 'Rating', 'Length']
#printTable = PrettyTable(headers)
#printTable._set_align('l')

# For each dictionary tag
for entry in allDicts:
    # If the dictionary doesn't contain a track in the first level, skip
    if lookup(entry, 'Track ID') is None: continue
    
    # Otherwise, map each value in our database to Apple's names
    name   = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album  = lookup(entry, 'Album')
    count  = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    # If we don't have the track name, artist, AND album, skip
    if name is None or artist is None or album is None: continue

    # Other info isn't critical so might show up as none. 
    # Add all track info to table for printing
    # print(name, artist, album, count, rating, length)
    printTable.add_row([name, artist, album, count, rating, length])
    
    # Add artist entry to database, retrieve autoincremented (key) artist id
    # Ignore simply skips it if the artist already exists
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?'          , (artist, ))
    artist_id = cur.fetchone()[0]
    
    # Add album entry to database, retrieve autoincremented (key) album id
    # Like the artist, skip album if it already exists
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id ))
    cur.execute('SELECT id FROM Album WHERE title = ?'                        , (album, ))
    album_id = cur.fetchone()[0]
    
    # Add track entry to database
    # Replace will overwrite any non-existing values
    cur.execute('''INSERT OR REPLACE INTO Track 
                (title, album_id, len, rating, count) VALUES(?, ?, ?, ?, ?)''',
                (name, album_id, length, rating, count ))

# Print results
#print(printTable)

# Write database to disk
conn.commit()