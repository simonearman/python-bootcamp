from random import random
import sys
import os


def clear_console():
    """Clears the console"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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


def read_argv(option):
    """Returns the switch's value from command line arguments"""
    if option in sys.argv:
        option_index = sys.argv.index(option)
        if option_index < len(sys.argv) - 1 and not sys.argv[option_index + 1].startswith("-"):
            sys.argv.remove(option)
            return sys.argv.pop(option_index)
        sys.argv.remove(option)
    return None


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


def read_decks_argv():
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


def pick_card(hand, pack):
    """Takes a random card from the pack of cards and puts it in a hand"""
    picked_card = select_random_card_rank(pack)
    hand.append(picked_card)
    pack[picked_card] -= 1
    if count_cards(pack) == 0:
        shuffle_pack(pack, decks_in_pack)
        input("The pack of cards has been reshuffled. Press Enter to continue")


def bet(chips, player_hand):
    """Asks the user for the amount to bet, returns the bet amount"""
    bet_amount = input("How much would you like to bet? $")
    while not is_int(bet_amount) or int(bet_amount) > chips or int(bet_amount) <= 0:
        if not is_int(bet_amount):
            display_game(chips, [0, 0, 0, 0], 0, player_hand, [], f"${bet_amount} is not a viable bet", True)
            bet_amount = input("How much would you like to bet? $")
        elif int(bet_amount) <= 0:
            display_game(chips, [0, 0, 0, 0], 0, player_hand, [], f"You can't bet ${bet_amount}", True)
            bet_amount = input("How much would you like to bet? $")
        else:
            display_game(chips, [0, 0, 0, 0], 0, player_hand, [], "You can't bet more than you currently own", True)
            bet_amount = input("How much would you like to bet? $")
    return int(bet_amount)


def calculate_hand_value(hand):
    """Returns the sum of card's values of a hand"""
    value = 0
    temp_hand = hand.copy()
    # Puts all the aces at the very end of the hand for later calculations
    for card in range(temp_hand.count("A")):
        temp_hand.append((temp_hand.pop(temp_hand.index("A"))))
    for card in temp_hand:
        if card == "K" or card == "Q" or card == "J" or card == "10":
            value += 10
        elif is_int(card):
            value += int(card)
        else:
            if value <= 10:
                value += 11
            else:
                value += 1
    return value


def insurance(chips, current_bet, player_hand, dealer_hand):
    """Asks the user for the amount to bet, returns the bet amount"""
    insure_message = f"You can insure up to 50% of your current chips ({round(chips / 2)})."
    display_game(chips, current_bet, 0, player_hand, dealer_hand, insure_message, True)
    insurance_amount = input("How much would you like to insure? $")
    while not is_int(insurance_amount) or int(insurance_amount) > round(chips/2):
        if not is_int(insurance_amount):
            display_game(chips, current_bet, 0, player_hand, dealer_hand,
                         f"${insurance_amount} is not a viable insurance value.", True)
            insurance_amount = input("How much would you like to insure? $")
        else:
            display_game(chips, current_bet, 0, player_hand, dealer_hand,
                         f"You can only insure up to 50% of your current chips (${round(chips/2)})", True)
            insurance_amount = input("How much would you like to insure? $")
    return int(insurance_amount)


def display_bet(bets):
    bet_to_display = "$0"
    if bets[0] > 0:
        lowest_bet = max(bets)
        for a_bet in bets:
            if 0 < a_bet < lowest_bet:
                lowest_bet = a_bet
        bet_to_display = f"${lowest_bet}"
        if bets.count(lowest_bet) > 1:
            bet_to_display += f" x{bets.count(lowest_bet)}"
        if bets.count(lowest_bet * 2):
            bet_to_display += f" + ${lowest_bet * 2}"
            if bets.count(lowest_bet * 2) > 1:
                bet_to_display += f" x{bets.count(lowest_bet * 2)}"
    return bet_to_display


def display_cards(hand, hide_second_card):
    """Returns a string showing the cards in a hand"""
    if not hand:
        return ""
    elif hide_second_card:
        return f"[{hand[0]}] [?]"
    else:
        return f"[{'] ['.join(hand)}] = {calculate_hand_value(hand)}"


