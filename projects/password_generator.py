from random import randint

print("Welcome to the random password generator")
password_len = int(input("How long would you like the password to be? "))
if password_len < 1:
    print("The password needs to have at least one character")
    exit()
use_lower = input("Would you like to use lowercase letters? (Yes or No) ").lower()
use_capital = input("Would you like to use uppercase letters? (Yes or No) ").lower()
use_numbers = input("Would you like to use numbers? (Yes or No) ").lower()
use_symbols = input("Would you like to use symbols? (Yes or No) ").lower()

# Possible characters
chars_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
chars_cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&"]

# Filling the empty characters list with characters we want to use
characters = []
if use_lower == "yes" or use_lower == "y":
    characters.extend(chars_low)
if use_capital == "yes" or use_capital == "y":
    characters.extend(chars_cap)
if use_numbers == "yes" or use_numbers == "y":
    characters.extend(numbers)
if use_symbols == "yes" or use_symbols == "y":
    characters.extend(symbols)
if len(characters) == 0:
    print("Sadly, I can't make a password without any characters to use")
    exit()

# Generating the password
password = ""
while password_len > 0:
    random_char = characters[randint(0, len(characters) - 1)]
    password += random_char
    password_len -= 1

print(f"\nGenerated password: {password}")
