from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password", message="Password copied to the clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: "
                                                  f"{password}\nIs it ok to save?")

    if is_ok:
        with open("./data.txt", mode="a") as data:
            data.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=("Arial", 10, "bold"))
website.grid(row=1, column=0)

username = Label(text="Email/Username:", font=("Arial", 10, "bold"))
username.grid(row=2, column=0)

password = Label(text="Password:", font=("Arial", 10, "bold"))
password.grid(row=3, column=0)

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "examplemail@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
