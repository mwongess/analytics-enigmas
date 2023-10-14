# Write a program to read a value from the keyboard and output the phrase NEGATIVE 
# if the number is negative, POSITIVE if the number is positive or ZERO otherwise.

def neg_or_pos():
    try:
        number = int(input("Enter a number:"))
        if number > 0:
            print("POSITIVE")
        elif number < 0:
            print("NEGATIVE")
        else:
            print(0)
    except ValueError:
        print("Enter a valid number")

if __name__ == "__main__":
    neg_or_pos()