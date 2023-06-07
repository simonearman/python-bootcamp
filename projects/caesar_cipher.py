print("Welcome to Caesar cipher!")


def encrypt(_message, _shift):
    encrypted_message = ""
    for char in _message:
        # Checking if the character is a letter
        if (ord(char) > 96 and ord(char) < 123) or (ord(char) > 64 and ord(char) < 91):
            # Getting the letter ID, where "a" is 0 and "z" is 25
            letter_id = ord(char.lower()) - 97
            # Checking if the shift will move the letter ID above 25, in which case it loops around the count
            if letter_id + _shift < 26:
                encrypted_message += chr(ord(char) + _shift)
            else:
                encrypted_message += chr(ord(char) + _shift - 26)
        # If not a letter just rewrite the character
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(_message, _shift):
    decrypted_message = ""
    for char in _message:
        # Checking if the character is a letter
        if (ord(char) > 96 and ord(char) < 123) or (ord(char) > 64 and ord(char) < 91):
            # Getting the letter ID, where "a" is 0 and "z" is 25
            letter_id = ord(char.lower()) - 97
            # Checking if the shift will move the letter ID below 0, in which case it loops around the count
            if letter_id - _shift >= 0:
                decrypted_message += chr(ord(char) - _shift)
            else:
                decrypted_message += chr(ord(char) - _shift + 26)
        # If not a letter just rewrite the character
        else:
            decrypted_message += char
    return decrypted_message


# Asks for a number until valid
def ask_shift():
    shift = input("By how much would you like to shift the message? ")
    while not shift.isdigit():
        shift = input(f"\"{shift}\" is not a number. Type in a positive integer to shift the message: ")
    # We can use modulo of 26 as any shift+26x will bring the same encryption output
    return int(shift)%26


# Asks for either encryption or decryption until valid
mode = input("Type \"encrypt\" to encrypt or \"decrypt\" to decrypt a message: ").lower()
while mode == "" or not ("encrypt".startswith(mode) or "decrypt".startswith(mode)):
    mode = input(f"\"{mode}\" is not an option. Type in either \"encrypt\" or \"decrypt\": ")

# Checks for mode
if "encrypt".startswith(mode):
    message = input("Type in the message you want to encrypt: ")
    print(f"The encrypted message is:\n{encrypt(message, ask_shift())}")
else:
    message = input("Type in the message you want to decrypt: ")
    print(f"The decrypted message is:\n{decrypt(message, ask_shift())}")
    