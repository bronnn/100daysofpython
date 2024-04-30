# Rock, Paper, Scissors 

import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)

options = [rock, paper, scissors]

print ("You Chose " )
print(options[user_choice])
print ("Computer Chose " )
print(options[computer_choice])

if user_choice == 0 and  computer_choice == 2:
    print ("You win :)")
elif user_choice ==2 and computer_choice == 0:
    print("You lose :(")
elif user_choice == computer_choice:
    print ("Draw !")
elif computer_choice > user_choice:
    print ("You lose :(")
elif computer_choice < user_choice:
    print ("You win :)")
else:
    print ("You typed an invalid number, you lose :/ ")