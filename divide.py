# Write a program that accepts two numbers and divides the bigger number by the 
# smaller number and displays the results. The program should display an error 
# message (and not perform the calculation) if the smaller number is zero.in

def divide_numbers():
    numbers = input("Enter two numbers separated by a comma:")
    num1, num2 = map(int, numbers.split()) 
    
    min_num = min(num1, num2)
    if min_num == 0:
        print("Division by 0 is not allowed")
        return
    
    if num1 > num2:
        
        result = num1 / num2
    else:
        result = num2 / num1
        
        
    print("Result of division:", result)


if __name__ == "__main__":
    divide_numbers()