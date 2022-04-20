print("Welcome to Treasure Island!\nYour mission is to find the treasure")


def answer_not_understood(answer):
    print(f"\nI'm afraid i don't understand \"{answer}\".\n"
          f"Next time use a proper answer.")


starting_crossroad = input("\nYou wake up in the middle of the forest. In front of you, there is a road.\n"
                           "Which direction will you take? (West or East) ").lower()
if starting_crossroad == "west":
    take_statue = input("\nYou head west. On the ground, you find an abandoned, marble dragon statue.\n"
                        "Will you take it? (Yes or No) ").lower()
    if take_statue == "yes":
        print("\nWhen you touch the statue, it turns into a giant, hungry dragon.\n"
              "The dragon eats you. Game Over.")
    elif take_statue == "no":
        enter_forest = input("\nYou decided to ignore the statue. You keep on following the road west.\n"
                             "The road leads into a forest. Do you continue into the forest? (Yes or No) ").lower()
        if enter_forest == "yes":
            accept_riddle = input("\nYou head into the forest. Inside, You stumble upon an ent.\n"
                                  "He promises you treasure if you can answer his riddle.\n"
                                  "Will you accept the challenge? (Yes or No) ").lower()
            if accept_riddle == "yes":
                riddle_answer = input("\nHere is the riddle:\n"
                                      "\"What grows when it eats, but dies when it drinks?\" ").lower()
                if riddle_answer == "fire":
                    print("\n\"Fire! Yes!\" As promised, the ent rewards you with enough gold to buy a whole country.\n"
                          "You win!")
                else:
                    print(f"\nSadly, \"{riddle_answer}\" is not the answer.\n"
                          f"Better luck next time. Game over.")
            elif accept_riddle == "no":
                print("\n\"I don't want your treasure!\" - you exclaimed.\n"
                      "You chop the ent down, building yourself a home, where you spend the rest of your days.\n"
                      "Game over?")
            else:
                answer_not_understood(accept_riddle)
        elif enter_forest == "no":
            print("\nYou decided to linger for a little bit in front of the forest.\n"
                  "You waited for so long, that a group of bandits attack you for your trinkets.\n"
                  "Game Over.")
        else:
            answer_not_understood(enter_forest)
    else:
        answer_not_understood(take_statue)
elif starting_crossroad == "east":
    print("\nYou head east. You keep on going for days, finding nothing.\n"
          "You die from starvation. Game over.")
else:
    answer_not_understood(starting_crossroad)
