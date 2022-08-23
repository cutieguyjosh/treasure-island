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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

start = input("You see two roads leading to a path. Do you go left or right?\n").lower()

if start == "left":
  middle = input("You come to a lake and see an insland in the middle of it. Type 'wait' to wait for a boat. Type 'swim' to swim to it.\n").lower()
  if middle == "wait":
    end = input("You arrived at the island unharmed and see 3 doors. One red, One yellow, and one blue. Which color door do you choose?\n").lower()
    if end == "red":
      print("You enter the door full of flames and got burned. Game Over!")
    elif end == "blue":
      print("You enter the door full of wolves and got eaten. Game Over!")
    elif end == "yellow":
      print("You enter the door and see a giant treasure chest. Congratulations, you win!")
    else:
      print("Game over!")
    
  elif middle == "swim":
    print("You were attacked by a giant Shark. Game over!")

elif start == "right":
  print("You fall into a deep deep hole. Game over.")

else:
  print("Wrong choice. Start over!")
  

