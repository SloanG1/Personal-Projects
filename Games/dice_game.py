"""
This program was written by Gavin Sloan
February 25th, 2022
This program demonstrates a very simple dice game with computer and user mechanics
"""

import random

print("Welcome to the dice game!")
print()
print("You will be trying to guess the roll of the die")
print("that the computer has already prerolled")
print()
print("You will be asked how many max tries you would like,\nas well as how many dice you would like to guess for")
print()
print("When guessing the number,\nplease enter your guess in words instead of numbers, thank you")

def computer():
    print()
    print("COMPUTER MODE")
    tries = int(input("how many tries would you like to have?"))
    print("Max tries: " + str(tries))
    dice_number = int(input("how many dice would you like to have?"))
    while dice_number > 10:
        dice_number = int(input("Please enter a number less than 10:"))
    print("Number of dice guessed for: " + str(dice_number))
    counter = 0
    while counter < tries:
        while True:
            counter += 1
            roll1 = random.choice (["one","two","three","four","five","six"])
            roll2 = random.choice (["one","two","three","four","five","six"])
            roll3 = random.choice (["one","two","three","four","five","six"])
            roll4 = random.choice (["one","two","three","four","five","six"])
            roll5 = random.choice (["one","two","three","four","five","six"])
            roll6 = random.choice (["one","two","three","four","five","six"])
            roll7 = random.choice (["one","two","three","four","five","six"])
            roll8 = random.choice (["one","two","three","four","five","six"])
            roll9 = random.choice (["one","two","three","four","five","six"])
            roll10 = random.choice (["one","two","three","four","five","six"])
            rolls = (roll1, roll2, roll3, roll4, roll5, roll6, roll7, roll8, roll9, roll10)
            total_rolls = rolls[:dice_number]
            guess1 = random.choice (["one","two","three","four","five","six"])
            guess2 = random.choice (["one","two","three","four","five","six"])
            guess3 = random.choice (["one","two","three","four","five","six"])
            guess4 = random.choice (["one","two","three","four","five","six"])
            guess5 = random.choice (["one","two","three","four","five","six"])
            guess6 = random.choice (["one","two","three","four","five","six"])
            guess7 = random.choice (["one","two","three","four","five","six"])
            guess8 = random.choice (["one","two","three","four","five","six"])
            guess9 = random.choice (["one","two","three","four","five","six"])
            guess10 = random.choice (["one","two","three","four","five","six"])
            if dice_number == 1:
                guess = guess1
                total_rolls = roll1
            if dice_number == 10:
                guess = (guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, guess10)
            elif dice_number >= 9:
                guess = (guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9)
            elif dice_number >= 8:
                guess = (guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8) 
            elif dice_number >= 7:
                guess = (guess1, guess2, guess3, guess4, guess5, guess6, guess7)
            elif dice_number >= 6:
                guess = (guess1, guess2, guess3, guess4, guess5, guess6)
            elif dice_number >= 5:
                guess = (guess1, guess2, guess3, guess4, guess5)
            elif dice_number >= 4:
                guess = (guess1, guess2, guess3, guess4)
            elif dice_number >= 3:
                guess = (guess1, guess2, guess3)
            elif dice_number >= 2:
                guess = (guess1, guess2)
            elif dice_number < 2:
                guess = (guess1)
            print()
            print("Rolls remaining: " + str(tries - counter))
            print("roll number: " + str(total_rolls))
            print("guess number: " + str(guess))
            print()
            break
        if counter >= tries:
            print("Counter passed tries, simulation failed")
            break
        if guess == total_rolls:
            print("End of simulation, it took you " + str(counter) + " tries")
            break
        
def user():
    print()
    print("USER MODE:")
    tries = int(input("how many tries would you like to have?"))
    print("Max tries: " + str(tries))
    dice_number = int(input("how many dice would you like to have?"))
    print("Number of dice guessed for: " + str(dice_number))
    while dice_number > 10:
        dice_number = int(input("Please enter a number less than 10:"))
    counter = 0
    while counter < tries:
        counter += 1
        roll1 = random.choice (["one","two","three","four","five","six"])
        roll2 = random.choice (["one","two","three","four","five","six"])
        roll3 = random.choice (["one","two","three","four","five","six"])
        roll4 = random.choice (["one","two","three","four","five","six"])
        roll5 = random.choice (["one","two","three","four","five","six"])
        roll6 = random.choice (["one","two","three","four","five","six"])
        roll7 = random.choice (["one","two","three","four","five","six"])
        roll8 = random.choice (["one","two","three","four","five","six"])
        roll9 = random.choice (["one","two","three","four","five","six"])
        roll10 = random.choice (["one","two","three","four","five","six"])
        rolls = (roll1, roll2, roll3, roll4, roll5, roll6, roll7, roll8, roll9, roll10)
        total_rolls = rolls[:dice_number]
        if dice_number == 1:
            guess = (input("What do you think the roll was?"))
        if dice_number == 1:
            total_rolls = roll1 
        if dice_number == 10:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"), input("What do you think the fifth roll was?"), input("What do you think the sixth roll was?"), input("What do you think the seventh roll was?"), input("What do you think the eight roll was?"), input("What do you think the ninth roll was?"), input("What do you think the tenth roll was?"))
        elif dice_number >= 9:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"), input("What do you think the fifth roll was?"), input("What do you think the sixth roll was?"), input("What do you think the seventh roll was?"), input("What do you think the eight roll was?"), input("What do you think the ninth roll was?"))
        elif dice_number >= 8:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"), input("What do you think the fifth roll was?"), input("What do you think the sixth roll was?"), input("What do you think the seventh roll was?"), input("What do you think the eight roll was?"))
        elif dice_number >= 7:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"), input("What do you think the fifth roll was?"), input("What do you think the sixth roll was?"), input("What do you think the seventh roll was?"))
        elif dice_number >= 6:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"), input("What do you think the fifth roll was?"), input("What do you think the sixth roll was?"))
        elif dice_number >= 5:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"), input("What do you think the fifth roll was?"))   
        elif dice_number >= 4:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"), input("What do you think the fourth roll was?"))
        elif dice_number >= 3:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"), input("What do you think the third roll was?"))
        elif dice_number >= 2:
            guess = (input("What do you think the first roll was?"), input("What do you think the second roll was?"))
        print()
        print("Rolls remaining: " + str(tries - counter))
        print("roll number: " + str(total_rolls))
        print("guess number: " + str(guess))
        print() 
        if guess == total_rolls:
            print("End of simulation, it took you " + str(counter) + " tries")
            break
        if counter >= tries:
            print("I'm sorry, you failed the simulation")
            break
terminate = "no"
while terminate == "no":
    start_menu = input("type computer for computer play or user for user play.")
    if start_menu == "computer":
        computer()
    if start_menu == "user":
        user()
    terminate = input("Would you like to exit the simulation?")
    if terminate == "yes":
         break  
