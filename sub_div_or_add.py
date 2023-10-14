# Write a program that prompts the user for two numbers and then computes them 
# using the following rules. If the first number is greater than the second one, the 
# second number is subtracted from the first one. If the second number is greater than 
# the first one, the first number is divided by the second one. Otherwise the two 
# numbers are added

def sub_div_or_add():
    try:
        numbers = input("Please Enter your two numbers:")
        num1, num2 = map(float, numbers.split())

        if num1 > num2:
            result = num1 - num2
        elif num2 > num1 :
            result = num1 / num2
        else:
            result = num1 + num2
        
        print(result)   
    except ValueError:
        print("Enter valid numbers!!")
        
if __name__ == "__main__":
    sub_div_or_add()