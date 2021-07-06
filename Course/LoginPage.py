from task5 import*

class Login_page:
    def __init__(self, root):
        self.root = root
        root.geometry("500x500")
        root.title("Login Page")
        root.configure(bg = "sky blue")


        f1 = Frame(root, height= 130,bg = "sky blue" )
        label = Label(f1, width=20, height=4, text="Login Page", font=("Times New Roman", 15, "bold"), bg="LightPink1")
        l1= Label(f1, width=7, height=1, text="Username", font=("Times New Roman", 15, "bold"), bg = "sky blue")
        self.e1= Entry(f1, justify=CENTER, font=("arial", 14), width=30, borderwidth=4)

        f2 = Frame(root, height=200, bg = "sky blue")
        l2 = Label(f2, width=7, height=1, text="Password", font=("Times New Roman", 15, "bold"), bg = "sky blue")
        self.e2 = Entry(f2, justify=CENTER, font=("arial", 14), width=30, borderwidth=4)

        f3= Frame(root, height=200, bg = "sky blue")
        b1= Button(f3, text="Login", font= ("Times New Roman", 16, "bold"), width=11, height=1, bg="orange", fg="black",
                   activebackground="black", activeforeground="orange", command= lambda:[self.signin(self.e1.get(), self.e2.get())] )



        label.pack(side=TOP, pady=20, padx=20)
        f1.pack(side=TOP, fill=X)
        l1.pack(side= LEFT,padx=50, pady=10)
        self.e1.pack(side=LEFT, padx=10, pady=10)

        f2.pack(side=TOP,fill=X)
        l2.pack(side=LEFT,padx=50, pady=20)
        self.e2.pack(side=LEFT, padx=10, pady=20)

        f3.pack(side=BOTTOM, fill=X)
        b1.pack(side=TOP, pady=100, padx=30)

    def erase(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def signin(self, name, password):
        if name == "fatima":
            self.erase()
            if password == "1234":
                self.erase()
                self.root.destroy()
                mygui()


            else:
                print("Password is wrong.")
        else:
            print("Username is wrong.")



root = Tk()
obj = Login_page(root)
mainloop()
