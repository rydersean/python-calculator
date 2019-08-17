import re

def getFirstNumber():
    # Get first number from user input and check its a number
    user_first_number = input("Enter your number: ")
    val = re.search('^[0-9]+$', user_first_number)

    while not val:
        user_first_number = input("Enter your number again: ")
        val = re.search('^[0-9]+$', user_first_number)

    return int(user_first_number)

def getOperator():
    # Get the operator (x, /, +, -) from user input and check its an operator
    user_operator = input("Enter (x, /, + or -): ")
    val = re.search('^[x/+-]{1}$', user_operator)

    while not val:
        user_operator = input("Enter (x, /, + or -) again: ")
        val = re.search('^[x/+-]{1}$', user_operator)

    return user_operator

def getLastNumber():
    # Get the second number from the user input and check if its a number

    user_second_number = input("Enter your number: ")
    val = re.search('^[0-9]+$', user_second_number)

    while not val:
        user_second_number = input("Enter your number again: ")
        val = re.search('^[0-9]+$', user_second_number)

    return int(user_second_number)