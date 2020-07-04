# Dallin Romney

# Read line by line, print out the second word from any lines
# starting with "From ". Count and print how many lines there were

# Ask for user input for file name and open file
fname = input("Enter file name: ")

# Default file name
if len(fname) < 1 : fname = "mbox-short.txt"

# Open file
fh = open(fname)


count = 0 # Counter

for line in fh:
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")

