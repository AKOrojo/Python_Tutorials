
from tkinter import *

w = Tk()
w.title("Mile to KM Converter")
w.minsize(width=500, height=300)
w.config(padx=100, pady=100)

# label
x = 0

my_label = Label(text="Mile to KM Converter", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)

my_label2 = Label(text='0', font=("Arial", 24, "bold"))
my_label2.grid(column=2, row=2)

my_label3 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label3.grid(column=0, row=2)

my_label4 = Label(text='KM', font=("Arial", 24, "bold"))
my_label4.grid(column=3, row=2)

my_label3 = Label(text="Miles", font=("Arial", 24, "bold"))
my_label3.grid(column=3, row=1)


def m_to_km():
    number = float(input.get())
    result = round(number * 1.609)
    my_label2["text"] = result
    return result


button = Button(text="Calculate", command=m_to_km)
button.grid(column=2, row=3)

input = Entry(width=10)
input.grid(column=2, row=1)


w.mainloop()
