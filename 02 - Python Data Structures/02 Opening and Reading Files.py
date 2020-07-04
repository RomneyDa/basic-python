# Dallin Romney

# User input for the filename, and then print it in all caps

fname = input("Enter file name: ")
fh = open(fname)

content = fh.read();

print(content.upper())
