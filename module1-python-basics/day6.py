# Day 6: Advanced Control Structures - Combined Loops and Conditions

# Basic exercise: combined use of loops and conditions
#   Create a list of numbers from 1 to 20
#   Print the numbers that are greater than 10 and divisible by 3

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in numbers_1:
    if number > 10 and (number % 3) == 0:
        print(number)


# Intermediate exercise: Condition-controlled counter
#   Create a program that asks the user to input a password
#   The user has 3 attempts to enter the correct password
#   If the user enters the correct password, print "Access granted"
#   If the user enters the wrong password, print "Access denied" after 3 attempts

password = 'TeoVH'
password_counter = 3

while (True):
    password_input = input("Insert the password: ")
    if password_input == password:
        print("Access granted")
        break
    elif password_counter == 1:
        print("Access denied")
        break
    else:
        password_counter -= 1
        print(f"Incorrect password. Attempts left: {password_counter}")
        continue


# Intermediate exercise: filtered sum
#   Create a list of numbers positive and negative
#   Calculate the sum of the positive numbers until the sum be greater than or equal to 100
#   Print the result

numbers_2 = [-100, 0, -90, 5, -80, 10, -70, 15, -60, 20, -50, 25, -40, 30, -30, 35, -20, 40]
result = 0
numbers_list = []

for number in numbers_2:
    if result >= 100:
        print(f"The numbers used to calculate the result are: {numbers_list}")
        print(f"The result is: {result}")
        break
    elif number > 0:
        result += number
        numbers_list.append(number)
        continue


# Mini-project: ATM (simple simulation)

balance = 1000.00
transactions = {}
withdraw_number = 0
deposit_number = 0

while (True):
    print('--------------------------------')
    print('|             MENU             |')
    print('--------------------------------')
    print('|                              |')
    print('| 1. See balance               |')
    print('| 2. Withdraw money            |')
    print('| 3. Deposit money             |')
    print('| 4. See transactions          |')
    print('| 5. Exit                      |')
    print('--------------------------------')

    try:
        menu_option = int(input("Select an option: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if menu_option == 1:
        print(f"Your balance is: {balance:.2f}")
        continue
    elif menu_option == 2:
        try:
            withdraw = float(input("Insert the amount to withdraw: "))
        except ValueError:
            print("Please enter a correct value")
            continue

        if balance >= withdraw:
            balance -= withdraw
            print("Money successfully withdrawn")
            print(f"Your new balance is: {balance:.2f}")
            transactions[f'withdraw {withdraw_number + 1}'] = withdraw
            withdraw_number += 1
        else:
            print("Not enough money")
    elif menu_option == 3:
        try:
            deposit = float(input("Insert the amount to deposit: "))
        except ValueError:
            print("Please enter a correct value")
            continue

        if deposit > 0:
            balance += deposit
            print("Money successfully deposited")
            print(f"Your new balance is: {balance:.2f}")
            transactions[f'deposit {deposit_number + 1}'] = deposit
            deposit_number += 1
        else:
            print("Please enter a positive value")
    elif menu_option == 4:
        if transactions:
            print("Your transactions:")
            for transaction_type, amount in transactions.items():
                print(f"{transaction_type.capitalize()}: {amount:.2f}")
        else:
            print("No transactions made yet")
    elif menu_option == 5:
        print("See you!")
        break
    else:
        print("Select a correct option\n")
