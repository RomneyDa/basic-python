# Dallin Romney

# Read line by line, split each line into a list, and append any new words
# to a new list. Print resulting list in alphabetical order

# Ask for user input for file name and open file
fname = input("Enter file name: ")
fh = open(fname)

lst = list()                 # Initialize empty list

for line in fh:              # For each line in the file
    words = line.split()     # Split it into a list of words
    for word in words:       # Loop through each word in the
        if word not in lst:  # If the word hasn't been seen yet, 
            lst.append(word) # add it to list

lst.sort() # Sort list alphabetically

print(lst)
