from tkinter import *
root=Tk()
def buttonadd(num):
    current=e.get()
    e.insert(END, str(num))
def clear():
    digits=e.get()
    if digits:
        e.delete(len(digits)-1)
def result():
    sum=0
    digits=e.get()
    digitlist=digits.split("+")
    for i in digitlist:
        sum+=int(i)
    e.delete(0,END)
    e.insert(0,sum)
    return(sum)

e=Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
buttons={"1":(1,1,0),"2":(2,1,1),"3":(3,1,2),
         "4":(4,2,0),"5":(5,2,1),"6":(6,2,2),
         "7":(7,3,0),"8":(8,3,1),"9":(9,3,2),
         "+":("+",4,0),"0":(0,4,1),"=":("=",4,2)}
for display, (num,row,col) in buttons.items():
    if display=="=":
            Button(root,text=display, padx=40, pady=20, command=lambda: result()).grid(row=row,column=col)
    else:
         Button(root,text=display, padx=40, pady=20, command=lambda x=display: buttonadd(x)).grid(row=row,column=col)
buttonclear=Button(root,text="CLEAR",padx=120,pady=20,command=clear)
buttonclear.grid(row=5, columnspan=3)
root.mainloop()
"""
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button_add.grid(row=4,column=0)
button0.grid(row=4, column=1)
buttonequal.grid(row=4, column=2)
buttonclear.grid(row=5, columnspan=3)
button1=Button(root, text="1", padx=40, pady=20, command=lambda: buttonadd(1))
button2=Button(root, text="2", padx=40, pady=20, command=lambda: buttonadd(2))
button3=Button(root, text="3", padx=40, pady=20, command=lambda: buttonadd(3))
button4=Button(root, text="4", padx=40, pady=20, command=lambda: buttonadd(4))
button5=Button(root, text="5", padx=40, pady=20, command=lambda: buttonadd(5))
button6=Button(root, text="6", padx=40, pady=20, command=lambda: buttonadd(6))
button7=Button(root, text="7", padx=40, pady=20, command=lambda: buttonadd(7))
button8=Button(root, text="8", padx=40, pady=20, command=lambda: buttonadd(8))
button9=Button(root, text="9", padx=40, pady=20, command=lambda: buttonadd(9))
button0=Button(root, text="0", padx=40, pady=20, command=lambda: buttonadd(0))
button_add=Button(root,text="+",padx=40,pady=20,command=lambda: buttonadd("+"))
buttonequal=Button(root,text="=",padx=40,pady=20,command=result)
"""