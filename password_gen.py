#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"\nHow many symbols would you like?: "))
nr_numbers = int(input(f"\nHow many numbers would you like?: "))

picked_letters = random.choices(letters, k=nr_letters)
picked_numbers = random.choices(numbers, k=nr_numbers) 
picked_symbols = random.choices(symbols, k=nr_symbols)
    
generated_pass = picked_letters + picked_numbers + picked_symbols
random.shuffle(generated_pass)
password = ''.join(generated_pass)

print(f'\nyour password is: {password}\n')