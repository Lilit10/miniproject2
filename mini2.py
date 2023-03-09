import random

def roll_dice():
    return random.randint(1, 6)

def craps():
   
    dice1 = roll_dice()
    dice2 = roll_dice()
    sum_of_dice = dice1 + dice2
    print(f"You rolled {dice1} and {dice2}. Total: {sum_of_dice}")

    if sum_of_dice in (7, 11):
        print("You win")
        return True
    elif sum_of_dice in (2, 3, 12):
        print("You lose")
        return False
    else:
        goal = sum_of_dice
        print(f"Your goal is now {goal}. Roll again")

    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        sum_of_dice = dice1 + dice2
        print(f"You rolled {dice1} and {dice2}. Total: {sum_of_dice}")
        if sum_of_dice == goal:
            print("You win")
            return True
        elif sum_of_dice == 7:
            print("You lose")
            return False

craps()
