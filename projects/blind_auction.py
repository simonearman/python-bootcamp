import os


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def is_number(input):
    if input is None:
        return False
    try:
        float(input)
        return True
    except ValueError:
        return False


# Asks the user for the bid amount
def ask_bid():
    bid = input("How much would you like to bid? $")
    # Checking if the user's bid is a number, then if it is negative
    while not is_number(bid) or float(bid) < 0:
        if not is_number(bid):
            bid = input(f"\"{bid}\" is not a correct bid. Enter a proper value to bid: $")
        else:
            bid = input("You can't bid a negative amount. How much would you like to bid? $")
    return round(float(bid), 2)


# Adds a bidder to a dictionary
def add_bidder(dict):
    name = input("What is your name? ")
    # Checking if someone already used the same name, or if the name is empty
    while name in dict or name == "":
        if name == "":
            name = input("You need to enter your name: ")
        else:
            name = input(f"Someone else already has the name \"{name}\". Enter a different name: ")
    dict[name] = ask_bid()


def is_last_bidder():
    last_bidder = input("Are you the last bidder? (yes or no) ").lower()
    # Checking if the user's answer is acceptable, asking again if not
    while not ("yes".startswith(last_bidder) or "no".startswith(last_bidder)) or last_bidder == "":
        last_bidder = input(f"\"{last_bidder}\" is not a valid option. You can only answer \"yes\" or \"no\": ").lower()
    if "yes".startswith(last_bidder):
        return True
    else:
        return False


bidders = {}
finish_bidding = False

while not finish_bidding:
    clear_console()
    print("Welcome to the blind action!")
    add_bidder(bidders)
    finish_bidding = is_last_bidder()

# Collecting the highest bidder's data from the dictionary
highest_bidder = ""
highest_bid = 0
for name in bidders:
    if bidders[name] > highest_bid:
        highest_bid = bidders[name]
        highest_bidder = name
    # If some else has also bidded the same highest amount
    elif bidders[name] == highest_bid:
        highest_bidder += f" and {name}"

print(f"The auction's winner is {highest_bidder} with a bid of ${highest_bid:.2f}!")
