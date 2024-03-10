"""
File: subtract a square
Purpose: This is a two-player mathematical game of strategy. It is played by two
         people with a pile of coins (or other tokens) between them. The players take turns removing
         coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
         The player who removes the last coin wins.
Author:  Marco Raafat Zakaria
ID: 20231129
"""

import math  # to get built-in functions for math
import random  # this library would get you a random number


def is_number_under_sqrt(number):  # this function will check if we put the number under square root we will get a whole number or not
    sqrt_result = math.sqrt(number)
    return sqrt_result.is_integer()


print("Welcome to subtract a square game")
print("----------------------------------")
flag = True
while True :
    choice = input("A)explanation\nB)start the game\nC)exit the game\n(A/B/C): ")  # First menu
    choice = choice.upper()
    if choice == "A":  # A)explaination
        print(" explanation:\nThis is a two-player mathematical game of strategy.\n It is played by two people with a pile of coins (or other tokens) between them.\n The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...)\n The player who removes the last coin wins ")
        print("--------------------------------------------------------------------------------------------------------------------------")
    elif choice == "B":  # B)start the game
        while True:
            choice1 = input("A)choose your own maximum number of coins.\nB)The game choose you a random maximum number.\n(A/B): ").upper()  # Second menu
            if choice1 == "A":  # the user will choose his own number.
                max_number = input("enter your maximum number of coins: ")
                print(f"current number of coins are: {max_number}")
                while max_number.isdigit() == False:  # to check if the input is a number.
                    print("invalid input")
                    max_number = input("enter your maximum number of coins: ")
                break
            elif choice1 == "B":  # the game will display a random number.
                max_number = random.randint(10, 1000)  # the game will display a random number from 10 to 1000.
                print(f"current number of coins are: {max_number}")
                break
            else:  # if the user put another choices
                print("Invalid choice")
        while True:
            coins1 = input("Player 1 turn: ")
            while coins1.isdigit() == False or int(coins1) <= 0 or int(coins1) > int(max_number) or is_number_under_sqrt(int(coins1)) == False:  # to check if the input is valid.
                print("Invalid input")
                coins1 = input("Player 1 turn: ")
            while int(coins1) == int(max_number) and flag == True: # if the 1st player put a number equal to max_number in his first turn it will display invalid input and in any turn except first turn the flag will be false in line 55 so the condition will not occur.
                print("Invalid input")
                coins1 = input("Player 1 turn: ")
            else:
                max_number = int(max_number) - int(coins1)  # update max_number
                flag = False
                if int(max_number) == 0:
                    print("Player 1 wins")  # player 1 take the last number
                    print("---------------------------------------")
                    break
            print(f"Current number of coins are: {max_number}")
            coins2 = input("Player 2 turn: ")
            while coins2.isdigit() == False or int(coins2) <= 0 or int(coins2) > int(max_number) or is_number_under_sqrt(int(coins2)) == False: # to check if the input is valid.
                print("Invalid input")
                coins2 = input("Player 2 turn: ")
            max_number = int(max_number) - int(coins2)  # update max_number
            if int(max_number) == 0:
                print("Player 2 wins")  # player 2 take the last number
                print("---------------------------------------")
                break
            else:
                print(f"Current number of coins are: {max_number}")
                continue
    elif choice == "C":  # Exit the game
        break
    else:  # if the user put another choices
        print("Invalid input")