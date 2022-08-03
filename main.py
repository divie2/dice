from tkinter import *
import random

rat = Tk()
rat.title("divines dice game")
rat.geometry("500x500")




# get and return dice number

def get_number(x):
    if x == "\u2680":
        return (1)
    elif x == "\u2681":
        return (2)
    elif x == "\u2682":
        return (3)
    elif x == "\u2683":
        return (4)
    elif x == "\u2684":
        return (5)
    elif x == "\u2685":
        return (6)


# roll

def roll_dice():
    #  roll Random dice
    dice1 = random.choice(my_dice)
    dice2 = random.choice(my_dice)

    # get dice number
    d1 = get_number(dice1)

    d2 = get_number(dice2)

    # update sec
    num_dice_label1.config(text=d1)
    num_dice_label2.config(text=d2)

    #     update Labels
    dice_label1.config(text=dice1)
    dice_label2.config(text=dice2)


# create a dice list
my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

# create a Frame
my_frame = Frame(rat)
my_frame.pack(pady=20)

# create dice labels
dice_label1 = Label(my_frame, text='', font=('helvetica', 100))
dice_label1.grid(row=0, column=0, padx=5)
num_dice_label1 = Label(my_frame, text="",bg="green")
num_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=('helvetica', 100),)
dice_label2.grid(row=0, column=1, padx=5)
num_dice_label2 = Label(my_frame, text="",bg="green")
num_dice_label2.grid(row=1, column=1)

# create Roll button
my_button = Button(rat, text="Roll Dice", command=roll_dice,bg="purple")
my_button.pack(pady=20)

# roll dice function
roll_dice()
rat.mainloop()
