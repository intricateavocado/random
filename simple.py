import random
from words import words

def guessnum():
    guessed = False
    guess_num = 0
    computer_number = random.randint(1, 100)
    while guessed == False:
        guess = input("Guess the number: ")
        guess_num += 1
        if int(guess) == computer_number:
            print("You guessed the correct number!")
            print("It took you " + str(guess_num) + " guesses to enter the correct number.")
            guessed = True
        elif int(guess) < computer_number:
            print("Your guess is too low, guess again.")
        else: #int(guess) > computer_number
            print("Your guess is too high, guess again.")


def rockpaperscissors():
    userscore = 0
    computerscore = 0
    playing = True
    print("Welcome to Rock Paper Scissors!")
    rps = ['rock', 'paper', 'scissors']
    while playing:
        print(" ")
        print(f"     Score    ")
        print(f"______________")
        print(f"|User|Computer|")
        print(f"|----|--------|")
        print(f"|__{userscore}_|____{computerscore}___|")
        print(" ")
        userchoice = input("Enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
        computerchoice = random.choice(rps)
        #r > s, p > r, s > p, 
        if (userchoice == 'r' and computerchoice == 'scissors') or (userchoice == 'p' and computerchoice == 'rock') or (userchoice == 's' and computerchoice == 'paper'):
            userscore += 1
            print(f"You won! The computer chose {computerchoice}.")
        elif userchoice == computerchoice:
            print(f"You tied! You both chose {computerchoice}.")
        else: 
            computerscore += 1
            print(f"You lost! The computer chose {computerchoice}.")
        if (userscore == 5):
            print('You have won the game! :D')
            break
        elif (computerscore == 5):
            print('You have lost the game! :(')
            break


def temperature():
    def convert():
        global selection
        choice = False
        while choice == False:
            print("Please enter your choice for conversion.")
            selection_input = input("1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit: ")
            if selection_input == '1':
                selection = 'C'
                choice = True
            elif selection_input == '2':
                selection = 'F'
                choice = True
            else:
                print("That was not an option. Please try again.")
                choice = False
        return selection

    def f2c():
        f = int(input("Enter the Fahrenheit temperature to convert: "))
        print("Converting...")
        c = (f - 32) * (5/9)
        print("Done!")
        print(f"{f}°F converts to {c}°C.")

    def c2f():
        c = int(input("Enter the Celsius temperature to convert: "))
        print("Converting...")
        f = (c * 9/5) + 32
        print("Done!")
        print(f"{c}°C converts to {f}°F.")


    convert()
    if selection == 'C':
        f2c()
    else:
        c2f()


def randword():
    word_number = random.randint(0, 2465)
    word_pick = words[word_number]
    print(f"Word #{word_number}: {word_pick}")
