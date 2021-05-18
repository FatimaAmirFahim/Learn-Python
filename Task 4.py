from tkinter import*
root = Tk()
root.geometry("400x400")
root.configure(bg="PaleVioletRed1")
root.title("Calculator")
root.iconbitmap("cal.ico")
value=0
value2=0
f1= Frame(bg="sky blue", width=50, height=40)
l0 = Label(f1, text="Put the inputs and click the button to perform the following operation.",
           font=("Times New Roman", 15, "bold"))
def plus(value, value2):
    result = float(value) + float(value2)
    l1 = Label(root, text=result, width=30, font=("Times New Roman", 15))
    l1.pack(side=TOP, pady=20)

def minus(value, value2):
    result = float(value) - float(value2)
    l1 = Label(root, text=result, width=30, font=("Times New Roman", 15))
    l1.pack(side=TOP, pady=20)

def multiply(value, value2):
    result = float(value) * float(value2)
    l1 = Label(root, text=result, width=30, font=("Times New Roman", 15))
    l1.pack(side=TOP, pady=20)

def divide(value, value2):
    result = float(value) / float(value2)
    l1 = Label(root, text=result, width=30, font=("Times New Roman", 15))
    l1.pack(side=TOP, pady=20)

def remainder(value, value2):
    result = float(value) % float(value2)
    l1 = Label(root, text=result, width=30, font=("Times New Roman", 15))
    l1.pack(side=TOP, pady=20)


e1= Entry(f1, font=("Times New Roman", 15), width=20)
e2= Entry(f1, font=("Times New Roman", 15), width=20)
b1 = Button(root, text="plus",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : plus(e1.get(), e2.get()))
b2 = Button(root, text="minus",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : minus(e1.get(), e2.get()))
b3 = Button(root, text="multiply",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : multiply(e1.get(), e2.get()))
b4 = Button(root, text="divide",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : divide(e1.get(), e2.get()))
b5 = Button(root, text="remainder",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : remainder(e1.get(), e2.get()))





f1.pack(side=TOP, fill=X)
l0.pack(side=TOP, pady= 20)
e1.pack(side=LEFT, padx=200, pady= 50)
e2.pack(side=LEFT, padx=200,pady=50)
b1.pack(side=TOP, pady=20)
b2.pack(side=TOP, pady=20)
b3.pack(side=TOP, pady=20)
b4.pack(side=TOP, pady=20)
b5.pack(side=TOP, pady=20)

mainloop()