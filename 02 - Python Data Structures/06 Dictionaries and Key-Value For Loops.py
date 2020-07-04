# Dallin Romney

# Ask for user input for file name and open file
fname = input("Enter file name: ")

# Default file name
if len(fname) < 1 : fname = "mbox-short.txt"

# Open file
fh = open(fname)

countDict = dict() # Empty dictionary for "histogram"

# For each line in the file, find sender values and log them
# in the dictionary
for line in fh:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        countDict[sender] = countDict.get(sender, 0) + 1
        
# Loop through dictionary to find case with most occurences
bigword   = None
bigvalue  = None    
for k, v in countDict.items():
    if v > bigvalue or bigword is None:
        bigword = k
        bigvalue = v
        
print(bigword, bigvalue)

