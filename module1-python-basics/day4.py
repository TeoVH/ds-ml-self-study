# Day 4: Functions

# Basic exercise: basic functions
#   Create a function that prints a personalized greeting
#   Create a function that checks if a number is even or odd
#   Create a function that multiplies two numbers and returns the result

def personalized_greeting(name):
    """Prints a personalized greeting."""
    print(f"Hello, {name}!")

personalized_greeting("TeoVH")


def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

print(is_even(13))
print(is_even(24))


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print(multiply(3, 4))


# Basic exercise: more functions
#   Create a function that prints each food in a menu
#   Create a function that calculates the average of a list of grades
#   Create a function that classifies the average grade and returns a message

def print_menu(menu):
    """Prints each food in the menu."""
    if not menu:
        print("The menu is empty.")
        return
    for food in menu:
        print(f"Dish: {food}")

menu = ["Burger", "Pizza", "Fries", "Ribs", "Fried Chicken"]
print_menu(menu)


def calculate_average(grades):
    """Calculates the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def classify_average(average):
    """Classifies the average grade and returns a message."""
    if average < 3:
        return f"Your final grade is {average:.2f}. You failed."
    elif average > 4.5:
        return f"Your final grade is {average:.2f}. Extraordinary performance!"
    else:
        return f"Your final grade is {average:.2f}. You approved."

grades1 = [1.0, 1.5, 2.0, 2.5, 3.0]
grades2 = [5.0, 4.5, 4.0, 3.5, 3.0]
grades3 = [4.6, 4.7, 4.8, 4.9, 5.0]

average1 = calculate_average(grades1)
average2 = calculate_average(grades2)
average3 = calculate_average(grades3)

print(classify_average(average1))
print(classify_average(average2))
print(classify_average(average3))


# Mini-project: Grade calculator (with functions)
#   Ask the user to enter 5 grades and store them in a list
#   Use the calculate_average function to calculate the average of the grades
#   Use the clasify_average function to classify the average grade and print the result 

grades = []

print("\nWelcome to the grade calculator")
while len(grades) < 5:
    grade = float(input(f"Enter grade {len(grades) + 1} (0-5): "))
    if grade < 0 or grade > 5:
        print("Invalid grade. Please enter a grade between 0 and 5.")
        continue
    else:
        grades.append(grade)

average = calculate_average(grades)
print(classify_average(average))


# Bonus exercise: temperature conversion function
#   Create a function that converts temperatures between Celsius and Fahrenheit
#   The function should take three parameters: degrees, origin_unit, and target_unit

def convert_temperature(degrees, origin_unit, target_unit):
    """Converts a list of temperatures from one unit to another."""
    if origin_unit.lower() == target_unit.lower():
        return f"{degrees}° {origin_unit}"
    elif origin_unit.lower() == ("c") and target_unit.lower() == ("f"):
        return degrees * 1.8 + 32
    elif origin_unit.lower() == ("f") and target_unit.lower() == ("c"):
        return (degrees - 32) / 1.8
    else:
        return "Invalid units. Please use 'c' for Celsius or 'f' for Fahrenheit."

print(convert_temperature(100, 'c', 'F'))
print(convert_temperature(212, 'f', 'C'))
