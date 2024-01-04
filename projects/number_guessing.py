from random import randint


def is_int(var):
    """Returns True if the variable can be changed to an integer, returns False otherwise"""
    if var is None:
        return False
    try:
        int(var)
        return True
    except ValueError:
        return False


def ask_for_number():
    """Returns the number entered by the player. Asks until a valid number has been entered."""
    guess = input("Guess the number: ")
    while not is_int(guess) or int(guess) < 1 or int(guess) > 100:
        print("You can only input a number from 1 to 100.")
        guess = input("Guess the number: ")
    return int(guess)


print("Welcome to the number guessing game!")
print("I'm thinking of a number from 1 to 100.")
print("You have 5 attempts to guess the number.")
the_number = randint(1, 100)
life = 5
did_win = False

# Main game body
player_guess = ask_for_number()
while life > 0 and not did_win:
    if player_guess == the_number:
        print("You've guessed the number! Good game.")
        did_win = True
    else:
        life -= 1
        if life < 1:
            print(f"You have run out of lives. The number was {the_number}.")
        else:
            if player_guess > the_number:
                print("Too high.")
            else:
                print("Too low.")
            print(f"You have {life} more attempts.")
            player_guess = ask_for_number()
