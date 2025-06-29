# Rock Paper Scissors Project

'''
You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.
'''

import random
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

game_illustrations = [rock, paper, scissors]
bots_weapon = random.randint(0,2)
your_weapon = int(input("Choose your weapon! Enter 0 for Rock, 1 for Paper and 2 for Scissors: "))
print("Your choice:")
print(game_illustrations[your_weapon])
print("Computer's choice:")
print(game_illustrations[bots_weapon])
if your_weapon == bots_weapon:
    print("It's a draw!")
elif your_weapon == 0 and bots_weapon == 1:
    print("You lose.")
elif your_weapon == 1 and bots_weapon == 0:
    print("You won!")
elif your_weapon == 0 and bots_weapon == 2:
    print("You won!")
elif your_weapon == 2 and bots_weapon == 0:
    print("You lose!")
elif your_weapon == 1 and bots_weapon == 2:
    print("You lose!")
elif your_weapon == 2 and bots_weapon == 1:
    print("You won!")
elif your_weapon == 1 and bots_weapon == 2:
    print("You lose!")
else:
    print("Invalid input! You lose.")