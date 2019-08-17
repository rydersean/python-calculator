import GetUserInput as getInput
import Calculations as calc

another_turn = True
while another_turn:
    # Get User Input
    user_first_number = getInput.getFirstNumber()
    user_operator = getInput.getOperator()
    user_second_number = getInput.getLastNumber()

    # Perform calculation and output results for user
    if user_operator == '+':
        print(calc.addition(user_first_number, user_second_number))
    elif user_operator == '-':
        print(calc.subtraction(user_first_number, user_second_number))
    elif user_operator == '*' or user_operator == 'x':
        print(calc.multiplication(user_first_number, user_second_number))
    else:
        print(calc.division(user_first_number, user_second_number))

    user_turn_choice = input("Do you want to quit? (q to quit) ")
    if user_turn_choice == 'q':
        another_turn = False
