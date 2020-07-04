# Dallin Romney
# SQLite Notes

import sqlite3

conn = sqlite3.connect('02_emaildb.sqlite') # Check/open access to DB
cur = conn.cursor()                      # Like a handle to send commands

cur.execute('DROP TABLE IF EXISTS Counts') # Ensures file is clear
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')            # Take file name from user

if (len(fname) < 1): fname = 'mbox-short.txt' # Default file name (no user input)
fh = open(fname)                              # Open file

for line in fh:                                # For each line in the file
    if not line.startswith('From: '): continue # Look only for lines starting with From:
    pieces = line.split()                      # Split them into a list of words
    email = pieces[1]                          # email address is the 2nd word
    
    # Question mark ? is a placeholder just like %.2f in MATLAB
    # (email,) returns a 1x1 tuple
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    
    row = cur.fetchone() # Check to see if there's any matches
     
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    
    # Writes to Disk
    conn.commit()
    
# https://www.sqlite.org/lang_select.html
    
# Command to select an ordered table of email and count data from database
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr): # For each row in the returned table
    print(row[0], row[1])       # Print count converted to string, email
    
# Close the connection to the database
cur.close()
    
# =============================================================================
# Example SQL Commands:
# 
# INSERT INTO Users(name, email) VALUES('Kristin', 'kf@umich.edu')
# DELETE FROM Users WHERE email = 'fred@umich.edu'
# UPDATE Users SET name = 'Charles' WHERE email = 'csev@umich.edu'
# 
# SELECT * FROM Users
# SELECT * FROM Users WHERE email = 'csev@umich.edu'
# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name
# 
# =============================================================================
