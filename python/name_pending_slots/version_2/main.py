# This is the main program, this will handle all user interactions

from slots import *
from scratchcards import *
from goals import *

def main():
    quitting = False
    money = 99
    round = 1
    goal = 100
    while quitting == False:
        if money <= 0:
            print("You went bankrupt.")
            quitting = True
        elif money >= goal:
            round += 1
            goal = goals(round)
            print("You passed the goal! Next round goal:",goal)
        else:
            print("Your goal:",goal)
            print("Money: ", money)
            print("Type 1 for slots and 2 for scratch cards, or 9 to quit!")
            gambletype = input()
            if gambletype == "1":
                money = slots(money, goal, round)
            elif gambletype == "2":
                money = scratch(money, goal, round)
            elif gambletype == "9":
                quitting = True
            else:
                print("Type 1 or 2.")

if __name__ == "__main__":
    main()