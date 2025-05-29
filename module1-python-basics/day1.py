# Day 1: data types and variables

# Integer
number = 10
# Float
decimal_number = 10.5
# String
text = "Hello, World!"
# Boolean
is_active = True
# List
fruits = ["apple", "banana", "cherry"]

# operations with variables
number -= 5
number += 2

# printing a sentence with the variables
print(f"{text} mi favorite number is {number} and I like {fruits[0]}.")

# simulating a ministore
# Variables
product_name = "Apple"
unit_price = 0.5

# Input from user
amount = int(input('How many apples do you want to buy? '))

# Calculate total price
total = unit_price * amount

# Print the result
print(f"You bought {amount} {product_name}(s) at ${unit_price} each. Total: ${total:.2f}")
