from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FOREGROUND_COLOR = "#FFFFFF"

# ---------------------------- MECHANICS ------------------------------- #
try:
    data = pandas.read_csv("Flash Card/data/french_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("Flash Card/data/Words To Learn.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_tile, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_tile, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("Words To Learn.csv")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="Flash Card/images/card_back.png")
card_img = PhotoImage(file="Flash Card/images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_img)
card_tile = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

tick_img = PhotoImage(file="Flash Card/images/right.png")
known_button = Button(image=tick_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="Flash Card/images/wrong.png")
unknown_button = Button(
    image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
