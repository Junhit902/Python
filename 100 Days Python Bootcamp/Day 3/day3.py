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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Tresure Island!")
print("Your mission is to find the treasure!")

direction = input('You\'re at cross road. Where do you want to go? \n\tType "Right" or "Left"\n\t').upper()
if direction == "RIGHT":
    print("You fell into a hole. GAME OVER.")
elif direction == "LEFT":
    swim_boat = input("Do you want to swim or wait a boat? Type one option: ").upper()
    if swim_boat == "SWIM":
        print("You attacked by trout. GAME OVER.")
    elif swim_boat == "BOAT":
        door = input("Which following doors you will choose? Type 'red', 'blue' or 'yellow': ").upper()
        if door == "RED":
            print("Burned by fire. GAME OVER.")
        elif door == "BLUE":
            print("Eaten by beasts. GAME OVER.")
        elif door == "YELLOW":
            print("You win!")
        else:
            print("GAME OVER.")
    else:
        print("You attacked by trout. GAME OVER.")
else:
    print("You fell into a hole. GAME OVER.")
