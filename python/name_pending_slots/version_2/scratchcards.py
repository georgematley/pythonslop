# This handles all the scratch cards.

from main import *
from goals import *

import random

def scratch(money, goal, round):
    back = False
    while back == False:
        if money <= 0:
            back = True
        elif money >= goal:
            round += 1
            goal = goals(round)
            print("You passed the goal! Next round goal:", goal)
        else:
            back = False
        print("""Choose a scratch card!
        1. Win big! (Match 3 - 5 coins)
        2. Bang Bang! (Find symbol - 5 coins)
        3. Go Fish! (Find symbol - 10 coins)
        4. Bingo! (Match 5 - 10 coins)
        5. The big one! (Find symbol - 20 coins)
        9. Back""")
        print("Goal:",goal)
        print("Money:",money)
        card = input()
        if card == "1":
            money -= 5
            money = winbig(money)
        elif card == "2":
            money -= 5
            money = bangbang(money)
        elif card == "3":
            money -= 5
            money = gofish(money)
        elif card == "9":
            back = True
    return money, goal, round

def winbig(money):
    symbols = ["MoneyBag","Diamond","Boat","Gold","BigWin"]
    scratchcard = []
    print("Press enter to scratch!")
    while len(scratchcard) < 3:
        scratcher = input()
        if scratcher == "":
            scratchcard.append(choose_symbol(symbols))
            print(scratchcard)
        else:
            print("Press enter!")
    money = big_winnings(scratchcard, money)
    return money

def big_winnings(scratchcard, money):
    if scratchcard == ["MoneyBag","MoneyBag","MoneyBag"]:
        print("MoneyBag Win! 50 coins!")
        money += 50
    elif scratchcard == ["Diamond","Diamond","Diamond"]:
        print("Diamond Win! 100 coins!")
        money += 100
    elif scratchcard == ["Boat","Boat","Boat"]:
        print("Boat Win! 150 coins!")
        money += 150
    elif scratchcard == ["Gold","Gold","Gold"]:
        print("Gold Win! 200 coins!")
        money += 200
    elif scratchcard == ["BigWin","BigWin","BigWin"]:
        print("BIG WIN! 500 COINS!")
        money += 500
    return money

def bangbang(money):
    symbols = ["Gun","Tavern","Horsey","Tumbleweed","BANGBANG"]
    print("Press enter to scratch!")
    scratch = False
    while scratch == False:
        scratcher = input()
        if scratcher == "":
            symbol = choose_symbol(symbols)
            if symbol == "BANGBANG":
                print("Your symbol: ",symbol)
                print("BANG BANG! YOU WIN 20 COINS!")
                money += 20
            else:
                print("Your symbol: ", symbol)
                print("Too bad...")
            scratch = True
        else:
            print("Press enter to scratch!")
            scratch = False
    return money

def gofish(money):
    print("""Go fishing!
    1. Small Fry - 5 coins
    2. Sea Bass - 10 coins
    3. Cod - 15 coins
    4. Golden Fish - 20 coins
    5. The Big One - 50 coins""")
    symbols = ["Seaweed","Kelp","Sand","Shell","Small Fry","Small Fry","Small Fry","Sea Bass","Sea Bass","Cod","Golden Fish","The Big One"]
    scratch = False
    while scratch == False:
        print("Press enter to scratch!")
        scratcher = input()
        if scratcher == "":
            symbol = choose_symbol(symbols)
            print("Your symbol: ", symbol)
            money = fish_wins(symbol, money)
            scratch = True
        else:
            scratch = False
    return money

def fish_wins(symbol, money):
    if symbol == "Small Fry":
        print("Small Fry win! 5 coins!")
        money += 5
    elif symbol == "Sea Bass":
        print("Sea Bass win! 10 coins!")
        money += 10
    elif symbol == "Cod":
        print("Cod win! 15 coins!")
        money += 15
    elif symbol == "Golden Fish":
        print("Golden Fish win! 20 coins!")
        money += 20
    elif symbol == "The Big One":
        print("You caught The Big One! 50 coins!!!")
        money += 50
    else:
        print("Too bad...")
    return money

def choose_symbol(symbols):
    chance = random.randint(0,(len(symbols)-1))
    symbol = symbols[chance]
    return symbol
