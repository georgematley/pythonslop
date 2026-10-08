import tkinter as tk
from slots import *

def main_window():
    money = 10
    goal = 20
    round = 1
    window = tk.Tk()
    button = tk.Button(master=window, text = "Visit slots!", command=lambda: slots(money, goal, round))
    button.pack()
    button2 = tk.Button(master=window, text = "Roll slots!", command=lambda: rollslot()) # rollslot will roll the slots and display on a label the result and money and other bs.

    window.mainloop()

main_window()