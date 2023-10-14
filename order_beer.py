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
            quantity = int(input("How many bottles do you want? "))
            if quantity >= 0:
                break
            else:
                print("Quantity can't be below 0.")
        except ValueError:
            print("Invalid input! Please enter a valid quantity (a non-negative number).")

    total_cost = 0
    
    if choice == 1:
        total_cost = quantity * 200
        print(f"{quantity} bottles of Tusker cost you Ksh {total_cost}")
    elif choice == 2:
        total_cost = quantity * 280
        print(f"{quantity} bottles of Pilsner cost you Ksh {total_cost}")
    elif choice == 3:
        total_cost = quantity * 320
        print(f"{quantity} bottles of Smirnoff cost you Ksh {total_cost}")
    else:
        total_cost = quantity * 180
        print(f"{quantity} bottles of White cap cost you Ksh {total_cost}")


if __name__ == "__main__":
    order_beer()
