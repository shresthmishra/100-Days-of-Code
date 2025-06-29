# Treasure Island Project

'''
- Your goal today is to build a "Chose your own adventure game". 
- Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.
- Once you've completed the project, you can always extend the game and make it more interesting!
'''

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input("You're at a cross-road!\n"
      "Which way will you go to? (Left or Right): ").lower()
if crossroad == "right":
    print("You fell in a hole and died! Game Over.")
elif crossroad == "left":
    swim = input("You are now looking at a lake.\n"
          "Will you swim or wait for the boat? (Swim or Wait): ").lower()
    if swim == "swim":
        print("Crocodiles took you out for dinner! Game Over.")
    elif swim == "wait":
        door = input("You've almost reached the treasure! But looking at multiple doors.\n"
                     "Which door will you go to? (Red, Blue, Yellow): ").lower()
        if door == "red":
            print("Snakes attacked you! Game Over.")
        if door == "blue":
            print("You got locked inside a cave forever! Game Over.")
        elif door == "yellow":
            print("Congratulations, you won the treasure!")
        else:
            print("Non existent door!")
