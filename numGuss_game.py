'''Number Guessing Game is a game in which the computer randomly selects a number between 1 and 100.
The user must guess the number within a limited number of attempts. 
After each incorrect guess, the program provides a hint indicating whether the guess is too low or too high.
'''
'''Winning Rules
Computer generates a random number between 1 and 100.
User has a maximum of 7 attempts to guess the number.
User wins immediately if the guess matches the randomly generated number.
If the guess is lower than the selected number, the program displays "Too Low" and the user should try a higher number.
If the guess is higher than the selected number, the program displays "Too High" and the user should try a lower number.
Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.
If the user does not guess the number within 7 valid attempts, the game ends and reveals the correct number.

'''
import random
attempts=7

def display_rule():
    print("Your playing game")
    print("You have 7 attempt")
    return
def playing_game(number, attempt=1):
    if attempt > attempts:
        print("game over")
        print("The correct number was",number)
        return

    gusse=input(f"attempt {attempt}/7-Enter your number: ")
    try:
        gusse=(int(gusse))
    except ValueError:
        print("Please enter number")
        return playing_game(number, attempt)
    if gusse < 1 or gusse >100  :
        



