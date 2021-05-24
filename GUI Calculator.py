from tkinter import*


class Calculator:

    def __init__(self, root):
        self.root = root

        root.geometry("400x400")
        root.title("GUI Calculator")
        root.iconbitmap("cal.ico")
        root.configure(bg="sky blue")

        f1 = Frame(root, height=40, bg="sky blue")
        self.v1 = Entry(f1, width=10, justify=CENTER, font=("arial", 14), borderwidth=4)
        self.v2 = Entry(f1, width=10, justify=CENTER, font=("arial", 14), borderwidth=4)

        f2 = Frame(root, height=150)
        f2top = Frame(f2, height=50, bg="sky blue")
        plusbut = Button(f2top, width=8, text="plus", bg="gray92", activebackground="orange",
                         font=("arial", 12, "bold"),
                         command=lambda: plus(self.v1.get(), self.v2.get()))
        minusbut = Button(f2top, width=8, text="minus", bg="gray92", activebackground="orange",
                          font=("arial", 12, "bold"),
                          command=lambda: minus(self.v1.get(), self.v2.get()))
        f2center = Frame(f2, height=50, bg="sky blue")
        multibut = Button(f2center, width=8, text="multiple", bg="gray92", activebackground="orange",
                          font=("arial", 12, "bold"),
                          command=lambda: multiple(self.v1.get(), self.v2.get()))
        divibut = Button(f2center, width=8, text="divide", bg="gray92", activebackground="orange",
                         font=("arial", 12, "bold"),
                         command=lambda: divide(self.v1.get(), self.v2.get()))
        f2bottom = Frame(f2, height=50, bg="sky blue")
        rembut = Button(f2bottom, width=8, text="reminder", bg="gray92", activebackground="orange",
                        font=("arial", 12, "bold"),
                        command=lambda: rem(self.v1.get(), self.v2.get()))
        clear = Button(f2bottom, width=8, text="clear", bg="gray92", activebackground="orange",
                        font=("arial", 12, "bold"),
                        command=lambda: erase(self))

        f1.pack(side=TOP, fill=BOTH)
        self.v1.pack(side=LEFT, padx=30, pady=20)
        self.v2.pack(side=LEFT, padx=30, pady=20)
        f2.pack(side=TOP, fill=BOTH)
        f2top.pack(side=TOP, fill=BOTH, expand=1)
        plusbut.pack(side=LEFT, pady=10, padx=55)
        minusbut.pack(side=LEFT, pady=10, padx=55)
        f2center.pack(side=TOP, fill=BOTH, expand=1)
        multibut.pack(side=LEFT, pady=10, padx=55)
        divibut.pack(side=LEFT, pady=10, padx=55)
        f2bottom.pack(side=TOP, fill=BOTH, expand=1)
        rembut.pack(pady=10)
        clear.pack(pady=10)

        def plus(v1, v2):
            result = float(v1) + float(v2)
            self.result_label = Label(self.root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.result_label.pack(side=TOP, pady=20)

        def minus(v1, v2):
            result = float(v1) - float(v2)
            self.result_label = Label(self.root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.result_label.pack(side=TOP, pady=20)

        def multiple(v1, v2):
            result = float(v1) * float(v2)
            self.result_label = Label(self.root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.result_label.pack(side=TOP, pady=20)

        def divide(v1, v2):
            result = float(v1) / float(v2)
            self.result_label = Label(self.root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.result_label.pack(side=TOP, pady=20)

        def rem(v1, v2):
            result = float(v1) % float(v2)
            self.result_label = Label(self.root, width=30, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.result_label.pack(side=TOP, pady=20)
        def erase(self):
            self.v1.delete(0, END)
            self.v2.delete(0, END)
            self.result_label.destroy()




root = Tk()
obj = Calculator(root)
mainloop()