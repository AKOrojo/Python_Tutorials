
from tkinter import *

w = Tk()
w.title("My GUI")
w.minsize(width=500, height=300)

# label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"


def button_clicked():
    print("I GOT CLICKED")


def change_text():
    my_label["text"] = "Text"


def name():
    my_label["text"] = input.get()


button = Button(text="Click Me", command=name)
button.pack()

input = Entry(width=10)
input.pack()


w.mainloop()
