# This has the slot mechanics

from main import *
from goals import *

import random

def get_symbols(slot):
    symbols = ["cherry", "lemon", "1 bar", "2 bars", "3 bars", "7"]
    for i in range(3):
        probability = random.randint(1, 100) # cherries = 40%, lemons = 30%, 1 bar = 10%, 2 bar = 10%, 3 bar = 7%, 7 = 3%
        if probability <= 40:
            slot.append(symbols[0])
        elif 41 <= probability <= 70:
            slot.append(symbols[1])
        elif 71 <= probability <= 80:
            slot.append(symbols[2])
        elif 81 <= probability <= 90:
            slot.append(symbols[3])
        elif 91 <= probability <= 97:
            slot.append(symbols[4])
        elif probability > 97:
            slot.append(symbols[5])
        else:
            print("Something isn't working!")
    return slot

def slot_winnings(slot, money, multiplier):
    if slot == ["cherry", "cherry", "cherry"]:
        print(f"3 cherries! You win {(5*multiplier)} coins!")
        money += (5*multiplier)
    elif slot[0] == "cherry" and slot[1] == "cherry":
        print(f"2 cherries! You win {(3*multiplier)} coins!")
        money += (3*multiplier)
    elif slot == ["lemon", "lemon", "lemon"]:
        print(f"3 lemons! You win {(10*multiplier)} coins!")
        money += (10*multiplier)
    elif slot == ["1 bar", "1 bar", "1 bar"]:
        print(f"3 bars! You win {(20*multiplier)} coins!")
        money += (20*multiplier)
    elif slot == ["2 bars", "2 bars", "2 bars"]:
        print(f"6 bars! You win {(30*multiplier)} coins!")
        money += (30*multiplier)
    elif slot == ["3 bars", "3 bars", "3 bars"]:
        print(f"9 bars! You win {(40*multiplier)} coins!")
        money += (40*multiplier)
    elif slot == ["7","7","7"]:
        print(f"7 7 7 ! You win {(77*multiplier)} coins!")
        money += (77*multiplier)

    return slot, money

def slots(money, goal, round):
    print("Click enter to roll the slots! (Costs 1 coin)")
    print("Alternatively, type a number to raise stakes!") # change to show stakes as well as (current stake 1 coin etc.)
    print("Or type 'quit' to go back to the main menu!")
    stop = False
    multiplier = 1
    while stop == False:
        #if money <= 0: # to do, fix this????
         #   stop = True
        if money >= goal:
            round += 1
            goal = goals(round)
            print("You passed the goal! Next round goal:",goal)
        else:
            rollslot = input()
            if rollslot == "quit":
                stop = True

            elif rollslot == "" and money > 0:
                money -= multiplier
                slot = []
                get_symbols(slot)
                print(" | ".join(slot))
                slot, money = slot_winnings(slot, money, multiplier)
                print("Money: ", money)
                stop = False
            elif rollslot != "":
                try:
                    rollslot = int(rollslot)
                    if rollslot > money:
                        print("You don't have that much money!")
                    else:
                        multiplier = int(rollslot)
                        print("Multiplier raised to: ", multiplier)
                except:
                    print("Something went wrong.")

            else:
                stop = True
        return money, goal, round