def display_game(chips, current_bet, insurance_amount, player_hand, dealer_hand, message, hide_second_card):
    """Displays the most important game info"""
    clear_console()
    insurance_to_print = "\n"
    if insurance_amount > 0:
        insurance_to_print = f"INSURANCE: ${insurance_amount}\n"
    print(f"{' ' * 38}BLACKJACK")
    print(f"{'=' * 85}")
    print(f"{' ' * 8}DEALER'S CARDS{' ' * 30}BALANCE: ${chips}")
    dealer_hand_graphics = display_cards(dealer_hand, hide_second_card)
    print(f"{' ' * 8}{dealer_hand_graphics}{' ' * (40 - len(dealer_hand_graphics))}"
          f"CURRENT BET: {display_bet(current_bet)}")
    print(f"{' ' * 50}{insurance_to_print}")
    print(f"{' ' * 8}PLAYER'S CARDS")
    player_hand_graphic = f"{display_cards(player_hand[0], False)}"
    if player_hand[1]:
        player_hand_graphic = f"1: {player_hand_graphic}{' ' * (35 - len(player_hand_graphic))}" \
                              f"2: {display_cards(player_hand[1], False)}"
    print(f"{' ' * 8}{player_hand_graphic}")
    player_hand_graphic2 = ""
    if player_hand[2]:
        player_hand_graphic2 = f"3: {display_cards(player_hand[2], False)}"
        if player_hand[3]:
            player_hand_graphic2 += f"{' ' * (38 - len(player_hand_graphic2))}4: {display_cards(player_hand[3], False)}"
    print(f"{' ' * 8}{player_hand_graphic2}\n")
    print(message)


def read_game_end_move(can_keep_bet, lost):
    if can_keep_bet:
        return input(f"Enter \"B\" to place a new bet, or press ENTER to keep the last bet: ").lower()
    elif lost:
        return input("You don't have any money left. Press Enter to quit the game")
    else:
        return input("Press ENTER to place a new bet")


def read_move(can_double_down, can_split, can_insurance, hand_number, player_hand):
    hand_number_message = ""
    if player_hand[1]:
        hand_number_message = f" for hand #{hand_number + 1}"
    move = input(f"Your move{hand_number_message}: ").lower()
    if move == "h":
        return "H"
    elif move == "s":
        return "S"
    elif can_double_down and move == "d":
        return "D"
    elif can_split and move == "sp":
        return "SP"
    elif can_insurance and move == "i":
        return "I"
    else:
        return None


