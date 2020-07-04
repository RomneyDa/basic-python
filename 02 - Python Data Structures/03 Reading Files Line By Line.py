# Dallin Romney

# User input for the filename, and then search for and average confidence values
fname = input("Enter file name: ")
fh = open(fname)

count = 0
totalconf = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else :
        pos = line.find(' ')
        confstring = line[pos + 1:]
        conf = float(confstring.strip())
        totalconf += conf
        count += 1

avgconf = totalconf/count
print("Average spam confidence:", avgconf)
