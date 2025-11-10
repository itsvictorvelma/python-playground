import random

print("Welcome to Rock, Paper, Scissors.")
print("\nGood Luck!")

your_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0,2)

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
    print("Input invalid")

else:
    if your_choice == 0:
        print(f"Your choice:\n\n{options[0]}")
        
        if computer_choice == 1:
            print(f'\nComputers choice\n\n{options[1]}')
            print("You lose!")

        elif computer_choice == 2:
            print(f'\nComputers choice:\n\n{options[2]}')
            print("You Win!")
            
        elif computer_choice == 0:
            print(f'\nComputers choice:\n\n{options[0]}')
            print("You Tied!")

    elif your_choice == 1:
        print(f"Your choice:\n\n{options[1]}")
        
        if computer_choice == 1:
            print(f'\nComputers choice\n\n{options[1]}')
            print("You Tied!")

        elif computer_choice == 2:
            print(f'\nComputers choice:\n\n{options[2]}')
            print("You Lose!")
        else:
            print(f'\nComputers choice:\n\n{options[0]}')
            print("You Win!")

    elif your_choice == 2:
        print(f"Your choice:\n\n{options[2]}")
        
        if computer_choice == 1:
            print(f'\nComputers choice\n\n{options[1]}')
            print("You Win!")

        elif computer_choice == 2:
            print(f'\nComputers choice:\n\n{options[2]}')
            print("You Tied!")
        else:
            print(f'\nComputers choice:\n\n{options[0]}')
            print("You Lose!")
