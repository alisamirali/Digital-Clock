from tkinter import *
from time import strftime

root = Tk()  # Creates tkinter window
root.title("Digital Clock By: Ali Samir")  # Adds title to tkinter window


# Function used to display time on the label
def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=("arial", 160, "bold"), bg="black", fg="white")

lbl.pack(anchor="center", fill="both", expand=1)

time()  # Time function is called

mainloop()  # Runs the application program
