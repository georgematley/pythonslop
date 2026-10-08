import tkinter as tk
from slots import *

money = 5
goal = 20
round = 1

def main_window(money,goal,round):
    window = tk.Tk()
    button2 = tk.Button(master=window, text="Roll slots!", command=lambda: slots(money, goal, round))  # rollslot will roll the slots and display on a label the result and money and other bs.
    button2.pack()
    while True:
        window.update()
        window.update_idletasks()
    return money, goal, round


money, goal, round = main_window(money,goal,round)