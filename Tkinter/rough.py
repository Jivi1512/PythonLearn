from tkinter import *

root = Tk()

def buttonadd(num):
    current = e.get()
    e.insert(END, str(num))

def clear():
    digits = e.get()
    if digits:
        e.delete(len(digits)-1)

def result():
    total = 0
    digits = e.get()
    digitlist = digits.split("+")
    for i in digitlist:
        total += int(i)
    e.delete(0, END)
    e.insert(0, total)
    return total

# Create the Entry widget
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# List of button values
buttons = [
    ("1", 1), ("2", 2), ("3", 3), 
    ("4", 4), ("5", 5), ("6", 6), 
    ("7", 7), ("8", 8), ("9", 9),
    ("0", 0), ("+", "+")
]

# Create the number buttons dynamically
row = 1
col = 0
for text, value in buttons:
    button = Button(root, text=text, padx=40, pady=20, command=lambda v=value: buttonadd(v))
    button.grid(row=row, column=col)
    col += 1
    if col > 2:  # Move to the next row
        col = 0
        row += 1

# Additional buttons
button_clear = Button(root, text="CLEAR", padx=120, pady=20, command=clear)
button_clear.grid(row=row, columnspan=3)

button_equal = Button(root, text="=", padx=40, pady=20, command=result)
button_equal.grid(row=row+1, column=0, columnspan=3)

root.mainloop()
