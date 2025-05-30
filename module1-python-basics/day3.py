# Day 3: Lists and Loops

# Basic exercise (lists):
#   Create a list of menu foods
#   Print a sentence for each food in the list
#   Add a new food to the list
#   Print the total number of dishes in the menu

menu = ["Burger", "Pizza", "Fries", "Ribs", "Fried Chicken"]

for food in menu:
    print(f"I love to eat {food}.")

menu.append("Sushi")

print(f"There are {len(menu)} dishes in the menu.")


# Basic exercise (for loop):
#   Print the numbers from 1 to 10
#   Print the multiplication table of 5

for i in range(1, 11):
    print(f"Number: {i}")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# Basic exercise (while loop):
#   Ask the user to enter a password
#   If the password is correct, print a welcome message and exit the loop
#   If the password is incorrect, print an error message and ask again

password = "python123"

while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Welcome! You have entered the correct password.")
        break
    else:
        print("Incorrect password, try again.")


# Mini-project: grade point average calculator
#   Ask the user to enter 5 grades
#   Calculate the average of the grades
#   If the average is less than 3, print a message saying the user failed
#   If the average is greater than 4.5, print a message saying the user had an extraordinary performance
#   Otherwise, print a message saying the user approved

grades = []

while len(grades) < 5:
    grade = float(input(f"Enter grade {len(grades) + 1}: "))
    if grade < 0 or grade > 5:
        print("Invalid grade. Please enter a grade between 0 and 5.")
        continue
    else:
        grades.append(grade)

average = sum(grades) / len(grades)
if average < 3:
    print(f"Your final grade is {average:.2f}. You failed.")
elif average > 4.5:
    print(f"Your final grade is {average:.2f}. Extraordinary performance!")
else:
    print(f"Your final grade is {average:.2f}. You approved.")
