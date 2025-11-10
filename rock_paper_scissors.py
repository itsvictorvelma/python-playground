import random

print("Welcome to Rock, Paper, Scissors.")
print("\nGood Luck!")

your_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

options=[''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''',
''' 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
]


if your_choice not in [0, 1, 2]:
    print("invalid input")

else:
    computer_choice = random.randint(0,2)

print(f"your choice: \n{options[your_choice]}")
print(f"\nComputer's choice: \n{options[computer_choice]}")


if your_choice == computer_choice:
    print("You Tied!")

elif (your_choice == 0 and computer_choice == 2) or \
     (your_choice == 1 and computer_choice == 0) or \
     (your_choice == 2 and computer_choice == 1):
    print("You win!")

else:
    print("You Lose!")