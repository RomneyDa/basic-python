# Dallin Romney

# Take in hours and hourly pay and output gross Pay, considering overtime

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

# Convert strings to floats
h = float(hrs)
r = float(rate)

# For less than overtime, simply rate times time
if hrs <= 40:
    pay = h*r
# For more, pay 1.5 normal rate for any hours past 40
else:
    pay = 40*r + (h - 40)*r*1.5

# Print results
print(pay)
