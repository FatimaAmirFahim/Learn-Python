from tkinter import*
root = Tk()
root.geometry("1200x800")
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
f2= Frame(bg="PaleVioletRed1", width=50, height=40)
b1 = Button(f2, text="plus",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : plus(e1.get(), e2.get()))
b2 = Button(f2, text="minus",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : minus(e1.get(), e2.get()))
f3= Frame(bg="PaleVioletRed1", width=50, height=40)
b3 = Button(f3, text="multiply",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : multiply(e1.get(), e2.get()))
b4 = Button(f3, text="divide",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : divide(e1.get(), e2.get()))
f4= Frame(bg="PaleVioletRed1", width=50, height=40)
b5 = Button(f4, text="remainder",  height=1, width=8, bg="LightYellow2", fg="dark khaki",
            font=("Times New Roman", 15),activebackground="dim gray", activeforeground="deep pink",
            command = lambda : remainder(e1.get(), e2.get()))





f1.pack(side=TOP, fill=X)
l0.pack(side=TOP, pady= 20)
e1.pack(side=LEFT, padx=200, pady= 50)
e2.pack(side=LEFT, padx=200,pady=50)
f2.pack(side=TOP, fill=X)
b1.pack(side=LEFT, padx=200, pady=20)
b2.pack(side=RIGHT,padx=200, pady=20)
f3.pack(side=TOP, fill=X)
b3.pack(side=LEFT,padx=200, pady=20)
b4.pack(side=RIGHT,padx=200, pady=20)
f4.pack(side=TOP, fill=X)
b5.pack(side=TOP, pady=20)

mainloop()