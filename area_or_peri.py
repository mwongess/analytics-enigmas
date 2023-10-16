# Write a program that computes the area & perimeter of either a rectangle, a circle or 
# a right-angled triangle. The program should display a menu that enables the user to 
# select the type of figure whose area & perimeter he/she wants to compute. Depending 
# on the users choice, the program should prompt for the dimensions and perform the 
# computations. The output should be: - The type of figure, the dimensions, the area 
# and the perimeter. (NB:The calculation should be for only one figure at any one 
# time.

import math
from tabulate import tabulate

cols = ["Figures"]
figures = [["1. cirlce"],["2. rectangle"], ["3. right-angled triangle"]]

def calc_area_or_peri():
    print(tabulate(figures, headers=cols))
    
    choice = int(input("Please chooce the type of the figure:"))
    if choice in [1, 2, 3]:
        if choice == 1:
            radius = float(input("Please enter radius:"))
            area = math.pi * (radius ** 2)
            perimeter = 2 * math.pi * radius
        elif choice == 2:
            length = float(input("Please enter the rectangle length:"))
            width = float(input("Please enter the rectangle width:"))
            area = length * width
            perimeter = 2 * (length + width)
        elif choice == 3:
            base = float(input("Please enter the triangle base:"))
            height = float(input("Please enter the triangle height:"))
            area = 0.5 * base * height
            perimeter = base + height + math.sqrt(base**2 + height**2)

if __name__ == "__main__":
    calc_area_or_peri()