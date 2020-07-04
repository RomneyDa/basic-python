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
        time = words[5]
        times = time.split(':')
        hour = times[0]
        countDict[hour] = countDict.get(hour, 0) + 1

# Print results
for k, v in sorted(countDict.items()):
     print(k, v)

