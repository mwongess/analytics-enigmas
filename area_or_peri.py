from tabulate import tabulate

cols = ["Figures"]
figures = [["1. cirlce"],["2. rectangle"], ["3. right-angled triangle"]]

def calc_area_or_peri():
    print(tabulate(figures, headers=cols))
    
    choice = input("Please chooce the type of the figure")
    if choice in [1, 2, 3]:
        if choice == 1:
            # Circle
            radius = float(input("Please enter radius"))
            area = ""
            perimeter = ""
        elif choice == 2:
            # Rectangle
            length = float(input("Please enter radius"))
            width = float(input("Please enter radius"))
            area = ""
            perimeter = ""
        elif choice == 3:
            # Right-angled triangle
            base = float(input("Please enter radius"))
            height = float(input("Please enter radius"))
            area = ""
            perimeter = ""

if __name__ == "__main__":
    calc_area_or_peri()