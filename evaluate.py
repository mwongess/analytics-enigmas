def evaluate():
    try:
        numbers =input("Enter two numbers:")
        num1, num2 = map(float, numbers.split())
        operator = input("Enter an operator:")
        # if operator not in ["/", "*", "%", "+", "-"]:
        #     print("An operator must be one of /, *, %, + or -")
        if operator == "+":
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Division by zero is not allowed.")
                return
            result = num1 / num2
        elif operator == '%':
            if num2 == 0:
                print("Modulo by zero is not allowed.")
                return
            result = num1 % num2
        else:
            print("Invalid operator. Please enter +, -, *, /, or %.")
            return

        print(f"Result: {num1} {operator} {num2} = {result:.2f}")
 
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        
if __name__ == "__main__":
    evaluate()