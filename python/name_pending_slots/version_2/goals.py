def goals(round):
    if round == 1:
        goal = 100
    elif round == 2:
        goal = 400
    elif round == 3:
        goal = 900
    elif round == 4:
        goal = 1600
    elif round == 5:
        goal = 6000
    elif round == 6:
        goal = 20000
    else:
        goal = (round^2) * 10000
    return goal