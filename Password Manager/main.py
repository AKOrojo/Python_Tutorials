import email
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Times New Roman"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def searchbox():
    website = website_entry.get()
    try:
        with open("Password Manager/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Not Data Entry", message="No Data Entry")
    else:
        if website in data:
            email = data[website]
            username = email["username"]
            password = email["password"]
            messagebox.showinfo(
                title=email, message=f"Username: {username}\n Password: {password}")
        else:
            messagebox.showinfo(
                title="Not Vaild Entry", message="Search for valid entry")


def save():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Fill Boxes", message="All boxes not filled")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"Details\n Email: {username} \n Password: {password} \n Is It Okay?")
        if is_ok:
            try:
                with open("Password Manager/data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("Password Manager/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("Password Manager/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0)
website.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

search = Button(text="Search", highlightthickness=0,
                width=15, command=searchbox)
search.grid(column=2, row=1)

username = Label(text="Email/Username", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0)
username.grid(column=0, row=2)

username_entry = Entry(width=48)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "b.korojo@gmail.com")

password = Label(text="Password", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0)
password.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password",
                           highlightthickness=0, command=password_generator)
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", highlightthickness=0, width=60, command=save)
add_password.grid(column=0, row=4, columnspan=3)

window.mainloop()
