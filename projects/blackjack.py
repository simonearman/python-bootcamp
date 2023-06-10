from random import random
import sys


def read_argv(option):
    """Returns the switch's value from command line arguments"""
    if option in sys.argv:
        option_index = sys.argv.index(option)
        if option_index < len(sys.argv) - 1 and not sys.argv[option_index + 1].startswith("-"):
            sys.argv.remove(option)
            return sys.argv.pop(option_index)
        sys.argv.remove(option)
    return None


def is_int(value):
    """Returns True if the value is an integer, returns False otherwise"""
    if value is None:
        return False
    try:
        value = int(value)
        if value % 1 == 0:
            return True
        else:
            return False
    except ValueError:
        return False


def read_chips_argv():
    """Returns the amount specified in the -c or -chips switch, returns 100 if not specified"""
    chips_amount = read_argv("-c")
    if chips_amount is None:
        chips_amount = read_argv("-chips")
    if chips_amount is None:
        return 100
    if not is_int(chips_amount) or int(chips_amount) < 1:
        return 100
    else:
        return int(chips_amount)


def read_deck_argv():
    """Returns the amount specified in the -d or -decks switch, returns 6 if not specified"""
    decks_amount = read_argv("-d")
    if decks_amount is None:
        decks_amount = read_argv("-decks")
    if decks_amount is None:
        return 6
    if not is_int(decks_amount) or int(decks_amount) < 1:
        return 6
    else:
        return int(decks_amount)


def count_cards(pack):
    """Returns the amount of cards left in the pack"""
    count = 0
    for rank in pack:
        count += pack[rank]
    return count


def select_random_card_rank(pack):
    """Returns a card rank from amongst all the available cards in the pack"""
    rank_probability = []
    previous_rank_probability = 0
    for rank in pack:
        if pack[rank] == 0:
            rank_probability.append(-1)
        else:
            rank_probability.append(pack[rank]/count_cards(pack) + previous_rank_probability)
            previous_rank_probability = (pack[rank]/count_cards(pack) + previous_rank_probability)
    rank_probability[len(rank_probability)-1] = 1
    random_value = random()
    for index, probability in enumerate(rank_probability):
        if random_value < probability:
            return list(pack.keys())[index]


def remove_random_cards(cards_to_remove, pack):
    """Removes an amount of random cards from the pack of cards"""
    while cards_to_remove > 0:
        pack[select_random_card_rank(pack)] -= 1
        cards_to_remove -= 1


def shuffle_pack(pack, decks):
    """Shuffles the card pack with several decks of cards, removing from 15% to 18% of all cards"""
    card_ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    for rank in card_ranks:
        pack[rank] = 4 * decks
    cards_to_remove = round((random() * 0.03 + 0.15) * 52 * decks)
    remove_random_cards(cards_to_remove, pack)


def pick_card(pack):
    """Returns a random card from the pack of cards, removing it from the pack"""
    print("test")


def bet(chips):
    """Asks the user for the amount to bet, returns the bet amount"""
    bet_amount = input("How much would you like to bet? $")
    while not is_int(bet_amount) or int(bet_amount) > chips or int(bet_amount) == 0:
        if not is_int(bet_amount):
            bet_amount = input(f"\"{bet_amount}\" is not a viable bet.\nHow much would you like to bet? $")
        elif int(bet_amount) == 0:
            bet_amount = input(f"You can't bet $0.\nHow much would you like to bet? $")
        else:
            bet_amount = input("You can't bet more than you currently own.\nHow much would you like to bet? $")
    return bet_amount


"""def hit():


def stand():


def double_down():


def split():


def surrender():"""


def play_blackjack(chips, decks):
    shuffle_pack(card_pack, decks)
    print(card_pack)
    current_bet = bet(chips)


card_pack = {}
starting_chips = read_chips_argv()
decks_in_pack = read_deck_argv()
play_blackjack(starting_chips, decks_in_pack)
