# Function to flip a single digit
def flip_digit(digit):
    if digit == "0":
        return "9"
    elif digit == "1":
        return "8"
    elif digit == "2":
        return "7"
    elif digit == "3":
        return "6"
    elif digit == "4":
        return "5"
    elif digit == "5":
        return "4"
    elif digit == "6":
        return "3"
    elif digit == "7":
        return "2"
    elif digit == "8":
        return "1"
    elif digit == "9":
        return "0"
    else:
        return digit

# Main program
num = input("Enter any number (0-9 digits): ")

flipped = ""
for d in num:
    flipped += flip_digit(d)

print("Flipped number is: ", flipped)