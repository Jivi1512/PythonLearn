from tkinter import *
root=Tk()
def click():
    name=entry.get()
    label1=Label(root, text=f"Welcome {name}")
    label1.grid()

#Creating labels
label1=Label(root, text="Hey Peeps!")
label1.grid()

#Creating buttons
button=Button(root, text="Enter your name", command=click, fg="blue" )
#state="active/disabled,normal", padx=50, pady=50
button.grid()

#Creating entry widget
entry=Entry(root,width=40, borderwidth=5,border=10)
entry.grid()
entry.insert(0,"Enter")
root.mainloop()