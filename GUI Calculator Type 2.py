from tkinter import*

class calculator:

    def __init__(self, root):
        self.root = root
        root.geometry("650x650")
        root.title("Calculator")
        root.iconbitmap("cal.ico")
        root.configure(bg="cyan")

        f1 = Frame(root, width=80, height=350, bg="LightPink1")
        self.e1 = Entry(f1, width=30, border=5, justify=CENTER)
        self.e2 = Entry(f1, width=30, border=5, justify=CENTER)

        f2= Frame(root, width=80, height=100, bg="coral")
        b1= Button(f2, text="plus", font=("Times New Roman", 15, "bold"), width=8, bg="orange", fg="black",
                   activebackground="yellow", activeforeground="green",
                   command = lambda: [self.result(int(1)), self.erase()] )
        b2 = Button(f2, text="minus", font=("Times New Roman", 15, "bold"), width=8, bg="orange", fg="black",
                    activebackground="yellow", activeforeground="green",
                    command = lambda: [self.result(int(2)), self.erase()])

        f3= Frame(root, width=80, height=150, bg="coral")
        b3 = Button(f3, text="multiple", font=("Times New Roman", 15, "bold"), width=8, bg="orange", fg="black",
                    activebackground="yellow", activeforeground="green",
                    command = lambda: [self.result(int(3)), self.erase()])
        b4 = Button(f3, text="divide", font=("Times New Roman", 15, "bold"), width=8, bg="orange", fg="black",
                    activebackground="yellow", activeforeground="green",
                    command = lambda: [self.result(int(4)), self.erase()])

        f4= Frame(root, width=80, height=150, bg="coral")
        b5 = Button(f4, text="remainder", font=("Times New Roman", 15, "bold"), width=8, bg="orange", fg="black",
                    activebackground="yellow", activeforeground="green",
                    command = lambda: [self.result(int(5)), self.erase()])


        f1.pack(side=TOP, fill=BOTH)
        self.e1.pack(side=LEFT, padx=65, pady=30)
        self.e2.pack(side=LEFT, padx=65, pady=30)

        f2.pack(side=TOP, fill=BOTH)
        b1.pack(side=LEFT, padx= 105, pady=30)
        b2.pack(side=LEFT, padx= 105, pady=30)

        f3.pack(side=TOP, fill=BOTH)
        b3.pack(side=LEFT, padx=105, pady=30)
        b4.pack(side=LEFT, padx=105, pady=30)

        f4.pack(side=TOP, fill=BOTH)
        b5.pack(pady=25)

        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text="answer")
        self.result_label.pack(side=TOP, pady=20)

    def plus(self, e1, e2):
        res = int(e1) + int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)

    def minus(self, e1, e2):
        res = int(e1) - int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)

    def multiple(self, e1, e2):
        res = int(e1) * int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)

    def divide(self, e1, e2):
        res = int(e1) / int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)

    def remainder(self, e1, e2):
        res = int(e1) % int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)

    def result(self,condition):
        self.con=condition
        if self.con == 1:
            self.result_label.destroy()
            return self.plus(self.e1.get(),self.e2.get())
        elif self.con == 2:
            self.result_label.destroy()
            return self.minus(self.e1.get(),self.e2.get())
        elif self.con == 3:
            self.result_label.destroy()
            return self.multiple(self.e1.get(),self.e2.get())
        elif self.con == 4:
            self.result_label.destroy()
            return self.divide(self.e1.get(),self.e2.get())
        elif self.con == 5:
            self.result_label.destroy()
            return self.remainder(self.e1.get(),self.e2.get())
        else:
            pass

    def erase(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)


root=Tk()
obj=calculator(root)
mainloop()