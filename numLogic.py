import random
range_num_a = None
range_num_b = None

def randomizer(range_num_a, range_num_b):
    return random.randint(min(range_num_a, range_num_b), max(range_num_a, range_num_b))

def randomLogic():
    user_guess = int(input("What's your guess? "))
    if user_guess == randomizer:
        print("You Win!!")
    else:
        print("You Lose!\nThe answer was: ", randomizer(range_num_a, range_num_b))

def get_range_and_confirm():
    global range_num_a
    global range_num_b
    range_num_a = int(input("What range would you like to use? "))
    range_num_b = int(input("And the second number? "))
    print("Would you like to use {} and {} as your range?".format(range_num_a, range_num_b))
    user_input = input("Y or N? ").upper()

    if user_input == "Y":
        randomLogic()
    elif user_input == "N":
        print("You chose No!")
    else:
        print("Invalid Input!")
    return user_input

def main():
    global range_num_a
    global range_num_b
    get_range_and_confirm()
    

if __name__ == "__main__":
    main()

