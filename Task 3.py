from tkinter import*
window=Tk()
window.geometry("800x800")
window.title("GUI TASK 3")
window.iconbitmap("GUI logo.ico")
window.configure(bg="blue")

f1=Frame(window, bg="red", width=800, height=800)
b1=Button(f1, text="Button", font=("Times New Roman", 30, "bold"), bg="light green", fg="yellow",
          activebackground="sky blue", activeforeground="grey", border=20)
b2=Button(f1, text="Button", font=("Times New Roman", 30, "bold"), bg="light green", fg="yellow",
          activebackground="sky blue", activeforeground="grey", border=20)
b3=Button(f1, text="Button", font=("Times New Roman", 30, "bold"), bg="light green", fg="yellow",
          activebackground="sky blue", activeforeground="grey", border=20)
f2= Frame(window, bg="yellow", width="940")
f3= Frame(f2, bg="purple", width=940, height=350)
l1=Label(f3, text="Label", font=("Times New Roman", 30, "bold"),bg="grey", width=10)
e1=Entry(f3, width=20, font=("Times New Roman", 30, "bold"))
b4=Button(f3, text="Button", font=("Times New Roman", 30, "bold"), bg="light green", fg="yellow",
          activebackground="sky blue", activeforeground="grey", border=20)
f4= Frame(f2, bg="black", width=940, height=500)
e2=Entry(f4, width=20, font=("Times New Roman", 30, "bold"))
e3=Entry(f4, width=20, font=("Times New Roman", 30, "bold"))



f1.pack(side=LEFT, fill=Y)
b1.pack(padx=100, pady= 40)
b2.pack(padx=100, pady= 40)
b3.pack(padx=100, pady= 40)
f2.pack(side=RIGHT, fill=Y)
f3.pack(side=TOP, fill=X)
l1.pack(padx=250, pady=25)
e1.pack(padx=250, pady=25)
b4.pack(padx=250, pady=25)
f4.pack(side=TOP, fill=BOTH)
e2.pack(side=TOP, padx=250, pady=53)
e3.pack(side=TOP, padx=250, pady=52)


mainloop()