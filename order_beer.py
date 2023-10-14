# Sample output 


# * * * * Jamal and Daughters Pub * * * *

# Beer               Brand Price
#-------------------------------
# 1) Tusker          200/=
# 2) Pilsner         280/=
# 3) Smirnoff Ice    320/=
# 4) White Cap       180/=

# Enter your choice: 2
# How many bottles of pilsner do you want? 11
# 11 bottles of pilsner will cost you Kshs. 3080

from tabulate import tabulate

def order_beer():
    col_names = ["Beer Brand", "Price"]

    beer_menu = [
        ["1) Tusker", "200/="],
        ["2) Pilsner", "280/="],
        ["3) Smirnoff", "320/="],
        ["4) White Cap", "180/="],
    ]

    print("* * * * Jamal and Daughters Pub * * * *")
    print(tabulate(beer_menu, headers=col_names))

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")

        except ValueError:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

    while True:
        try:
            if choice == 1:
                quantity = int(input("How many bottles of Tusker do you want? "))
            elif choice == 2:
                quantity = int(input("How many bottles of Pilsner do you want? "))
            elif choice == 3:
                quantity = int(input("How many bottles of Smirnoff do you want? "))
            else:
                quantity = int(input("How many White cap of Tusker do you want? "))
            if quantity >= 0:
                break
            else:
                print("Quantity can't be below 0.")
        except ValueError:
            print("Invalid input! Please enter a valid quantity (a non-negative number).")

    
    if choice == 1:
        total_cost = quantity * 200
        print(f"{quantity} bottles of Tusker will cost you Ksh {total_cost}")
    elif choice == 2:
        total_cost = quantity * 280
        print(f"{quantity} bottles of Pilsner will cost you Ksh {total_cost}")
    elif choice == 3:
        total_cost = quantity * 320
        print(f"{quantity} bottles of Smirnoff will cost you Ksh {total_cost}")
    else:
        total_cost = quantity * 180
        print(f"{quantity} bottles of White cap will cost you Ksh {total_cost}")


if __name__ == "__main__":
    order_beer()
