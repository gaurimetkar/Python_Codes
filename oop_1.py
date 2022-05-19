# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateInterest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5

    def __init__(self, n, a):
        self.Name = n
        self.Amount = int(a)

    def Display(self):
        print("Name of the customer is", self.Name)
        print("Amount in the bank account is", self.Amount)

    def Deposit(self, amount):
        self.Amount = self.Amount + amount
        print("Account Balance is :", self.Amount)

    def Withdraw(self, amount):
        if amount < self.Amount:
            self.Amount = self.Amount - amount
            print("Account Balance is :", self.Amount)
        else:
            print("Insufficient balance in your account")

    def CalculateInterest(self):
        Interest = (self.Amount * self.ROI * 1) / 100           # Simple Interest= P x R x T ÷ 100 (Let T = 1)
        print("Interest is :", Interest)

def main():
    obj1 = BankAccount("Red", 1000)
    obj2 = BankAccount("Green", 2000)

    obj1.Display()
    amount = int(input("Enter the amount to be deposited :"))
    obj1.Deposit(amount)
    amount = int(input("Enter the amount to be withdrawn :"))
    obj1.Withdraw(amount)
    obj1.CalculateInterest()
    print()
    obj2.Display()
    amount = int(input("Enter the amount to be deposited :"))
    obj2.Deposit(amount)
    amount = int(input("Enter the amount to be withdrawn :"))
    obj2.Withdraw(amount)
    obj2.CalculateInterest()

if __name__ == "__main__":
    main()