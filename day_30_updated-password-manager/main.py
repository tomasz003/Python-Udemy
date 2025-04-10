from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    web_given = web_entry.get()
    try:
        with open("passwords.json", "r") as f:
            data=json.load(f)   #dictionary!
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No passwords in our database yet!")
    else:
        if web_given in data:
            email=data[web_given]["email"]
            password=data[web_given]["password"]
            messagebox.showinfo(title=f"Your data for {web_given}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="No record", message=f"There is no password for {web_given}")

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
    new_data={
        web_given: {
            "email": email_given,
            "password": password_given,
        }
    }
    if len(web_given)==0 or len(email_given)==0 or len(password_given)==0:
        messagebox.showinfo(title="Oopsie!", message="Make sure to fill all the fields!")
    else:
            try:
                with open("passwords.json", "r") as f:
                    data=json.load(f)   #read
            except FileNotFoundError:
                with open("passwords.json", "w") as f:
                    json.dump(new_data, f, indent=4)    #write
            else:
                data.update(new_data)  # update

                with open("passwords.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
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
search_button=Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")

#entries:
web_entry=Entry(width=30)
web_entry.grid(row=1, column=1, sticky="w")
web_entry.focus()
email_entry=Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "mail@gmail.com")
pass_entry=Entry(width=30)
pass_entry.grid(row=3, column=1, sticky="w")

window.mainloop()