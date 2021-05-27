from tkinter import*

class calculator:

    def __init__(self, root):
        self.root = root
        root.geometry("650x650")
        root.title("Calculator")
        root.iconbitmap("cal.ico")
        root.configure(bg="cyan")

        f1 = Frame(root, width=80, height=350, bg="LightPink1")
        self.e1 = Entry(f1, width=15, border=2, font=("Times New Roman", 15, "bold"), justify=CENTER)
        self.e2 = Entry(f1, width=15, border=2, font=("Times New Roman", 15, "bold"), justify=CENTER)

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

        self.f5 = Frame(root, width=80, height=50, bg="CadetBlue1")
        self.l1 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER)
        self.l2 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER)
        self.l3 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER)
        self.l4 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER)
        self.l5 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER)

        self.f5.pack(side=BOTTOM, fill=BOTH, expand=1)
        self.l1.pack(side=LEFT, padx=10, pady=20)
        self.l2.pack(side=LEFT, padx=10, pady=20)
        self.l3.pack(side=LEFT, padx=10, pady=20)
        self.l4.pack(side=LEFT, padx=10, pady=20)
        self.l5.pack(side=LEFT, padx=10, pady=20)


        f1.pack(side=TOP, fill=BOTH)
        self.e1.pack(side=LEFT, padx=80, pady=30)
        self.e2.pack(side=LEFT, padx=80, pady=30)

        f2.pack(side=TOP, fill=BOTH)
        b1.pack(side=LEFT, padx= 105, pady=30)
        b2.pack(side=LEFT, padx= 105, pady=30)

        f3.pack(side=TOP, fill=BOTH)
        b3.pack(side=LEFT, padx=105, pady=30)
        b4.pack(side=LEFT, padx=105, pady=30)

        f4.pack(side=TOP, fill=BOTH)
        b5.pack(pady=25)

        f6= Frame(root, width=80, height=150, bg="coral")
        self.result_label = Label(f6, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text="answer")
        self.result_label.pack(side=TOP, pady=20)
        f6.pack(side=TOP, fill=BOTH)

    def plus(self, e1, e2):
        res = int(e1) + int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)
        self.l1 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e1.get())
        self.l2 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="+")
        self.l3 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e2.get())
        self.l4 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="=")
        self.l5 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)

        self.l1.pack(side=LEFT, padx=10, pady=20)
        self.l2.pack(side=LEFT, padx=10, pady=20)
        self.l3.pack(side=LEFT, padx=10, pady=20)
        self.l4.pack(side=LEFT, padx=10, pady=20)
        self.l5.pack(side=LEFT, padx=10, pady=20)



    def minus(self, e1, e2):
        res = int(e1) - int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)
        self.l1 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e1.get())
        self.l2 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="-")
        self.l3 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e2.get())
        self.l4 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="=")
        self.l5 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)

        self.l1.pack(side=LEFT, padx=10, pady=20)
        self.l2.pack(side=LEFT, padx=10, pady=20)
        self.l3.pack(side=LEFT, padx=10, pady=20)
        self.l4.pack(side=LEFT, padx=10, pady=20)
        self.l5.pack(side=LEFT, padx=10, pady=20)

    def multiple(self, e1, e2):
        res = int(e1) * int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)
        self.l1 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e1.get())
        self.l2 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="*")
        self.l3 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e2.get())
        self.l4 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="=")
        self.l5 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)

        self.l1.pack(side=LEFT, padx=10, pady=20)
        self.l2.pack(side=LEFT, padx=10, pady=20)
        self.l3.pack(side=LEFT, padx=10, pady=20)
        self.l4.pack(side=LEFT, padx=10, pady=20)
        self.l5.pack(side=LEFT, padx=10, pady=20)

    def divide(self, e1, e2):
        res = int(e1) / int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)
        self.l1 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e1.get())
        self.l2 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="/")
        self.l3 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e2.get())
        self.l4 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="=")
        self.l5 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)

        self.l1.pack(side=LEFT, padx=10, pady=20)
        self.l2.pack(side=LEFT, padx=10, pady=20)
        self.l3.pack(side=LEFT, padx=10, pady=20)
        self.l4.pack(side=LEFT, padx=10, pady=20)
        self.l5.pack(side=LEFT, padx=10, pady=20)

    def remainder(self, e1, e2):
        res = int(e1) % int(e2)
        self.result_label = Label(root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)
        self.result_label.pack(side=TOP, pady=20)
        self.l1 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e1.get())
        self.l2 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="%")
        self.l3 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=self.e2.get())
        self.l4 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text="=")
        self.l5 = Label(self.f5, width=10, height=2, font=("arial", 12, "bold"), justify=CENTER, text=res)

        self.l1.pack(side=LEFT, padx=10, pady=20)
        self.l2.pack(side=LEFT, padx=10, pady=20)
        self.l3.pack(side=LEFT, padx=10, pady=20)
        self.l4.pack(side=LEFT, padx=10, pady=20)
        self.l5.pack(side=LEFT, padx=10, pady=20)

    def result(self,condition):
        self.con = condition
        if self.con == 1:
            self.vanish()
            return self.plus(self.e1.get(),self.e2.get())
        elif self.con == 2:
            self.vanish()
            return self.minus(self.e1.get(),self.e2.get())
        elif self.con == 3:
            self.vanish()
            return self.multiple(self.e1.get(),self.e2.get())
        elif self.con == 4:
            self.vanish()
            return self.divide(self.e1.get(),self.e2.get())
        elif self.con == 5:
            self.vanish()
            return self.remainder(self.e1.get(),self.e2.get())
        else:
            pass

    def erase(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)

    def vanish(self):
        self.result_label.destroy()
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        self.l5.destroy()


root=Tk()
obj=calculator(root)
mainloop()