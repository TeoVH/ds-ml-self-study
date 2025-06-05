# Day 5: Dictionaries

# Imports from past exercises
from day4 import calculate_average


# Basic exercise: basic dictionaries
#   Create a dictionary to store a student's name, age, and grades
#   Check if the student is approved based on the average of their grades
#   Print the student's name, average grade, and approval status

student = {
    'name': 'TeoVH',
    'age': 21,
    'grades': [5, 4.8, 4.6, 4.4],
}

if calculate_average(student['grades']) < 3:
    student['Approved'] = False
else:
    student['Approved'] = True

print(f"Student: {student['name']}\nAverage Grade: {calculate_average(student['grades']):.2f}\nApproved: {student['Approved']}")


# Basic exercise: brows dictionaries
#   Create a dictionary to store the inventory
#   Print the quantity of each ingredient in the inventory

inventory = {
    'bread': 10,
    'tomato': 5,
    'cheese': 8,
    'lettuce': 12,
    'ham': 6,
}

for ingredient, quantity in inventory.items():
    print(f"There are {quantity} {ingredient} in the inventory")


# Basic exercise: update and delete dictionary items
#   Update the quantity of an ingredient in the inventory
#   Add a new ingredient to the inventory
#   Delete an ingredient from the inventory

inventory['tomato'] = 10
inventory['ribs'] = 7
inventory.update({'ham': 10})
del inventory['lettuce']
# Print the updated inventory
print(inventory)
print('\n')


# Mini-project: Contact book
#   Create a contact book using a dictionary
#   Implement the following functionalities:
#     1. View all contacts
#     2. Search for a contact by name
#     3. Add a new contact
#     4. Delete a contact
#     5. Exit the program

contacts = {
    'contact1': '111-1111',
    'contact2': '222-2222',
    'contact3': '333-3333',
    'contact4': '444-4444',
    'contact5': '555-5555',
}

while(True):
    print('--------------------------------')
    print('|             MENU             |')
    print('--------------------------------')
    print('|                              |')
    print('| 1. View all contacts         |')
    print('| 2. Search contact(name)      |')
    print('| 3. Add new contact           |')
    print('| 4. Delete contact            |')
    print('| 5. Exit                      |')
    print('--------------------------------')

    try:
        menu_option = int(input("Select an option: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if menu_option == 1:
        for key, value in contacts.items():
            print(f"{key}: {value}")
        print("\n")
    elif menu_option == 2:
        contact_name = input("Contact-name: ")
        if contact_name in contacts:
            print(f"The number of {contact_name} is: {contacts[contact_name]}\n")
        else:
            print("Contact does not exist\n")
    elif menu_option == 3:
        contact_name = input("Contact-name: ")
        if contact_name in contacts:
            print("Contact already exists\n")
        else:
            contact_number = input("Contact-number (xxx-xxxx): ")
            contacts[contact_name] = contact_number
            print(f"Contact {contact_name} saved successfully\n")
    elif menu_option == 4:
        contact_name = input("Contact-name: ")
        if contact_name in contacts:
            del contacts[contact_name]
            print("Contact deleted successfully\n")
        else:
            print("Unable to delete non-existent contact\n")
    elif menu_option == 5:
        print("See you!")
        break
    else:
        print("Select a correct option\n")
