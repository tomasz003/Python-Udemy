from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
YOUR_LANGUAGE="English"
LEARNING_LANGUAGE="German"
#------------------WORDS-------------------------#
try:
    vocab=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    vocab = pandas.read_csv("data/german_words.csv")
dict_vocab=vocab.to_dict(orient="records")
curr_card={}


def user_know():
    dict_vocab.remove(curr_card)
    data=pandas.DataFrame(dict_vocab)
    data.to_csv("data/words_to_learn.csv", index=False)
    word_draw()


def word_draw():
    global flip_timer, curr_card
    window.after_cancel(flip_timer)
    curr_card=choice(dict_vocab)
    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(language, text=LEARNING_LANGUAGE, fill="black")
    canvas.itemconfig(word, text=curr_card[LEARNING_LANGUAGE], fill="black")
    flip_timer=window.after(3000, flip)
    return 0

def flip():
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(language, text=YOUR_LANGUAGE, fill="white")
    canvas.itemconfig(word, text=curr_card[YOUR_LANGUAGE], fill="white")

#------------------UI SETUP----------------------#
window=Tk()
window.title("Fiszki")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas=Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img=PhotoImage(file="images/card_front.png")
back_card_img=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 263,image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

#texts
language=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word=canvas.create_text(400, 263,text="", font=("Ariel", 60, "bold"))

#buttons
wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image, highlightthickness=0, command=word_draw)
wrong_button.grid(row=1, column=0)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image, highlightthickness=0, command=user_know)
right_button.grid(row=1, column=1)

flip_timer=window.after(3000, flip)
word_draw()
window.mainloop()