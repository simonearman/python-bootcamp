from random import randint

# ASCII arts by Veronica Karlsson
rock = '''
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

print("Welcome to rock, paper, scissors")
move = input("Type \"rock\", \"paper\" or \"scissors\" to choose your move: ").lower()

# User move
# You can use abbreviations such as "s" or "sci" to choose scissors, etc.
if "rock".startswith(move):
    print(f"\nYour move: rock{rock}")
    move = "rock"
elif "paper".startswith(move):
    print(f"\nYour move: paper{paper}")
    move = "paper"
elif "scissors".startswith(move):
    print(f"\nYour move: scissors{scissors}")
    move = "scissors"
else:
    print(f"\n\"{move}\" is not an option\nTry one of the allowed moves")
    exit()

# Random AI move: 0 = rock, 1 = paper, 2 = scissors
ai_rand = randint(0, 2)
if ai_rand == 0:
    print(f"AI move: rock{rock}")
    ai_move = "rock"
elif ai_rand == 1:
    print(f"AI move: paper{paper}")
    ai_move = "paper"
else:
    print(f"AI move: scissors{scissors}")
    ai_move = "scissors"

# Results
# First we check for a draw
if move == ai_move:
    print(f"You both chose {move}, it's a draw!")
elif move == "rock":
    if ai_move == "scissors":
        print("Rock beats scissors, you win!")
    else:
        print("Paper beats rock, you lose!")
elif move == "paper":
    if ai_move == "rock":
        print("Paper beats rock, you win!")
    else:
        print("Scissors beat paper, you lose!")
elif move == "scissors":
    if ai_move == "paper":
        print("Scissors beat paper, you win!")
    else:
        print("Rock beats scissors, you lose!")
