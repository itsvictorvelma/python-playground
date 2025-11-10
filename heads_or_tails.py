import random

choice = input("Make you're call. Heads or Tails?: ").lower()
coin = random.randrange(10)

if coin % 2 == 0:
    print("\nHeads")
    
    if choice == "heads":
        print("\nYou win!\n")
    
    else: 
        print("\nYou lose!\n")

elif coin % 2 != 0:
    print("\nTails")

    if choice == "tails":
        print("\nYou win!\n")

    else:
        print("\nYou lose!\n")