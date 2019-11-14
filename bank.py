
class Account():
    def __init__(self, balance, overdraft, type):
        self.balance = balance
        self.overdraft = False
        self.type = False

    def isOverdraft(self, bool):
        self.type = bool

    def displayBalance(self):
        print("Account balance: " +str(self.balance))
        print(self.overdraft)

    def displayNewBalance(self):
        print("New account balance: " +str(self.balance))


    def deposit(self, amount):
        print(amount)
        self.balance += amount
        self.displayNewBalance()
        if self.overdraft == True:
            if self.balance >= 0:
                self.overdraft = False


    def withdraw(self, amount):
        print(amount)
        #self.balance -= amount
        #self.displayNewBalance()

        if self.balance < amount:
            print("Warning")
            if self.type == True:
                self.balance -= amount
                self.displayNewBalance()
                self.overdraft = True
            else:
                print("Not an overdraft account")
        else:
            self.balance -= amount
            self.displayBalance()


    def overdraftAction(self):
        if self.type == True:
            print("")
        else:
            print("No")
        return

def main():
    normAccound = Account(200, False, False)
    normAccound.isOverdraft(True)
    normAccound.displayBalance()
    normAccound.withdraw(400)
    normAccound.displayBalance()
    normAccound.deposit(400)
    normAccound.displayBalance()

main()
