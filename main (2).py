print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

print("You are at a crossroads. Do you want to go left or right?")
direction = input("Type 'left' or 'right': ").lower()
if direction == "left":
          choice = input("You have come to the lake. There is an island in the middle of the lake. Type 'wait' to wait              for a boat.Type'swim' to swim across.").lower()
          if choice == "wait":
                    choice2 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one                           yellow and one blue. Which colour do you choose?").lower()
                    if choice2 == "red":
                              print("It is a room full of fire. Game over.")
                    elif choice2 == "yellow":
                              print("You found the treasure! You win!")
                    elif choice2 == "blue":
                              print("You enter a room of beasts. Game over.")
                    else:
                              print("Game over.")
          else:
                    print("You are attacked by an angry trout. Game over.")
else:
          print("You fell into a hole. Game over.")
          