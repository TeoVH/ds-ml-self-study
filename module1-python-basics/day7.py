# Modules and Exceptions in Python

# Importing the math module
from math import sqrt, sin

#Importing math_utils module made by the user
from math_utils import add, subtract, multiply, divide


# Basic exercise: Calculate the square root and sine of a number using the math module
def calculate_sqrt(number):
    """Calculate the square root of a number."""
    return sqrt(number)

def calculate_sin(number):
    """Calculate the sine of a number (in radians)."""
    return sin(number)


# Miniproject: Advanced calculator
#   This calculator performs basic arithmetic operations and handles exceptions.
#   It allows users to choose an operation and input numbers, while also handling invalid inputs gracefully.

def advanced_calculator():
    """A simple advanced calculator that performs basic arithmetic operations."""
    while True:
        print("-----------------------------------------------------------------")
        print("|              Welcome to the Advanced Calculator!              |")
        print("-----------------------------------------------------------------")
        print("| Available operations:                                         |")
        print("|  1. Add (+)                                                   |")
        print("|  2. Subtract (-)                                              |")
        print("|  3. Multiply (*)                                              |")
        print("|  4. Divide (/)                                                |")
        print("|  5. Exit                                                      |")
        print("-----------------------------------------------------------------")

        operation = input("Please choose an operation: ")
        
        if operation not in ['+', '-', '*', '/', '1', '2', '3', '4', '5']:
            print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}. Please enter valid numbers.")
        
        if operation == '+' or operation == '1':
            print(f"{a} + {b} = {add(a, b)}")
        elif operation == '-' or operation == '2':
            print(f"{a} - {b} = {subtract(a, b)}")
        elif operation == '*' or operation == '3':
            print(f"{a} * {b} = {multiply(a, b)}")
        elif operation == '/' or operation == '4':
            if b == 0:
                print("Error: Cannot divide by zero.")
                continue
            else:
                print(f"{a} / {b} = {divide(a, b)}")
        elif operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")


# Example usage
if __name__ == "__main__":
    try:
        number = float(input("Enter a number to calculate its square root and sine: "))
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")
        exit(1)
    
    print(f"The square root of {number} is {calculate_sqrt(number)}")
    print(f"The sine of {number} radians is {calculate_sin(number):.3f}")


    # Example usage of the math_utils module
    try:
        a = float(input("Enter first number for arithmetic operations: "))
        b = float(input("Enter second number for arithmetic operations: "))
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid numbers.")
        exit(1)

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")
    # print(f"Division by zero: {divide(a, 0)}")  # This will raise an exception

    # Run the advanced calculator
    advanced_calculator()