from tkinter import *

def button_clicked():
    inp_text = input.get()
    my_label.config(text=inp_text)


window=Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

#Label
my_label=Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.place(x=0,y=0)
my_label.grid(row=0, column=0)

#Button
button=Button(text="Wyślij", command=button_clicked)
button.grid(row=1, column=1)

new_button=Button(text="skibidi")
new_button.grid(row=0, column=2)

#Entry
input=Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()