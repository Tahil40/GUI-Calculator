# Importing Modules.....
from tkinter import *

# Creating Windows....
window = Tk()
window.geometry("400x320")
window.title("Calculator - Created by Mohd.Tahil")
window.wm_iconbitmap("arc.ico.ico")
window .config(background="black")
window.resizable(False, False)

# MAKING the func for button....
def click(event):
    global scvalue
    global scvar
    value = event.widget.cget("text")

    if value=="=":
        if scvalue.get().isdigit():
            value0 = int(scvalue.get())
        
        else:
            try:
                value0 = eval(scvalue.get())
            
            except Exception as e:
                value0 = "Error"
                print(e)

        scvar.set(value0)
        scvalue.update()

    elif value=="C":
        scvar.set("")
        scvalue.update()

    else:
        scvar.set(scvalue.get()+value)
        scvalue.update()

# Creating screen on windos...
scvar = StringVar()
scvar.set("")
scvalue = Entry(window, font="lucida 40 bold", bg="black", fg="yellow", textvariable=scvar)
scvalue.pack(pady=5, padx=5)

#Creating Frames as buttons.....
f0 = Frame(window, bg="black")

b0 = Button(f0, text="9", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne", padx=2)
b0.bind("<Button-1>", click)

b0 = Button(f0, text="8", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne")
b0.bind("<Button-1>", click)

b0 = Button(f0, text="7", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne")
b0.bind("<Button-1>", click)

b0 = Button(f0, text="6", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne")
b0.bind("<Button-1>", click)

b0 = Button(f0, text="5", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne")
b0.bind("<Button-1>", click)

b0 = Button(f0, text="4", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne")
b0.bind("<Button-1>", click)

b0 = Button(f0, text="3", font="lucida 30 bold", bg="black", fg="yellow")
b0.pack(side=LEFT, anchor="ne", padx=2)
b0.bind("<Button-1>", click)
f0.pack(fill=X)

# Creating Frame 2......
f1 = Frame(window, bg="black")
b1 = Button(f1, text="2", font="lucida 30 bold", bg="black", fg="yellow")
b1.pack(side=LEFT, anchor="ne",padx=2, pady=2)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="1", font="lucida 30 bold", bg="black", fg="yellow")
b1.pack(side=LEFT, anchor="ne", pady=2)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="00", font="lucida 30 bold", bg="black", fg="yellow")
b1.pack(side=LEFT, anchor="ne", pady=2)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="0", font="lucida 30 bold", bg="black", fg="yellow")
b1.pack(side=LEFT, anchor="ne", pady=2)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="+", font="lucida 30 bold", bg="black", fg="blue", padx=5)
b1.pack(side=LEFT, anchor="ne", padx=5, pady=2)
b1.bind("<Button-1>", click)

b1= Button(f1, text="-", font="lucida 30 bold", bg="black", fg="green", padx=5)
b1.pack(side=LEFT, anchor="ne", padx=5, pady=2)
b1.bind("<Button-1>", click)
f1.pack(fill=X)

# Creating Frame 3....
f2 = Frame(window, bg="black")
b2 = Button(f2, text="/", font="lucida 30 bold", bg="black", fg="blue", padx=6)
b2.pack(side=LEFT, anchor="ne", padx=2)
b2.bind("<Button-1>", click)

b2 = Button(f2, text="*", font="lucida 30 bold", bg="black", fg="brown", padx=4)
b2.pack(side=LEFT, anchor="ne")
b2.bind("<Button-1>", click)

b2 = Button(f2, text="%", font="lucida 30 bold", bg="black", fg="yellow", padx=6)
b2.pack(side=LEFT, anchor="ne")
b2.bind("<Button-1>", click)

b2 =  Button(f2, text="C", font="lucida 30 bold", bg="black", fg="purple", padx=5)
b2.pack(side=LEFT, anchor="ne")
b2.bind("<Button-1>", click)

b2 = Button(f2, text="=", font="lucida 30 bold", bg="black", fg="aqua", padx=33)
b2.pack(side=LEFT, anchor="ne")
b2.bind("<Button-1>", click)
f2.pack(fill=X)

# Closing the Windos...
window.mainloop()