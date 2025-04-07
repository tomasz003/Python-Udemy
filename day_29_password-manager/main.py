from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[choice(letters) for _ in range(randint(8, 10))]
    password_list+=[choice(symbols) for _ in range(randint(2, 4))]
    password_list+=[choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password="".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_new_one():
    web_given=web_entry.get()
    email_given=email_entry.get()
    password_given=pass_entry.get()

    if len(web_given)==0 or len(email_given)==0 or len(password_given)==0:
        messagebox.showinfo(title="Oopsie!", message="Make sure to fill all the fields!")
    else:
        is_okay=messagebox.askokcancel(title=web_given, message=f"Data entered: \nEmail: {email_given}\n"
                                                        f"Password: {password_given}\n\nIs it okay to save it?")

        if is_okay:
            with open("passwords.txt", "a") as f:
                f.write(f"{web_given} | {email_given} | {password_given}\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200, highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#labels:
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)

#buttons:
start_button=Button(text="Add", command=add_new_one)
start_button.grid(row=4, column=1, columnspan=2,  sticky="ew")
gen_pass_button=Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2,  sticky="ew")

#entries:
web_entry=Entry()
web_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
web_entry.focus()
email_entry=Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "mail@gmail.com")
pass_entry=Entry(width=30)
pass_entry.grid(row=3, column=1, sticky="w")

window.mainloop()