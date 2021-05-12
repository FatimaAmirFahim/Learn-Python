class Calculator:
    def __init__(self):
        self.value1 = int(input("Enter number 1: "))
        self.value2 = int(input("Enter number 2: "))

        print("Operation:")
        print("1. Addition.")
        print("2. Subtraction.")
        print("3. Multiplication.")
        print("4. Division.")
        print("5. Remainder")
        print("6. Press any other number to quit calculating.")

    def addition(self):
        print("Addition Result: ", self.value1 + self.value2)
    def subtraction(self):
        print("Subtraction Result: ", self.value1 - self.value2)
    def multiplication(self):
        print("Multiplication Result: ", self.value1 * self.value2)
    def division(self):
        print("Division Result: ", self.value1 / self.value2)
    def remainder(self):
        print("Remainder Result: ", self.value1 % self.value2)



while True:

    obj = Calculator()

    choice= int(input("Enter the operation: "))
    if choice == 1:
        obj.addition()
    elif choice == 2:
        obj.subtraction()
    elif choice == 3:
        obj.multiplication()
    elif choice == 4:
        obj.division()
    elif choice == 5:
        obj.remainder()
    else:
        break





