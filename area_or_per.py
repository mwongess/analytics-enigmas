from tabulate import tabulate

cols = ["Figures"]
figures = [["1. cirlce"],["2. rectangle"], ["3. right-angled triangle"]]

def calc_area_or_peri():
    print(tabulate(figures, headers=cols))
    
    choice = input("Please chooce the type of the figure")
    if choice in [1, 2, 3]:
        if choice == 1:
            # Circle
            area = ""
            perimeter = ""
        elif choice == 2:
            # Rectangle
            area = ""
            perimeter = ""
        elif choice == 3:
            # Right-angled triangle
            area = ""
            perimeter = ""

if __name__ == "__main__":
    calc_area_or_peri()