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
        except ValueError: 
            print("Invalid choice.Please enter 1, 2, 3 or 4")



    #
    while True: 
        try: 
            quantity = int(input("How many bottles do you want? ")) 
        except ValueError: 
            print("Quantity cant be below 0")

if __name__ == "__main__":
   order_beer()