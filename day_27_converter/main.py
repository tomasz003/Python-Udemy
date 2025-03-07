from tkinter import *

def button_clicked():
    mile_distance = float(input.get())
    km_distance=round(1.609*mile_distance,2)
    result.config(text=f"{km_distance}")


window=Tk()
window.title("Miles to km converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=30)

#Labels
miles=Label(text="miles", font=("Arial", 12, "bold"))
miles.config(padx=10, pady=0)
miles.grid(row=0, column=2)

km=Label(text="km", font=("Arial", 12, "bold"))
km.grid(row=1, column=2)
km.config(padx=10, pady=0)

eq=Label(text="is equal to", font=("Arial",12))
eq.grid(row=1, column=0)
eq.config(padx=10, pady=0)

result=Label(text="0", font=("Arial", 12))
result.grid(row=1, column=1)

#Button
button=Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

#Entry
input=Entry(width=10, font=("Arial",12))
input.grid(row=0, column=1)


window.mainloop()