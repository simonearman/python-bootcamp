print("Welcome to Caesar cipher!")


def caesar(_message, _shift, _mode):
    new_message = ""
    if _mode == "decrypt":
        _shift *= -1
    for char in _message:
        # Checking if the character is a letter
        if (ord(char) > 96 and ord(char) < 123) or (ord(char) > 64 and ord(char) < 91):
            # Getting the letter ID, where "a" is 0 and "z" is 25
            letter_id = ord(char.lower()) - 97
            # Checking if the shifted ID will be outside of the 0-25 range, looping around if needed
            if letter_id + _shift > 25:
                new_message += chr(ord(char) + _shift - 26)
            elif letter_id + _shift < 0:
                new_message += chr(ord(char) + _shift + 26)
            else:
                new_message += chr(ord(char) + _shift)
        # If not a letter just rewrite the character
        else:
            new_message += char
    return new_message


# Asks for a number until valid
def ask_shift():
    shift = input("By how much would you like to shift the message? ")
    while not shift.isdigit():
        shift = input(f"\"{shift}\" is not a number. Type in a positive integer to shift the message: ")
    # We can use modulo of 26 as any shift+26x will bring the same encryption output
    return int(shift)%26


# Asks for either encryption or decryption until valid, allows for abbreviations
mode = input("Type \"encrypt\" to encrypt or \"decrypt\" to decrypt a message: ").lower()
while mode == "" or not ("encrypt".startswith(mode) or "decrypt".startswith(mode)):
    mode = input(f"\"{mode}\" is not an option. Type in either \"encrypt\" or \"decrypt\": ")

# Sets the mode name right for the print function
if "encrypt".startswith(mode):
    mode = "encrypt"
else:
    mode = "decrypt"
    
message = input(f"Type in the message you want to {mode}: ")
print(f"The {mode}ed message is:\n{caesar(message, ask_shift(), mode)}")
