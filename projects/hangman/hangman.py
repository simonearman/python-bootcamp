import random
import string
import os

# Gallows image by me
hanged_drawing = ["   ==========",
                  "   I        |",
                  "   I",
                  "   I",
                  "   I",
                  "   I",
                  "   I",
                  "   I",
                  "=======\n"]


# Takes a string, returns a list of characters in that string
def split_string(input_string):
    str_list = []
    for char in input_string:
        str_list.append(char)
    return str_list


# Cleares the console 
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Takes the guessed letters, letters in the random word and player's lives left and draws the game out based on them
def draw_game(_guessed_letters, _word_letters, _lives):
    # Changing the hanged image based on the lives left
    if _lives == 5:
        hanged_drawing[2] = "   I        O"
    if _lives == 4:
        hanged_drawing[3] = "   I        |"
        hanged_drawing[4] = "   I        |"
    elif _lives == 3:
        hanged_drawing[3] = "   I       /|"
    elif _lives == 2:
        hanged_drawing[3] = "   I       /|\\"
    if _lives == 1:
        hanged_drawing[5] = "   I       /"
    if _lives == 0:
        hanged_drawing[5] = "   I       / \\"

    # Drawing out the word
    word_to_draw = ""
    for char in _word_letters:
        if char in _guessed_letters:
            word_to_draw += f"{char} "
        else:
            word_to_draw += "_ "
    hanged_drawing[1] = f"   I        |                 CHECKED LETTERS: {', '.join(_guessed_letters)}"
    hanged_drawing[6] = f"   I                          WORD: {word_to_draw}"
    clear_console()
    print("Welcome to hangman!\n")
    print("\n".join(hanged_drawing))


lives = 6
words_file = open("words.txt")
# Reading the file and making a list of all words with splitlines()
words = words_file.read().splitlines()
# Choosing a random word
word = random.choice(words).lower()
# Dividing the word into a list of characters
word_letters = split_string(word)
words_file.close()
guessed_letters = []

# Main gameplay code
while True:
    draw_game(guessed_letters, word_letters, lives)
    if lives <= 0:
        print(f"You didn't find the word \"{word}\" and got hanged, game over!")
        break
    # If all the word letters are in the guessed letters list, you win
    elif all(l in guessed_letters for l in word_letters):
        print("You found the word, you win!")
        break

    # Taking the user input until he enters a proper letter
    letter = input("Which letter will you check? ").lower()
    while len(letter) != 1 or letter not in string.ascii_lowercase:
        letter = input(f"\"{letter}\" is not a proper single-character letter.\nGive me another letter ").lower()

    # Checking if the letter is correct
    if letter in guessed_letters:
        lives -= 1
    elif letter not in word_letters:
        lives -= 1
        guessed_letters.append(letter)
    else:
        guessed_letters.append(letter)
