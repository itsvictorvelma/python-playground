
def calculator():

    while True:

        while True:
            operator = input("\nWhich operator would you like to use? (+, -, *, /, %): ").strip()        
            if operator in ["+", "-", "/", "*", "%"]:
                break
            else:
                print("\nThat is not a valid operator. Try again.")

        first_num = float(input("\nGreat!\n\nPlease give me the first number: "))
        second_num = float(input("\nPlease input the second number: "))

        if operator == "+":
            print("\nThat equals to:", first_num + second_num)

        elif operator == "-":
            print("\nThat equals to:", first_num - second_num)

        elif operator == "/":
            if second_num == 0:
                print("\nCannot divide by zero!")
            else:
                print("\nThat equals to:", first_num / second_num)

        elif operator == "*":
            print("\nThat equals to:", first_num * second_num)

        elif operator == "%":
            if second_num == 0:
                print("\nCannot divide by zero!")
            else:
                print("\n", first_num % second_num, "is the remainder")

        repeat = input("\ndo you have any more problems to solve? (y/n): ").strip().lower()

        if repeat != "y":
            print("\nSee you next time!")
            break


print("\nWelcome to my calculator")

calculator()
