# Day 2: operations, conditionals and input()

# Basic excercise:
#   Ask the user two numbers
#   Return the bigger one and print if the bigger one is even or odd

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 == number2:
    print("Both numbers are equal.")
elif number1 > number2:
    bigger_number = number1
else:
    bigger_number = number2

if number1 != number2:
    if bigger_number % 2 == 0:
        print(f"The bigger number {bigger_number} is even.")
    else:
        print(f"The bigger number {bigger_number} is odd.")

# Mini-project: Age simulator + discount:
#   Ask the user for their age
#   If the user is under 12, print a message saying free entry
#   If the user is between 12 and 17, print a message saying price is $5
#   If the user is elder than 18, print a message saying price is $10
#   If the user is elder than 65, print a message saying price is 50% discount

age = int(input("Enter your age: "))
if age < 12:
    print("Free entry!")
elif 12 <= age <= 17:
    print("Price is $5.")
elif age > 65:
    print("50% discount")
else:
    print("Price is $10.")
    