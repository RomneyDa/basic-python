# Dallin Romney

largest = None
smallest = None

# Take in integers from user input and find smallest and largest
while True:
    strin = input("Enter a number:")
    if strin == "done":
        break

    try:
        num = int(strin)
        
        if largest == None:
            largest = num
        elif num > largest:
            largest = num

        if smallest == None:
            smallest = num
        elif num < smallest:
            smallest = num
    except:
        print("Invalid input")

# Print results
print("Maximum is", largest)
print("Minimum is", smallest)