def play_blackjack(chips, decks):
    keep_playing = True
    shuffle_pack(card_pack, decks)
    keep_bet = False
    first_bet = 0
    welcome_message = "Welcome to Blackjack! To start the game place your first bet"
    while keep_playing:
        insurance_amount = 0
        player_hand = []
        for hand in range(4):
            player_hand.append([])
        dealer_hand = []
        if not keep_bet:
            current_bet = [0, 0, 0, 0]
            display_game(chips, current_bet, 0, player_hand, dealer_hand, welcome_message, True)
            first_bet = bet(chips, player_hand)
            current_bet = [first_bet, 0, 0, 0]
        else:
            current_bet = [first_bet, 0, 0, 0]
        chips -= first_bet
        pick_card(player_hand[0], card_pack)
        pick_card(dealer_hand, card_pack)
        pick_card(player_hand[0], card_pack)
        pick_card(dealer_hand, card_pack)
        can_double_down = False
        can_split = False
        can_insurance = False
        for hand_number, hand in enumerate(player_hand):
            if hand:
                move = None
                if len(hand) == 1:
                    pick_card(hand, card_pack)
                if calculate_hand_value(hand) == 21 or calculate_hand_value(dealer_hand) == 21:
                    move = "S"
                while move is None:
                    if len(hand) == 1:
                        pick_card(hand, card_pack)
                        if calculate_hand_value(hand) == 21:
                            break
                    moves_available = "Enter \"H\" to hit, \"S\" to stand"
                    if len(hand) == 2:
                        player_hand_value = calculate_hand_value(hand)
                        if (player_hand_value == 9 or player_hand_value == 10 or player_hand_value == 11) or \
                                ((player_hand_value == 16 or player_hand_value == 17 or player_hand_value == 18) and
                                 "A" in player_hand) \
                                and chips >= first_bet:
                            moves_available += ", \"D\" to double down"
                            can_double_down = True
                        if calculate_hand_value([hand[0], 0]) == calculate_hand_value([hand[1], 0]) \
                                and [] in player_hand and chips >= first_bet:
                            moves_available += ", \"SP\" to split"
                            can_split = True
                        if dealer_hand[0] == "A" and not can_insurance and hand_number < 1:
                            moves_available += ", \"I\" to insurance"
                            can_insurance = True
                    display_game(chips, current_bet, insurance_amount, player_hand, dealer_hand, moves_available,
                                 True)
                    move = read_move(can_double_down, can_split, can_insurance, hand_number, player_hand)
                    if move == "H":
                        pick_card(hand, card_pack)
                        if calculate_hand_value(hand) < 21:
                            move = None
                    elif move == "D":
                        pick_card(hand, card_pack)
                        current_bet[hand_number] *= 2
                        chips -= first_bet
                    elif move == "SP":
                        player_hand[player_hand.index([])] = [hand.pop(1)]
                        current_bet[current_bet.index(0)] = first_bet
                        chips -= first_bet
                        move = None
                    elif move == "I":
                        insurance_amount = insurance(chips, current_bet, player_hand, dealer_hand)
                        chips -= insurance_amount
                        move = None
        for hand in player_hand:
            if hand:
                while calculate_hand_value(dealer_hand) < 17 and \
                        calculate_hand_value(dealer_hand) <= calculate_hand_value(hand) and \
                        not (calculate_hand_value(hand) == 21 and len(hand) == 2) and \
                        not calculate_hand_value(hand) > 21:
                    pick_card(dealer_hand, card_pack)
        winnings = 0
        for hand_number, hand in enumerate(player_hand):
            if calculate_hand_value(hand) == 21 and len(hand) == 2 and not calculate_hand_value(dealer_hand) == 21:
                winnings += int(current_bet[hand_number] * 2.5)
            elif calculate_hand_value(dealer_hand) == 21 and len(dealer_hand) == 2:
                winnings += 0
            elif calculate_hand_value(hand) > 21:
                winnings += 0
            elif calculate_hand_value(dealer_hand) > 21:
                winnings += 2 * current_bet[hand_number]
            elif calculate_hand_value(hand) > calculate_hand_value(dealer_hand):
                winnings += 2 * current_bet[hand_number]
            elif calculate_hand_value(hand) == calculate_hand_value(dealer_hand):
                winnings += current_bet[hand_number]
            else:
                winnings += 0
        if calculate_hand_value(dealer_hand) == 21 and len(dealer_hand) == 2:
            winnings_message = f"The dealer has a Blackjack. You lose ${-(winnings - sum(current_bet))}"
        elif winnings - sum(current_bet) >= 0:
            winnings_message = f"You win ${winnings - sum(current_bet)} this round"
        else:
            winnings_message = f"You lose ${-(winnings - sum(current_bet))} this round"
        if insurance_amount > 0:
            if calculate_hand_value(dealer_hand) == 21 and len(dealer_hand) == 2:
                winnings_message += f". You win ${insurance_amount * 2} from the insurance bet"
                winnings += insurance_amount * 2
            else:
                winnings_message += f". You lost the insurance bet"
        chips += winnings
        display_game(chips, current_bet, insurance_amount, player_hand, dealer_hand, winnings_message, False)
        if chips <= 0:
            read_game_end_move(False, True)
            keep_playing = False
        elif first_bet < chips:
            if read_game_end_move(True, False) == "b":
                keep_bet = False
                welcome_message = "Place your bet to start another round"
            else:
                keep_bet = True
        else:
            welcome_message = "Place your bet to start another round"
            read_game_end_move(False, False)
            keep_bet = False


card_pack = {}
starting_chips = read_chips_argv()
decks_in_pack = read_decks_argv()
play_blackjack(starting_chips, decks_in_pack)
