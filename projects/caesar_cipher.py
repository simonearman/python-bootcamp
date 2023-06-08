print("Welcome to Caesar cipher!")


def caesar(_message, _shift, _mode):
    new_message = ""
    for char in _message:
        # Checking if the character is a letter
        if (ord(char) > 96 and ord(char) < 123) or (ord(char) > 64 and ord(char) < 91):
            # Getting the letter ID, where "a" is 0 and "z" is 25
            letter_id = ord(char.lower()) - 97
            # Checks if the mode is encryption
            if _mode == "encrypt":
                # Checking if the shift will move the letter ID above 25, in which case it loops around the count
                if letter_id + _shift < 26:
                    new_message += chr(ord(char) + _shift)
                else:
                    new_message += chr(ord(char) + _shift - 26)
            # Else, the mode is decryption
            else:
                # Checking if the shift will move the letter ID below 0, in which case it loops around the count
                if letter_id - _shift >= 0:
                    new_message += chr(ord(char) - _shift)
                else:
                    new_message += chr(ord(char) - _shift + 26)
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
