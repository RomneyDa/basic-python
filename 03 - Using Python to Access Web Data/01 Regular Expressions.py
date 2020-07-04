# Dallin Romney
# Regular Expressions

import re

# This line uses regular expressions to search for any number in the text of 
# a file, made up of digits 0-9 and of any length, and then uses list 
# comprehension to return a list of those numbers converted to strings.
# That list is then summed and the result printed.
print( sum( [ int(num) for num in re.findall('[0-9]+', open('DataActual.txt').read()) ] ) )
