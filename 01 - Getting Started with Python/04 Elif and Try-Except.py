# Dallin Romney

scoreString = input("Enter Score:")
error = "Invalid input. Must be a number between 0 and 1."

try:
    score = float(scoreString)

    if score < 0 or score > 1:
        print(error)
    else:
        if   score < 0.6:
            grade = "F"
        elif score < 0.7:
            grade = "D"
        elif score < 0.8:
            grade = "C"
        elif score < 0.9:
            grade = "B"
        else:
            grade = "A"

    print(grade)

except:
    print(error)
