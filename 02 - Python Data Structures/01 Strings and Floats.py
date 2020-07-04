# Dallin Romney

# Extract the number from the given string

# Given string
text = "X-DSPAM-Confidence:    0.8475";

# Find the space and slice anything after it
pos = text.find(' ')
sliced = text[pos+1:]

# Cut out any white space and convert it to a number
num = float(sliced.strip())

# Print result!
print(num)
