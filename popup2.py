#Program to check whether the input of user is correct or not, if not then give error message with pop-up menu(GUI)
#Program written by Shubham Rachha aka Titan Spy

def error():               #fuction to show error message
    import tkinter
    from tkinter import messagebox

    root=tkinter.Tk()
    root.withdraw()

    messagebox.showerror("Error","Wrong Input")
    root.mainloop()

def evaluate(event):             #function to evaluate the user input
    E=int(e.get())
    if (E==6):
        res.configure(text="Answer is right "+ str(e.get()))
    else:
        res.configure(text="Answer is wrong "+ str(e.get()))
        res.configure(error())

from tkinter import *  
top=Tk()
top.title("Titan spy")             #Title of our GUI
top.minsize(300,300)
w=Label(top,text="solve this, 3+3=?")
w.pack()
e=Entry(top)
e.bind('<Return>',evaluate)             #If user press the enter key then also user will get the output
e.pack()
b=Button(top,text="click")            #Button for user to click and check the answer
b.bind('<Button-1>',evaluate)
b.pack()
res=Label(top)
res.pack()
top.mainloop()

